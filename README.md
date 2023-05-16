## SQL Queries
### Sample for updating Symbols to inactive
```
update binance_trading set active = 0 where id in (10);
```
### Drop all Related tables including tables for order-bot:
```
Drop table binance_trading, created_orders,indicator_results, indicator_results_ema_sma_rsi_stoch,indicator_results_macd_bb,indicator_results_rsi_macd,indicator_signals_usdt,orders;
```