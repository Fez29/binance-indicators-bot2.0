## Currently Working on: 

If you're using RSI breakout and RSI divergence together, it's a good idea to add a trend-following indicator to your trading strategy. This can help confirm the overall trend direction and provide additional confirmation for your RSI-based signals. One popular trend-following indicator that works well with RSI-based strategies is the Moving Average Convergence Divergence (MACD).

- The MACD indicator consists of two lines: the MACD line and the signal line. The MACD line is the difference between two exponential moving averages (EMAs), typically the 12-period EMA and the 26-period EMA. The signal line is an EMA (usually 9-period) of the MACD line. The MACD indicator also includes a histogram, which represents the difference between the MACD line and the signal line.

- Here are some ways you can use the MACD indicator in conjunction with RSI breakout and RSI divergence signals:

    - MACD crossover: A bullish signal occurs when the MACD line crosses above the signal line, indicating that the shorter-term momentum is stronger than the longer-term momentum. Similarly, a bearish signal occurs when the MACD line crosses below the signal line. You can use these crossovers to confirm RSI breakout or divergence signals.

    - ***MACD divergence: Like RSI, the MACD indicator can also exhibit divergence with price. Bullish divergence occurs when the price makes a lower low, but the MACD makes a higher low, signaling a potential trend reversal. Bearish divergence occurs when the price makes a higher high, but the MACD makes a lower high. You can use MACD divergences as additional confirmation for RSI-based signals.***

    - MACD histogram: The MACD histogram can help you gauge the strength of the trend. When the histogram is above the zero line and increasing, it indicates a strengthening bullish trend. When the histogram is below the zero line and decreasing, it suggests a strengthening bearish trend. You can use the MACD histogram to confirm the strength of the trend when considering RSI breakout or divergence signals.

- Remember, it's important to use proper risk management and diversify your strategies to minimize the impact of false signals. Test your trading strategy using historical data and adjust your approach based on the results.



# RSI

### Aspects:
- RSI Breakout
    - Considered:
        - a new row in the rsi_breakout column will be marked as True if the RSI is above its previous resistance level or if the RSI is above 70.
        - This code adds a confirmation period and volume confirmation to your RSI breakout detection. It uses a rolling window to confirm that the RSI has stayed above the resistance level for the confirmation period, and checks that the volume during the potential breakout is significantly higher than the average volume.
```
df['rsi_breakout'] = ((df['RSI'] > df['RSI_resistance'].shift(1)) & (df['RSI'].shift(1) <= df['RSI_resistance'].shift(1))) | (df['RSI'] > 70)
```


# Important Features:
remove hardcoding of buy_ccurrency value and get details from "binance_trading" table where it is currently under the "quote_currency_symbol" column for the related symbol. 



# Additional features:

- Add config tables so values can be reoved from application.
```
config_table
- target_profit
- buy_amount
- url

indicator_config_table
- rsi_threshold
- configuration_value
- lookback_period
- strategy_id (foreign_key linking to strategy table)
```