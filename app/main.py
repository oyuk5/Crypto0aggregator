from app.exchanges.BinanceClient import BinanceClient

def main():
    client = BinanceClient()
    coin = "BTC"
    price = client.get_price(coin)
    if price > 0:
        print(f"Price: ${price:,.2f}")
    else:
        print("Did not get price")

if __name__ == "__main__":
        main()

