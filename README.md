# Telegram AI Bot Starter

A production-ready Telegram bot powered by OpenAI. Send it any message and it replies with AI. Great as a freelance deliverable or a base for client bots.

## Features
- `/start` and `/help` commands
- AI replies to any text message (GPT-4o-mini)
- Clean async structure, easy to extend

## Setup
1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a bot with @BotFather on Telegram to get a token.
3. Copy `.env.example` to `.env` and fill in your tokens:
   ```bash
   cp .env.example .env
   ```
4. Run it:
   ```bash
   python bot.py
   ```

## Selling this as a service
- Basic ($50): deploy this bot with the client's branding.
- Standard ($150): add custom commands and a knowledge base.
- Premium ($300): full custom bot with database, payments, or integrations.

## License
MIT
