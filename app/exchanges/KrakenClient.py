from app.exchanges.BaseClient import BaseClient
class KrakenClient(BaseClient):
    def __init__(self):
        super().__init__("https://api.kraken.com/0/public")
        self.ticker_map = {
            "BTC" : "XBT"
        }
    def get_price(self, symbol: str) -> float:
        kraken_symbol = self.ticker_map.get(symbol)
        pair = f"{kraken_symbol.upper()}USD"

        data = self._request("/Ticker",params = {"pair":pair})
        try:
            if data and not data.get("error"):
                result = data.get("result", {})
                for key, value in result.items():
                    price = value.get("c",[0])[0]
                    return float(price)
        except Exception as e:
            print(f"Error while parsing Kraken: {e}")

        return 0.0