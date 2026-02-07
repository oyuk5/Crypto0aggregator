from app.exchanges.BaseClient import BaseClient
class BinanceClient(BaseClient):
    def __init__(self):
        super().__init__("https://api.binance.com/api/v3")
    def get_price(self,symbol:str) ->float:
        ticker = f"{symbol.upper()}USDT"
        data = self._request("/ticker/price", params={"symbol":ticker})
        if data and "price" in data:
            return float(data["price"])
        return 0.0