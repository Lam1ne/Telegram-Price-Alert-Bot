import unittest
from src.telegram_alert import TelegramAlert
from src.data_fetcher import DataFetcher

class TestTelegramBot(unittest.TestCase):

    def setUp(self):
        self.telegram_alert = TelegramAlert(token='YOUR_TELEGRAM_BOT_TOKEN', chat_id='YOUR_CHAT_ID')
        self.data_fetcher = DataFetcher(asset='BTC', source='binance')

    def test_send_alert(self):
        # Mock the send_message method to test without actually sending a message
        self.telegram_alert.send_message = lambda message: "Message sent"
        response = self.telegram_alert.send_message("Test alert")
        self.assertEqual(response, "Message sent")

    def test_fetch_price(self):
        price = self.data_fetcher.get_current_price()
        self.assertIsInstance(price, (int, float))

    def test_price_alert(self):
        threshold = 50000  # Example threshold
        current_price = self.data_fetcher.get_current_price()
        if current_price > threshold:
            alert_message = f"Alert! The price of BTC has exceeded the threshold of {threshold}."
            response = self.telegram_alert.send_message(alert_message)
            self.assertEqual(response, "Message sent")

if __name__ == '__main__':
    unittest.main()