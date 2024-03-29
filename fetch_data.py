import sys
from jugaad_data.nse import NSELive
import json
import os
from datetime import datetime
import logging
from config import nifty_50, nifty_bank, nifty_next_50

# Configure logging to write to both file and console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
    handlers=[logging.FileHandler("fetch_data.log"), logging.StreamHandler(sys.stdout)],
)


def fetch_and_save_stock_data(symbol):
    try:
        nse_live = NSELive()
        stock_quote = nse_live.stock_quote(symbol)

        if stock_quote:
            # Extract lastUpdateTime and parse it to datetime object
            last_update_time_str = stock_quote["metadata"]["lastUpdateTime"]
            last_update_time = datetime.strptime(
                last_update_time_str, "%d-%b-%Y %H:%M:%S"
            )
            year = last_update_time.strftime("%Y")
            month = last_update_time.strftime("%m")

            # Adjusted Directory path: data/year/month
            data_directory = os.path.join("data", symbol, year, month)
            os.makedirs(data_directory, exist_ok=True)

            filename = os.path.join(
                data_directory, f"{symbol}_{last_update_time.strftime('%Y-%m-%d')}.json"
            )

            if os.path.exists(filename):
                logging.info(
                    f"Data file {filename} already exists. Skipping fetch for {symbol}."
                )
                return

            with open(filename, "w") as file:
                json.dump(stock_quote, file, indent=4)
            logging.info(f"Data for {symbol} saved to {filename}")
        else:
            logging.error(
                f"No data returned for {symbol}. Check if the symbol is correct or API issues."
            )
    except Exception as e:
        logging.error(f"Error fetching data for {symbol}: {e}")


if __name__ == "__main__":
    symbols = nifty_50 + nifty_bank + nifty_next_50
    for symbol in symbols:
        fetch_and_save_stock_data(symbol)
