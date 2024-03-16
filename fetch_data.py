# fetch_data.py
from jugaad_data.nse import NSELive
import json
from datetime import datetime


def fetch_and_save_stock_data(symbol):
    nse_live = NSELive()
    stock_quote = nse_live.stock_quote(symbol)
    filename = f"data/{symbol}_{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(filename, "w") as file:
        json.dump(stock_quote, file)
    print(f"Data for {symbol} saved to {filename}")


if __name__ == "__main__":
    symbols = ["SBIN", "RELIANCE", "TCS"]
    for symbol in symbols:
        fetch_and_save_stock_data(symbol)
