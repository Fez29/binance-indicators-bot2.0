from databaseHelper import create_database_connection
from main import logger

def analyze_indicator_results(database_name, table_name, symbol):
    try:
        connection = create_database_connection(database_name)
        cursor = connection.cursor()

        # Get the total number of rows for the trading pair
        cursor.execute(f"""
            SELECT COUNT(*) FROM {table_name} WHERE symbol=%s;
        """, (symbol,))
        total_rows = cursor.fetchone()[0]

        # Calculate the percentage of times each condition is met
        condition_columns = ["ema_greater_sma", "rsi_less_than_30", "percent_k_greater_d"]
        condition_percentages = {}

        for column in condition_columns:
            cursor.execute(f"""
                SELECT COUNT(*) FROM {table_name} WHERE symbol=%s AND {column}=1;
            """, (symbol,))
            count = cursor.fetchone()[0]
            percentage = (count / total_rows) * 100
            condition_percentages[column] = percentage

        cursor.close()
        connection.close()

        return condition_percentages
    except Exception as e:
        logger.error(f"analyze_indicator_results Error: {e}")

    return None
