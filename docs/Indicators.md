# Indicators:

- Simple Moving Average (SMA): The average price over a specified period. It helps to identify trends by smoothing out price fluctuations.

- Exponential Moving Average (EMA): A weighted moving average that gives more importance to recent data. It reacts faster to price changes than the SMA.

- Relative Strength Index (RSI): A momentum oscillator that measures the speed and change of price movements. It ranges from 0 to 100, with values above 70 indicating overbought conditions and values below 30 indicating oversold conditions.

- Moving Average Convergence Divergence (MACD): A trend-following momentum indicator that shows the relationship between two moving averages (usually 12-day and 26-day EMAs). It consists of the MACD line, signal line, and histogram, which can be used to identify potential trend reversals and buy/sell signals.

- Bollinger Bands: A set of three lines plotted around the price, consisting of the SMA (middle band) and two standard deviations above and below the SMA (upper and lower bands). Bollinger Bands are used to measure market volatility and potential overbought/oversold conditions.

- Stochastic Oscillator: A momentum indicator that compares a security's closing price to its price range over a given period. It consists of two lines, %K and %D, which can generate buy/sell signals when they cross each other.

- Fibonacci Retracement: A set of horizontal lines that indicate potential support and resistance levels based on the Fibonacci sequence. Traders use these levels to identify potential price reversals during retracements in a trend.

- Ichimoku Cloud: A comprehensive indicator that provides information about support/resistance levels, trend direction, and momentum. It consists of five lines (Tenkan-sen, Kijun-sen, Senkou Span A, Senkou Span B, and Chikou Span) and a "cloud" formed between Senkou Span A and Senkou Span B.

- Pivot Points: Horizontal lines that indicate potential support and resistance levels based on the previous trading session's high, low, and closing prices. These can be used to set profit targets and stop-loss levels.

- On-Balance Volume (OBV): A cumulative indicator that uses volume and price to measure buying and selling pressure. A rising OBV indicates positive buying pressure, while a falling OBV suggests negative selling pressure.

## Some combinations:

- Moving Averages with RSI or Stochastic Oscillator: A moving average (like the SMA or EMA) can be used to identify the overall trend direction. Then, the RSI or Stochastic Oscillator can be used to identify overbought or oversold conditions within that trend. For example, in an uptrend, you might look for oversold conditions as a potential buying opportunity.

- MACD with Bollinger Bands: The MACD can be used to identify potential buy and sell signals, while Bollinger Bands can provide additional information about the volatility of the market and potential overbought or oversold conditions.

- Fibonacci Retracement with RSI: Fibonacci Retracement levels can provide potential support and resistance levels, while the RSI can provide additional confirmation of these levels. For example, if the price retraces to a Fibonacci level and the RSI also shows oversold conditions, this could be a potential buying opportunity.

- Ichimoku Cloud with Volume: The Ichimoku Cloud can provide a comprehensive view of the market's trend, support and resistance levels, and momentum, while volume indicators like On-Balance Volume (OBV) can provide additional confirmation of these trends.

- Price Action with Volume: Some traders focus primarily on price action (i.e., the study of raw price movements without any additional indicators) and use volume as a secondary indicator to confirm their analysis.


- Intervals:

Client.KLINE_INTERVAL_1MINUTE
Client.KLINE_INTERVAL_3MINUTE
Client.KLINE_INTERVAL_5MINUTE
Client.KLINE_INTERVAL_15MINUTE
Client.KLINE_INTERVAL_30MINUTE
Client.KLINE_INTERVAL_1HOUR
Client.KLINE_INTERVAL_2HOUR
Client.KLINE_INTERVAL_4HOUR
Client.KLINE_INTERVAL_6HOUR
Client.KLINE_INTERVAL_8HOUR
Client.KLINE_INTERVAL_12HOUR
Client.KLINE_INTERVAL_1DAY
Client.KLINE_INTERVAL_3DAY
Client.KLINE_INTERVAL_1WEEK
Client.KLINE_INTERVAL_1MONTH

# Data periods

"1 day ago UTC"
"2 days ago UTC"
"5 days ago UTC"
"1 week ago UTC"
"2 weeks ago UTC"
"1 month ago UTC"
"3 months ago UTC"
"6 months ago UTC"
"1 year ago UTC"



## Results:
### Set 1:
```
before row: 541
interval = client.KLINE_INTERVAL_1MINUTE
period = "3 weeks ago UTC"
```

## Buy Orders triggered:
10
```
+-----+---------------------+---------+---------------+---------------+-------------+-------------+-------------+-----------------+------------------+---------------------+
| id  | timestamp           | symbol  | ema           | sma           | rsi         | percent_k   | percent_d   | ema_greater_sma | rsi_less_than_30 | percent_k_greater_d |
+-----+---------------------+---------+---------------+---------------+-------------+-------------+-------------+-----------------+------------------+---------------------+
| 380 | 2023-05-06 21:04:10 | ADAUSDT |    0.37911362 |    0.37909286 | 35.62909369 | 22.22222222 | 20.74074074 |               1 |                1 |                   1 |
| 384 | 2023-05-06 21:05:36 | ADAUSDT |    0.37906203 |    0.37902143 | 35.49673993 | 12.50000000 | 10.83333333 |               1 |                1 |                   1 |
| 387 | 2023-05-06 21:06:41 | BNBUSDT |  322.66377916 |  322.63571429 | 36.82538854 | 33.33333333 | 16.66666667 |               1 |                1 |                   1 |
| 392 | 2023-05-06 21:08:30 | ADAUSDT |    0.37892565 |    0.37890714 | 33.27796980 | 44.44444444 | 33.60269360 |               1 |                1 |                   1 |
| 396 | 2023-05-06 21:09:55 | ADAUSDT |    0.37892045 |    0.37889286 | 37.61380819 | 55.55555556 | 49.15824916 |               1 |                1 |                   1 |
| 507 | 2023-05-06 21:50:05 | BNBUSDT |  321.98559468 |  321.97857143 | 35.41332172 | 25.00000000 | 20.83333333 |               1 |                1 |                   1 |
| 508 | 2023-05-06 21:50:28 | ADAUSDT |    0.37810335 |    0.37809286 | 35.65878869 | 23.07692308 | 23.07692308 |               1 |                1 |                   1 |
| 510 | 2023-05-06 21:51:10 | ETHUSDT | 1888.21310755 | 1887.91142857 | 38.43241591 | 31.23486683 | 27.88539144 |               1 |                1 |                   1 |
| 511 | 2023-05-06 21:51:32 | BNBUSDT |  321.97418205 |  321.94285714 | 35.41332172 | 28.57142857 | 26.19047619 |               1 |                1 |                   1 |
| 512 | 2023-05-06 21:51:51 | ADAUSDT |    0.37806468 |    0.37804286 | 39.20015533 | 40.00000000 | 21.02564103 |               1 |                1 |                   1 |
+-----+---------------------+---------+---------------+---------------+-------------+-------------+-------------+-----------------+------------------+---------------------+

```
## Set 2
interval = client.Client.KLINE_INTERVAL_1HOUR
period = "3 weeks ago UTC"


## Current Strategy

- Simple Moving Average (SMA): It calculates the average of the closing prices for a specified number of periods.
- Exponential Moving Average (EMA): It calculates a weighted average of the closing prices for a specified number of periods, giving more weight to recent prices.
- Relative Strength Index (RSI): It measures the speed and change of price movements, and is usually used to identify overbought or oversold conditions.
- Stochastic Oscillator (%K and %D): It compares a security's closing price to its price range over a given time period, and consists of two lines, %K and %D, which are used to generate buy and sell signals.




### Buy Signal:

- The EMA is greater than the SMA (indicating an upward trend).
- The RSI is below a certain threshold, e.g., 30 or 40 (indicating the asset is oversold).
- The %K line is above the %D line (indicating a potential price increase).

### Sell Signal:

- The EMA is below the SMA (indicating a downward trend).
- The RSI is above a certain threshold, e.g., 70 or 80 (indicating the asset is overbought).
- The %K line is below the %D line (indicating a potential price decrease).





## Possible good combinations

### RSI (momentum) + Moving Average Crossover (trend) + Bollinger Bands (volatility):

- RSI: Relative Strength Index is a momentum oscillator that measures the speed and change of price movements.
- Moving Average Crossover: A trend-following indicator where you compare two moving averages, such as the short-term (e.g., 50-day) and long-term (e.g., 200-day) moving averages.
- Bollinger Bands: A volatility indicator that consists of a simple moving average (SMA) and two standard deviations above and below the SMA.


- Combination 1:
    - Momentum: Relative Strength Index (RSI)
    - Trend: Moving Average Convergence Divergence (MACD)
    - Volatility: Bollinger Bands (BB)

- Combination 2:
    - Momentum: Stochastic Oscillator (%K and %D) (Implemented)
    - Trend: Simple Moving Average (SMA) Crossover (e.g., 50-day SMA and 200-day SMA) (Implemented)
    - Volatility: Average True Range (ATR) (Implemented partially)

- Combination 3:
    - Momentum: Rate of Change (ROC)
    - Trend: Exponential Moving Average (EMA) Crossover (e.g., 12-day EMA and 26-day EMA)
    - Volatility: Standard Deviation

- Combination 4:
    - Momentum: On Balance Volume (OBV)
    - Trend: Ichimoku Cloud (Tenkan-sen, Kijun-sen, Senkou Span A, Senkou Span B, and Chikou Span)
    - Volatility: Chandelier Exit

- Combination 5:
    - Momentum: Money Flow Index (MFI)
    - Trend: Triple Exponential Moving Average (TEMA)
    - Volatility: Keltner Channels

- Combination 6:
    - Momentum: Williams %R
    - Trend: Parabolic Stop and Reverse (Parabolic SAR)
    - Volatility: Donchian Channels

- Combination 7:
    - Momentum: Ultimate Oscillator
    - Trend: Hull Moving Average (HMA)
    - Volatility: Historical Volatility

- Combination 8:
    - Momentum: TRIX (Triple Exponential Moving Average)
    - Trend: Adaptive Moving Average (AMA)
    - Volatility: Bollinger BandWidth

- Combination 9:
    - Momentum: Commodity Channel Index (CCI)
    - Trend: Double Exponential Moving Average (DEMA)
    - Volatility: Average Directional Index (ADX)

Combination 10:
    - Momentum: Force Index
    - Trend: Guppy Multiple Moving Average (GMMA)
    - Volatility: Chaikin Volatility

Combination 11:
    - Momentum: Know Sure Thing (KST) Oscillator
    - Trend: Moving Average Ribbon
    - Volatility: True Range (TR)

Combination 12:
    - Momentum: Accumulation/Distribution (A/D) Line
    - Trend: Zero Lag Exponential Moving Average (ZLEMA)
    - Volatility: Mass Index

- Combination 13:
    - Momentum: Relative Strength Index (RSI)
    - Trend: Exponential Moving Average (EMA) Crossover (e.g., 12-day EMA and 26-day EMA)
    - Volatility: Keltner Channels

- Combination 14:
    - Momentum: Relative Strength Index (RSI)
    - Trend: Guppy Multiple Moving Average (GMMA)
    - Volatility: Average Directional Index (ADX)

- Combination 15:
    - Momentum: Relative Strength Index (RSI)
    - Trend: Double Exponential Moving Average (DEMA)
    - Volatility: Bollinger BandWidth

- Combination 16:
    - Momentum: Relative Strength Index (RSI)
    - Trend: Hull Moving Average (HMA)
    - Volatility: Chandelier Exit