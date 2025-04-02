class DataFetcher:
    def __init__(self, asset, source='binance'):
        self.asset = asset
        self.source = source

    def get_price(self):
        if self.source == 'binance':
            return self._fetch_price_from_binance()
        elif self.source == 'yahoo':
            return self._fetch_price_from_yahoo()
        else:
            raise ValueError("Unsupported data source")

    def _fetch_price_from_binance(self):
        import requests
        url = f'https://api.binance.com/api/v3/ticker/price?symbol={self.asset.upper()}USDT'
        response = requests.get(url)
        data = response.json()
        return float(data['price'])

    def _fetch_price_from_yahoo(self):
        import yfinance as yf
        asset_data = yf.Ticker(self.asset)
        return asset_data.history(period='1d')['Close'].iloc[-1]