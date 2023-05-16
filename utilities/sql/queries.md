# Check for buy signal:
```
select * from indicator_results where ema_greater_sma = 1 AND rsi_less_than_30 AND percent_k_greater_d = 1;
```

