from binance_client import client
from indicatorHelper import get_data, get_stop_loss_factor_based_on_atr_value_for_symbol, execute_indicator_functions_as_list
from databaseHelper import create_all_tables, insert_binance_trading, get_active_trading_pairs, insert_indicators, insert_strategy, insert_strategy_indicators, get_indicator_names_per_strategy, get_active_strategies_id
from requestHelper import buyOrderRequest
from data import symbol_data, indicator_list, strategy_list, strategy_indicators
from shared import logger, url, interval, database_name, period, indicator_window, target_profit, buy_currency, buy_amount, delay
import asyncio
from priceWebSocketHelper import price_websocket_thread, price_updates
import time
from icecream import ic, install
ic.configureOutput(includeContext=True)
install()

trading_active = True
use_ic_debugging = False
track_price_updates = False

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
        while True:
            time.sleep(delay)
            start_time = time.time()
            active_strategy_ids = get_active_strategies_id(database_name)
            for id in active_strategy_ids:
                indicator_names = get_indicator_names_per_strategy(
                    database_name, id)
                for symbol in trading_symbols:
                    df = None

                    df = get_data(client, symbol, interval,
                                  period, indicator_window)

                    if track_price_updates == True:
                        if symbol in price_updates:
                            current_price = price_updates[symbol]
                            if use_ic_debugging == True:
                                ic(symbol, current_price)
                            logger.info(f"{symbol} = {current_price}")
                        else:
                            ic("Failed to get latest price for:", symbol)
                    # calculate Stop loss based on ATR
                    stop_loss_factor = get_stop_loss_factor_based_on_atr_value_for_symbol(
                        df)

                    buy_signals, indicators = execute_indicator_functions_as_list(
                        indicator_names, df)
                    count_true = buy_signals.count(
                        True) == len(indicator_names)

                    if count_true == True and trading_active == True:
                        buy_order = await buyOrderRequest(symbol, stop_loss_factor, target_profit, buy_currency, buy_amount, url, str(indicators))
                        if use_ic_debugging == True:
                            ic("BuyOrderId:", buy_order)
                        logger.info(f"BuyOrderId:", buy_order)

                    else:
                        if use_ic_debugging == True:
                            ic("No buy signal at this time for:",
                               symbol, "and indicators", indicator_names)
                        logger.info("No buy signal at this time for:", symbol)
            end_time = time.time()
            execution_time = end_time - start_time
            ic(execution_time)
    except Exception as e:
        if use_ic_debugging == True:
            ic("An error occurred:", e)
        logger.error(f"An error occurred: {e}")
        raise Exception(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())

# current_price = client.get_symbol_ticker(symbol=trading_symbol)
# print(current_price)
