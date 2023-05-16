import logging
import os
from logging.handlers import RotatingFileHandler
from binance_client import client

# Database

host = "192.168.222.128"
password = "123456"
user = "root"
port = 3306
database_name = "db_binance"

# Quick setup for congiguration, see bottom of file.
configuration = "1MINUTEINTERVALS"

# Indicator Parameters

# # Interval: Defines the time frame of the data (e.g., 1-hour candlesticks).
# # Affects the granularity of the analysis and depends on your trading style.
# interval = client.KLINE_INTERVAL_1MINUTE

# # Period: Specifies the duration of historical data (e.g., past 2 months).
# # More data provides a better understanding of the market but requires more computational resources.
# period = "2 days ago UTC"

# Target profit and stop loss: Define the desired profit and maximum acceptable loss for each trade.
target_profit = 1.04

# Buy currency and amount: Define the currency and the amount used for each trade.
buy_currency = "USDT"
buy_amount = "20"

# Indicator window: Defines the lookback window for calculating the technical indicators (e.g., past 14 periods).
# Affects the sensitivity of the indicators to price changes and depends on the specific indicator and trading strategy.
# indicator_window = 14

# Defines the period to be used to lookback into in indicators
lookback_period = 3

# RSI threshold to indicate oversold
rsi_threshold = 35

# Write historical indicator data to csv in get_data function
write_to_csv = False

# Request URL
url = "http://192.168.222.128:8000/process_trade"
# url = "http://localhost:8000/process_trade"

log_folder = "./logs"
log_file_name = os.path.join(log_folder, "binance_bot.log")

# Check if the logs folder exists, and create it if it doesn't
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler = RotatingFileHandler(
    log_file_name, maxBytes=5 * 1024 * 1024, backupCount=5)
log_handler.setFormatter(log_formatter)

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logger.addHandler(log_handler)

# Pre-Configured parameters

if configuration == "1MINUTEINTERVALS":
    interval = client.KLINE_INTERVAL_1MINUTE
    period = "1 day ago UTC"
    delay = 30
    indicator_window = 14
elif configuration == "3MINUTEINTERVALS":
    interval = client.KLINE_INTERVAL_3MINUTE
    period = "2 days ago UTC"
    delay = 150
    indicator_window = 14
elif configuration == "5MINUTEINTERVALS":
    interval = client.KLINE_INTERVAL_5MINUTE
    period = "2 days ago UTC"
    delay = 200
    indicator_window = 14
elif configuration == "15MINUTEINTERVALS":
    interval = client.KLINE_INTERVAL_15MINUTE
    # period = "1 week ago UTC"
    period = "2 weeks ago UTC"
    delay = 800
    indicator_window = 14
elif configuration == "30MINUTEINTERVALS":
    interval = client.KLINE_INTERVAL_30MINUTE
    period = "2 weeks ago UTC"
    delay = 1700
    indicator_window = 14
elif configuration == "1HOURINTERVALS":
    interval = client.KLINE_INTERVAL_1HOUR
    # period = "1 month ago UTC"
    period = "1 year ago UTC"
    delay = 600
    indicator_window = 14