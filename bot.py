import discord
import asyncpraw
import asyncio
from discord.ext import tasks

from config import (
    REDDIT_CLIENT_ID,
    REDDIT_CLIENT_SECRET,
    REDDIT_USER_AGENT,
    DISCORD_BOT_TOKEN,
    DISCORD_CHANNEL_ID,
    ROLE_ID
)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

reddit = None  
posted_posts = set()  

async def fetch_giveaways():
    global reddit, posted_posts
    try:
        subreddit = await reddit.subreddit("Chipotle")
        async for submission in subreddit.new(limit=10):
            flair_text = submission.link_flair_text or ""

            if (("giveaway" in submission.title.lower() or "🎁Reward Giveaway🎁" in flair_text) 
                and submission.id not in posted_posts):

                channel = client.get_channel(DISCORD_CHANNEL_ID)
                if channel is None:
                    print(f"Error: Could not find channel {DISCORD_CHANNEL_ID}")
                    return

                role_mention = f"<@&{ROLE_ID}>"

                embed = discord.Embed(
                    title=submission.title,
                    url=submission.url,
                    description=submission.selftext[:4000] if submission.selftext else None,
                    color=discord.Color.red()
                )
                embed.set_footer(text=f"Posted by u/{submission.author}")

                if submission.url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                    embed.set_image(url=submission.url)

                await channel.send(f"{role_mention} 🚨 New Chipotle Giveaway Alert! 🚨", embed=embed)
                posted_posts.add(submission.id)

    except Exception as e:
        print(f"Error while fetching Reddit posts: {e}")

@tasks.loop(minutes=1)
async def check_reddit():
    await fetch_giveaways()

@client.event
async def on_ready():
    global reddit
    print(f"Logged in as {client.user}")

    reddit = asyncpraw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )

    if not check_reddit.is_running():
        check_reddit.start()

client.run(DISCORD_BOT_TOKEN)
