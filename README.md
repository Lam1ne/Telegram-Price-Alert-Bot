# Telegram Price Alert Bot

This project is a Python bot that sends alerts to a Telegram chat when the price of a specified asset (such as Bitcoin or a stock) exceeds a defined threshold. It utilizes the Binance or Yahoo Finance API to fetch the current price of the asset.

## Project Structure

```
python-telegram-bot
├── src
│   ├── main.py            # Entry point of the bot
│   ├── config.py          # Configuration settings
│   ├── telegram_alert.py   # Telegram alert functionality
│   └── data_fetcher.py     # Data fetching from APIs
├── tests
│   └── test_bot.py        # Unit tests for the bot
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-telegram-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the bot:
   - Open `src/config.py` and set your Telegram bot token, the asset you want to monitor, and the price threshold for alerts.

4. Run the bot:
   ```
   python src/main.py
   ```

## Usage Guidelines

- The bot will monitor the specified asset's price and send an alert to your Telegram chat when the price exceeds the defined threshold.
- Ensure that your Telegram bot is set up correctly and that you have the necessary permissions to send messages to your chat.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.
