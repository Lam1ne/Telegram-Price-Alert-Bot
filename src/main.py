import time
import logging
from telegram_alert import TelegramAlert
from data_fetcher import DataFetcher
from config import TELEGRAM_TOKEN, CHAT_ID, ASSET, PRICE_THRESHOLD

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Starting the Telegram alert bot...")
    
    data_fetcher = DataFetcher()
    telegram_alert = TelegramAlert(TELEGRAM_TOKEN, CHAT_ID)

    while True:
        current_price = data_fetcher.get_current_price(ASSET)
        logging.info(f"Current price of {ASSET}: {current_price}")

        if current_price > PRICE_THRESHOLD:
            telegram_alert.send_alert(f"The price of {ASSET} has exceeded the threshold! Current price: {current_price}")
        
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()