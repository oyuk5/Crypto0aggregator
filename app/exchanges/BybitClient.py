from app.exchanges.BaseClient import BaseClient
class BybitClient(BaseClient):
    def __init__(self):
        super().__init__("https://api.bybit.com/v5")
    def get_price(self, symbol: str) -> float:
        ticker = f"{symbol.upper()}USDT"
        params = {
            "category" : "spot",
            "symbol" : "BTCUSDT"
        }
        data = self._request("/market/tickers",params)
        if data and "price" in data:
            return float(data["price"])
        return 0.0