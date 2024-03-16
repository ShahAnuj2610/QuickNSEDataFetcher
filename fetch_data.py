from jugaad_data.nse import NSELive
import json
import os
from datetime import datetime
import logging

from config import nifty_50, nifty_bank, nifty_next_50

# Configure logging
logging.basicConfig(
    filename="fetch_data.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def fetch_and_save_stock_data(symbol):
    # Ensure 'data' directory exists
    data_directory = "data"
    os.makedirs(data_directory, exist_ok=True)

    # Filename for the current day's data
    filename = os.path.join(
        data_directory, f"{symbol}_{datetime.now().strftime('%Y-%m-%d')}.json"
    )

    # Check if today's data file already exists
    if os.path.exists(filename):
        logging.info(
            f"Data file {filename} already exists. Skipping fetch for {symbol}."
        )
        return

    try:
        nse_live = NSELive()
        stock_quote = nse_live.stock_quote(symbol)

        # Check if API call returned data successfully
        if stock_quote:
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
    for symbol in nifty_50 + nifty_bank + nifty_next_50:
        fetch_and_save_stock_data(symbol)
