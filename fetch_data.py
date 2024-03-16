from jugaad_data.nse import NSELive
import json
from datetime import datetime
import os  # Import os module


def fetch_and_save_stock_data(symbol):
    nse_live = NSELive()
    stock_quote = nse_live.stock_quote(symbol)

    # Ensure 'data' directory exists
    data_directory = "data"
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)  # Create the 'data' directory if it does not exist

    filename = f"{data_directory}/{symbol}_{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(filename, "w") as file:
        json.dump(stock_quote, file)
    print(f"Data for {symbol} saved to {filename}")


if __name__ == "__main__":
    symbols = ["SBIN", "RELIANCE", "TCS"]  # Add your symbols here
    for symbol in symbols:
        fetch_and_save_stock_data(symbol)
