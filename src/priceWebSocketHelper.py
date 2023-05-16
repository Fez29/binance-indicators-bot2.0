import asyncio
import json
import websockets
import threading
from databaseHelper import get_active_trading_pairs
from shared import database_name, logger
from icecream import ic
import inspect

price_updates = {}


async def binance_price_websocket(symbol: str):
    binance_websocket_url = f"wss://stream.binance.com:9443/ws/{symbol.lower()}@trade"

    async with websockets.connect(binance_websocket_url) as websocket:
        while True:
            try:
                message = await websocket.recv()
                data = json.loads(message)
                # Update the price for this symbol in the price_updates dictionary
                price_updates[symbol.upper()] = data['p']
            except Exception as e:
                print(f"An error occurred: {e}")
                logger.error(f"An error occurred: {e}")
                raise Exception(f"An error occurred: {e}")


async def monitor_multiple_symbols(symbols: list):
    try:
        tasks = [binance_price_websocket(symbol) for symbol in symbols]
        await asyncio.gather(*tasks)
    except Exception as e:
        print(f"An error occurred: {e}")
        logger.error(f"An error occurred: {e}")
        raise Exception(f"An error occurred: {e}")


def run_websockets():
    try:
        symbols = get_active_trading_pairs(database_name)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(monitor_multiple_symbols(symbols))
    except Exception as e:
        print(f"An error occurred: {e}")
        logger.error(f"An error occurred: {e}")
        raise Exception(f"An error occurred: {e}")


price_websocket_thread = threading.Thread(target=run_websockets)

async def get_price_for_symbol(symbol):
    try:
        if symbol in price_updates:
            current_price = price_updates[symbol]
            logger.info(f"{symbol} = {current_price}")
        else:
            ic("Failed to get latest price for:", symbol)
        return current_price
    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        logger.error(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(
            f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")