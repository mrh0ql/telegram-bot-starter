"""
Telegram Bot Starter with AI integration.
Fill in BOT_TOKEN and OPENAI_API_KEY in a .env file (see .env.example).
Run: python bot.py
"""
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

logging.basicConfig(level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! I'm your AI assistant bot. Send me any message and I'll reply."
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start - begin\n/help - this message\nOr just send a message.")


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_text}],
    )
    await update.message.reply_text(resp.choices[0].message.content)


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    app.run_polling()


if __name__ == "__main__":
    main()
