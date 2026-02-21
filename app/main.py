from app.exchanges.BinanceClient import BinanceClient
from app.exchanges.BybitClient import BybitClient

def main():
    clients = [
        BinanceClient(),
        BybitClient(),
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

