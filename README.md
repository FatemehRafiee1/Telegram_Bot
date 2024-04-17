# Telegram Bot

This Telegram bot is designed using `aiogram` to perform a few tasks including providing assistance based on user input (chat-gpt), fetching cryptocurrency information, telling jokes, and sending IELTS speaking questions on specific topics.

## Getting Started

To use the bot, follow these steps:

1. **Install Dependencies:** Ensure you have all the necessary dependencies installed.


2. **Configure the Tokens:**

Obtain a Telegram Bot API token from the BotFather on Telegram. Once you have the token, replace `telegram_bot_token` in the code with your actual token.
Besides telegram token, you need a coinex and chatgpt api key as well.

3. **Run the Bot:**

Execute the Python script (`telegram_bot.py`) to start the bot.

## Functionality

### Commands

- `/start`: Initiates the bot and welcomes the user. If the user is returning, it greets them back.
- `/menu`: Displays the main menu of options for the user to choose from.

### Menu Options

1. **GPT**: Engages the bot in a conversation where it provides responses based on user input.
2. **IELTS**: Offers conversation starters on various topics.
3. **Joke**: Tells a random joke fetched from an external API.
4. **Crypto**: Provides information about cryptocurrencies including current prices and percentage changes.

### Additional Notes

- Users can interrupt ongoing conversations with gpt by typing `cancel` or `stop`.
- Questions for IELTS are stored in mongodb beforehand.
- Users' ids and their conversation history with Chat GPT will be also available in mongodb database.

