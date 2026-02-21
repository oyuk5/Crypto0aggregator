from app.exchanges.BinanceClient import BinanceClient
from app.exchanges.BybitClient import BybitClient
from app.exchanges.KrakenClient import KrakenClient


def main():
    clients = [
        BinanceClient(),
        BybitClient(),
        KrakenClient()
    ]
    results = {}
    for client in clients:
        coin = "BTC"
        price = client.get_price(coin)
        results[client] = price
        if price > 0:
            print(f"Price: ${price:,.2f}")
        else:
            print("Did not get price")

if __name__ == "__main__":
        main()

