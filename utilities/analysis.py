import sys
sys.path.append("../")

from analysisHelper import analyze_indicator_results
from main import database_name, indicator_results_table, logger
from databaseHelper import get_active_trading_pairs
import asyncio


async def analysis_function():
    try:
        active_trading_pairs = get_active_trading_pairs(database_name)
        trading_symbols = active_trading_pairs
        for symbol in trading_symbols:
            condition_percentages = analyze_indicator_results(database_name, indicator_results_table, symbol)

            for condition, percentage in condition_percentages.items():
                print(f"Analysis for {symbol}: {condition}: {percentage:.2f}%")
    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(analysis_function())