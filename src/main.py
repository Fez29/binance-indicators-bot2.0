from concurrent.futures import ThreadPoolExecutor
from binance_client import client
from indicatorHelper import get_data, get_stop_loss_factor_based_on_atr_value_for_symbol, execute_indicator_functions_as_list
from databaseHelper import create_all_tables, insert_binance_trading, get_active_trading_pairs, insert_indicators, insert_strategy, insert_strategy_indicators, get_indicator_names_per_strategy, get_active_strategies_id, get_quote_currency_by_symbol
from requestHelper import buyOrderRequest
from data import symbol_data, indicator_list, strategy_list, strategy_indicators
from shared import logger, url, interval, database_name, period, indicator_window, target_profit, buy_currency, buy_amount, delay
import asyncio
from priceWebSocketHelper import price_websocket_thread, price_updates
import time
from icecream import ic
ic.configureOutput(includeContext=True)

trading_active = True
use_ic_debugging = False
track_price_updates = False
measure_loop_execution_time = False

def debug(*args):
    if use_ic_debugging:
        ic(" ".join(map(str, args)))

async def main():
    try:
        global trading_active
        global use_ic_debugging
        create_all_tables(database_name)
        insert_binance_trading(database_name, symbol_data)
        insert_indicators(database_name, indicator_list)
        insert_strategy(database_name, strategy_list)
        insert_strategy_indicators(database_name, strategy_indicators)
        active_trading_pairs = get_active_trading_pairs(database_name)

        # get_indicator_names_per_strategy(database_name, id)
        trading_symbols = active_trading_pairs
        # Start the new websocket thread
        price_websocket_thread.start()

        def process_symbol(symbol):
            df = get_data(client, symbol, interval, period, indicator_window)
            stop_loss_factor = get_stop_loss_factor_based_on_atr_value_for_symbol(df)
            buy_signals, indicators = execute_indicator_functions_as_list(indicator_names, df)
            # Bool condition used to eliminate empty lists
            if bool(buy_signals) == True and bool(indicators) == True:
                return stop_loss_factor, indicators, buy_signals
            else:
                logger.info(f"Empty list found: buy_signals = {buy_signals}, indicators = {indicators}")
                return False, stop_loss_factor, indicators

        while True:
            if measure_loop_execution_time == True:
                start_time = time.time()
            active_strategy_ids = get_active_strategies_id(database_name)
            for id in active_strategy_ids:
                indicator_names = get_indicator_names_per_strategy(database_name, id)
                
                with ThreadPoolExecutor(max_workers=8) as executor:
                    futures = [(executor.submit(process_symbol, symbol), symbol) for symbol in trading_symbols]
                    
                    for future, symbol in futures:
                        try:
                            stop_loss_factor, indicators, buy_signals = future.result()
                        except Exception as e:
                            debug("An error occurred:", e)
                            logger.error(f"An error occurred: {e}")
                            raise Exception(f"An error occurred: {e}")
                        
                        count_true = buy_signals.count(True) == len(indicators)

                        if count_true and trading_active:
                            buy_order = await buyOrderRequest(symbol, stop_loss_factor, target_profit, buy_currency, buy_amount, url, str(indicators))
                            debug("BuyOrderId:", buy_order)
                            logger.info(f"BuyOrderId: {buy_order}")

                        else:
                            debug("No buy signal at this time for:", symbol, "and indicators", indicator_names)
                            logger.info(f"No buy signal at this time for: {symbol}")
                        debug("Processed symbol", symbol)
                        logger.info(f"Processed symbol: {symbol}")
            if measure_loop_execution_time == True:
                end_time = time.time()
                execution_time = end_time - start_time
                ic(execution_time)
            time.sleep(delay)
    except Exception as e:
        debug("An error occurred:", e)
        logger.error(f"An error occurred: {e}")
        raise Exception(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
