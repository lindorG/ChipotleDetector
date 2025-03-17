# Chipotle Giveaway Detector

## 📌 About
Chipotle Giveaway Detector is a Discord bot that monitors r/Chipotle on Reddit for new giveaway posts. If a post contains **"giveaway"** in the title or has the flair **"🎁Reward Giveaway🎁"**, the bot sends an embedded message to a designated Discord channel.

## 🔧 Setup

### 1. Install Dependencies
Run the following command to install the required libraries:

```bash
pip install -r requirements.txt
```

### 2. Configure the Bot
Create a `config.py` file and add the following credentials:

```python
REDDIT_CLIENT_ID = "your_reddit_client_id"
REDDIT_CLIENT_SECRET = "your_reddit_client_secret"
REDDIT_USER_AGENT = "your_user_agent"
DISCORD_BOT_TOKEN = "your_discord_bot_token"
DISCORD_CHANNEL_ID = your_discord_channel_id  # Replace with an integer
```

### 3. Run the Bot
Start the bot with:

```bash
python bot.py
```

## ⚙️ How It Works
- The bot checks r/Chipotle for new posts every minute.
- If a giveaway post is detected **and hasn’t been posted before**, it sends an embed to the configured Discord channel.
- It prevents duplicate postings by tracking previously posted giveaway IDs.

## Requirements
- Python 3.8+
- Installed dependencies from `requirements.txt`

## Contributing
Feel free to modify the bot for your needs. If you encounter issues, open a discussion or fork the project.

