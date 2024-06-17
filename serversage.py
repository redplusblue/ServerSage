#! /usr/bin/env python3
import logging, os, asyncio, sys
from telegram import Bot

from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
AUTHORIZED_USERNAME = os.getenv('AUTHORIZED_USERNAME')
AUTHORIZED_USER_CHAT_ID = os.getenv('AUTHORIZED_USER_CHAT_ID')

bot = Bot(token=TELEGRAM_TOKEN)

async def send_alert(message: str) -> None:
    """Send an alert message to the authorized user."""
    await bot.send_message(chat_id=AUTHORIZED_USER_CHAT_ID, text=message, parse_mode="Markdown")
    
if __name__ == "__main__":
    argc = len(sys.argv)
    argv = sys.argv
    if argc < 2:
        print("Usage: serversage <message>")
        print("serversage uses markdown to format the message.")
        sys.exit(1)
    else:
        asyncio.run(send_alert(argv[1]))