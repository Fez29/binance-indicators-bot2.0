symbol_data = [
    ('Binance Coin', 'BNB', 'Tether', 'USDT', 'BNBUSDT', 1),
    ('Bitcoin', 'BTC', 'Tether', 'USDT', 'BTCUSDT', 1),
    ('Ethereum', 'ETH', 'Tether', 'USDT', 'ETHUSDT', 1),
    ('Litecoin', 'LTC', 'Tether', 'USDT', 'LTCUSDT', 1),
    ('Tron', 'TRX', 'Tether', 'USDT', 'TRXUSDT', 1),
    ('Ripple', 'XRP', 'Tether', 'USDT', 'XRPUSDT', 1),
    ('Binance Coin', 'BNB', 'Bitcoin', 'BTC', 'BNBBTC', 1),
    ('Ethereum', 'ETH', 'Bitcoin', 'BTC', 'ETHBTC', 1),
    ('Litecoin', 'LTC', 'Bitcoin', 'BTC', 'LTCBTC', 1),
    ('Tron', 'TRX', 'Bitcoin', 'BTC', 'TRXBTC', 1),
    ('Ripple', 'XRP', 'Bitcoin', 'BTC', 'XRPBTC', 1),
    ('Litecoin', 'LTC', 'Binance Coin', 'BNB', 'LTCBNB', 1),
    ('Tron', 'TRX', 'Binance Coin', 'BNB', 'TRXBNB', 1),
    ('Ripple', 'XRP', 'Binance Coin', 'BNB', 'XRPBNB', 1),
]

indicator_list = [
    ("ema_50_200_cross","ema_50_200_cross indicator"),
    ("ema_sma_cross","ema_sma_cross indicator"),
    ("rsi","rsi indicator"),
    ("stoch","stoch indicator"),
    ("volume","volume indicator"),
    ("macd_cross","macd_cross"),
    ("macd_cross_above_zero","macd_cross_above_zero indicator"),
    ("bolingerbands","bolingerbands indicator"),
    ("rsi_divergence","rsi_divergence indicator"),
    ("rsi_divergence_v2","rsi_divergence_v2 indicator"),
    ("rsi_breakout","rsi_breakout indicator"),
    ("supertrend","supertrend indicator"),
    ("bollingerbands_zones", "bollingerbands_zones indicator")
]

strategy_list = [
    ("ema_rsi",1,"Uses the ema 50 cross above 200 line and rsi to confirm in undersold"),
    ("ema_rsi_rsibreakout",1,"Uses the ema 50 cross above 200 line and rsi to confirm in undersold plus rsi breakout"),
    ("bb_rsi_supertrend",1,"Uses closing price below lower bb line and rsi indicating undersold as well as supertrend to confirm trend"),
    ("macdcross_rsi",1,"Uses macd line cross over macd signal line and rsi is oversold"),
    ("ema",1,"EMA50 and EMA 200 cross as buy signal"),
    ("macd_cross_rsi",1,"Check for MACD cross and use RSI to confirm"),
    ("bb_supertrend",1,"Check for bollinger band trigger and use supertrend to confirm trend"),
    ("bbb_supertrend",1,"Check for bollinger band trigger and use supertrend to confirm trend"),
]

strategy_indicators = [
    (1,1),
    (1,3),
    (2,1),
    (2,3),
    (2,10),
    (3,3),
    (3,8),
    (3,13),
    (4,3),
    (4,6),
    (5,1),
    (6,6),
    (6,3),
    (7,8),
    (7,12),
    (8,12),
    (8,13),
]