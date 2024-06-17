# ServerSage
Simple Telegram Bot that fetches alerts from my server using a shell command and sends them to me on Telegram.

## Installation
1. Clone the repository 
2. Install the requirements using `pip install -r requirements.txt`
3. Create a `.env` file in the root directory and add the following:
```
TELEGRAM_TOKEN=<YOUR_TELEGRAM_BOT_TOKEN>
AUTHORIZED_USERNAME=<YOUR_TELEGRAM_USERNAME>
AUTHORIZED_USER_CHAT_ID=<YOUR_TELEGRAM_CHAT_ID>
```
4. Run the bot using `python bot.py`
5. Optionally, to run the bot as a shell command, add the Script location to $PATH and either run the script using `serversage.py` or create an alias in your `.bashrc` or `.zshrc` file.
