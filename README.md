# ChipotleDetector: Discord Giveaway Notifier

## Description

ChipotleDetector is a Discord bot that monitors the r/Chipotle subreddit for new posts containing the keywords "giveaway" or the tag "🎁Reward Giveaway🎁." When it detects a qualifying post, it automatically posts an alert in a designated Discord channel.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- **Python 3**: [Download Python](https://www.python.org/downloads/)
- **Discord Bot Token**: Obtainable from the [Discord Developer Portal](https://discord.com/developers/applications)
- **Reddit API Credentials**: Obtainable from the [Reddit Developer Portal](https://www.reddit.com/prefs/apps)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/lindorG/ChipotleDetector.git
   cd ChipotleDetector
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add the following lines:
     ```ini
     DISCORD_TOKEN=your_discord_bot_token_here
     CLIENT_ID=your_reddit_client_id_here
     CLIENT_SECRET=your_reddit_client_secret_here
     USER_AGENT=your_reddit_user_agent_here
     CHANNEL_ID=your_discord_channel_id_here
     ```
   Replace each placeholder with your actual credentials.

### Running the Bot

To start the bot, run:

```bash
python bot.py
```

The bot will now monitor r/Chipotle for giveaway posts and notify the configured Discord channel.

## Troubleshooting

- **Bot not responding?**
  - Ensure the bot has the necessary permissions to send messages in the specified Discord channel.
  - Check that the `DISCORD_TOKEN` is correctly set in the `.env` file.
  
- **Reddit API issues?**
  - Verify that `CLIENT_ID`, `CLIENT_SECRET`, and `USER_AGENT` are correctly configured in the `.env` file.
  - Ensure that your Reddit API credentials have access to public subreddit data.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Author

- GitHub: [lindorG](https://github.com/lindorG)

## Version History

- **1.0.0**
  - Initial release
  - Automatic giveaway detection and Discord notifications

