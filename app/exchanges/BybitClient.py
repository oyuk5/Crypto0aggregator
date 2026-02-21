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
        try:
            if data and data.get("retCode") == 0:
                result = data.get("result", {})
                items = result.get("list", [])
                if items:
                    price = items[0].get("lastPrice")
                    return float(price)
        except Exception as e:
            print(f"Error while parsing Bybit: {e}")
        return 0.0