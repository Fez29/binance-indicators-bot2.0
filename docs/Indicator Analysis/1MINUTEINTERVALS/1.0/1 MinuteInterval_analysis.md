# 1 Minute interval

Disclaimer: Bug found it code which could possibly have impacted the orders placed.

```
+----+---------------------+---------+---------+-------------+---------+-----------+--------------+---------------------------------+
+----+---------------------+---------+---------+-------------+---------+-----------+--------------+---------------------------------+
| Id | TimeStamp           | Symbol  | OrderId | OrderAmount | Price   | SellPrice | ProfitOrLoss | Indicator                       |
+----+---------------------+---------+---------+-------------+---------+-----------+--------------+---------------------------------+
|  1 | 2023-05-14 11:53:22 | BTCUSDT | 4965294 |    0.000746 | 26796.9 |     26529 |    -0.199883 | ['rsi', 'bb']                   |
|  2 | 2023-05-14 12:02:09 | LTCBNB  | 176831  |     77.1903 |  0.2592 |    0.2695 |      0.79506 | ['50ema_200ema_cross']          |
|  3 | 2023-05-14 12:02:38 | BTCUSDT | 4967801 |    0.000746 | 26785.2 |   26517.3 |    -0.199816 | ['bb', 'supertrend']            |
|  4 | 2023-05-14 12:03:37 | BTCUSDT | 4968069 |    0.000746 | 26781.7 |   26513.9 |    -0.199786 | ['rsi', 'bb']                   |
|  5 | 2023-05-14 12:17:10 | ETHUSDT | 4380171 |     0.01111 | 1798.52 |   1780.53 |    -0.199869 | ['rsi', 'bb']                   |
|  6 | 2023-05-14 12:17:21 | XRPUSDT | 753767  |          47 |  0.4256 |    0.4213 |      -0.2021 | ['rsi', 'bb']                   |
|  7 | 2023-05-14 12:17:43 | ETHUSDT | 4380357 |     0.01111 | 1799.32 |   1781.32 |     -0.19998 | ['rsi', 'indicator_macd_cross'] |
|  8 | 2023-05-14 12:18:32 | XRPUSDT | 753783  |        46.9 |  0.4256 |    0.4213 |     -0.20167 | ['indicator_macd_cross', 'rsi'] |
|  9 | 2023-05-14 12:20:23 | XRPUSDT | 753814  |        46.9 |  0.4256 |    0.4213 |     -0.20167 | ['rsi', 'indicator_macd_cross'] |
| 10 | 2023-05-14 12:27:07 | ETHUSDT | 4382979 |     0.01112 | 1798.62 |   1780.63 |    -0.200049 | ['rsi', 'indicator_macd_cross'] |
| 11 | 2023-05-14 12:39:06 | LTCBNB  | 177124  |     77.2499 |  0.2596 |    0.2699 |     0.795674 | ['50ema_200ema_cross']          |
| 12 | 2023-05-14 12:43:28 | LTCUSDT | 1224925 |     0.24639 |   81.18 |     84.42 |     0.798304 | ['50ema_200ema_cross']          |
| 13 | 2023-05-14 12:48:25 | TRXUSDT | 398326  |         288 | 0.06944 |   0.06874 |      -0.2016 | ['50ema_200ema_cross']          |
| 14 | 2023-05-14 12:56:10 | TRXUSDT | 398436  |       288.1 | 0.06934 |   0.06864 |     -0.20167 | ['bb', 'supertrend']            |
| 15 | 2023-05-14 13:12:19 | BNBUSDT | 949843  |        0.06 |  312.09 |    308.96 |      -0.1878 | ['50ema_200ema_cross']          |
| 16 | 2023-05-14 13:15:26 | BNBUSDT | 949971  |        0.06 |     312 |    308.87 |      -0.1878 | ['bb', 'supertrend']            |
| 17 | 2023-05-14 13:22:58 | LTCBNB  | 178033  |     76.1905 |  0.2618 |    0.2722 |     0.792381 | ['bb', 'supertrend']            |
| 18 | 2023-05-14 13:38:33 | TRXUSDT | 399124  |         289 | 0.06921 |   0.06851 |      -0.2023 | ['rsi', 'bb']                   |
| 19 | 2023-05-14 14:13:52 | BNBUSDT | 952695  |        0.06 |     312 |    308.87 |      -0.1878 | ['bb', 'supertrend']            |
| 20 | 2023-05-14 16:56:57 | ETHUSDT | 4452533 |     0.01105 | 1809.25 |   1791.15 |    -0.200005 | ['rsi', 'bb']                   |
| 21 | 2023-05-14 16:57:11 | BTCUSDT | 5052275 |    0.000741 | 26974.8 |   26705.1 |    -0.199863 | ['indicator_macd_cross', 'rsi'] |
| 22 | 2023-05-14 16:57:21 | BTCUSDT | 5052361 |    0.000741 | 26976.2 |   26706.4 |    -0.199892 | ['bb', 'supertrend']            |
| 23 | 2023-05-14 16:58:09 | BTCUSDT | 5052656 |    0.000741 | 26949.9 |   26680.4 |      -0.1997 | ['rsi', 'indicator_macd_cross'] |
| 24 | 2023-05-14 16:59:43 | LTCUSDT | 1249997 |     0.24172 |   82.74 |     86.04 |     0.797676 | ['bb', 'supertrend']            |
| 25 | 2023-05-14 17:00:35 | LTCUSDT | 1250121 |     0.24201 |   82.66 |     85.96 |     0.798633 | ['rsi', 'indicator_macd_cross'] |
| 26 | 2023-05-14 17:01:42 | ETHUSDT | 4453999 |     0.01108 | 1803.99 |   1785.95 |    -0.199883 | ['rsi', 'bb']                   |
| 27 | 2023-05-14 17:02:01 | ETHUSDT | 4454131 |     0.01107 | 1805.43 |   1787.37 |    -0.199924 | ['bb', 'supertrend']            |
| 28 | 2023-05-14 17:03:03 | ETHUSDT | 4454424 |     0.01108 | 1804.71 |   1786.66 |    -0.199994 | ['indicator_macd_cross', 'rsi'] |
| 29 | 2023-05-14 17:11:38 | ETHUSDT | 4456697 |     0.01107 | 1805.35 |   1787.29 |    -0.199924 | ['rsi', 'indicator_macd_cross']

```
# Data

```
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
]

strategy_list = [
    ("ema_rsi",1,"Uses the ema 50 cross above 200 line and rsi to confirm in undersold"),
    ("ema_rsi_rsibreakout",1,"Uses the ema 50 cross above 200 line and rsi to confirm in undersold plus rsi breakout"),
    ("bb_rsi",1,"Uses closing price below lower bb line and rsi indicating undersold"),
    ("macdcross_rsi",1,"Uses macd line cross over macd signal line and rsi is oversold"),
    ("ema",1,"EMA50 and EMA 200 cross as buy signal"),
    ("macd_cross_rsi",1,"Check for MACD cross and use RSI to confirm"),
    ("bb_supertrend",1,"Check for bollinger band trigger and use supertrend to confirm trend"),
]

strategy_indicators = [
    (1,1),
    (1,3),
    (2,1),
    (2,3),
    (2,10),
    (3,3),
    (3,8),
    (4,3),
    (4,6),
    (5,1),
    (6,6),
    (6,3),
    (7,8),
    (7,12),
]
```
## Config
```
if configuration == "1MINUTEINTERVALS":
    interval = client.KLINE_INTERVAL_1MINUTE
    period = "1 day ago UTC"
    delay = 30
    indicator_window = 14

# Defines the period to be used to lookback into in indicators
lookback_period = 3

# RSI threshold to indicate oversold
rsi_threshold = 35

Success Rate = 20%
Profit = 0.20475%
