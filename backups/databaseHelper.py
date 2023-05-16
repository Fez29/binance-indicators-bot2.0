import mysql.connector
from shared import logger, host

# Function to establish a connection with the MySQL database


def create_database_connection(database_name):
    try:
        connection = mysql.connector.connect(
            host=host,
            user="root",
            password="123456",
            database=database_name
        )
        return connection
    except Exception as e:
        logger.error(f"create_database_connection Error: {e}")

# Function to insert data into the database


def create_binance_trading_table(database_name, trading_table_name):
    try:
        connection = create_database_connection(database_name)
        logger.info("Connected to database successfully.")

        # Check if the binance_trading table exists
        cursor = connection.cursor()

        # Create the binance_trading table if it doesn't exist
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {trading_table_name} (
                id INT PRIMARY KEY AUTO_INCREMENT,
                base_currency VARCHAR(50) NOT NULL,
                base_currency_symbol VARCHAR(10) NOT NULL,
                quote_currency VARCHAR(10) NOT NULL,
                quote_currency_symbol VARCHAR(10) NOT NULL,
                trading_pair VARCHAR(10) NOT NULL UNIQUE,
                active BOOLEAN NOT NULL 
            );
        """)
        connection.commit()
        logger.info("binance_trading table created successfully.")

        cursor.close()
        connection.close()
    except Exception as e:
        logger.error(f"create_binance_trading_table Error: {e}")


def insert_binance_trading(database_name, trading_table_name, symbol_data):
    try:
        connection = create_database_connection(database_name)

        data = symbol_data

        # Check if each trading pair already exists in the table
        cursor = connection.cursor()
        for pair in data:
            cursor.execute(f"""
                SELECT COUNT(*) FROM {trading_table_name} WHERE
                base_currency=%s AND base_currency_symbol=%s AND
                quote_currency=%s AND quote_currency_symbol=%s AND
                trading_pair=%s;
            """, pair[1:])
            result = cursor.fetchone()

            # Insert the trading pair if it doesn't already exist
            if result[0] == 0:
                cursor.execute(f"""
                    INSERT INTO {trading_table_name} (base_currency, base_currency_symbol, quote_currency, quote_currency_symbol, trading_pair, active)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """, pair)
                connection.commit()
                logger.info(
                    f"Inserted trading pair {pair[1:]} into binance_trading table.")

            else:
                logger.info(
                    f"Trading pair {pair[1:]} already exists in binance_trading table.")

        cursor.close()
        connection.close()
    except Exception as e:
        logger.error(f"insert_binance_trading Error: {e}")


def get_active_trading_pairs(database_name):
    try:
        connection = create_database_connection(database_name)
        cursor = connection.cursor()

        cursor.execute("""SELECT trading_pair FROM binance_trading WHERE active='1';
        """)
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        trading_pairs = [pair[0] for pair in result]
        return trading_pairs
    except Exception as e:
        logger.error(f"get_active_trading_pairs Error: {e}")

    return


# Record results of inidcator checks in database
# Create table

def create_ema_sma_rsi_stoch_indicator_results_table(database_name, table_name):
    try:
        connection = create_database_connection(database_name)
        cursor = connection.cursor()

        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INT PRIMARY KEY AUTO_INCREMENT,
                timestamp TIMESTAMP NOT NULL,
                symbol VARCHAR(10) NOT NULL,
                ema DECIMAL(18, 8) NOT NULL,
                sma DECIMAL(18, 8) NOT NULL,
                rsi DECIMAL(18, 8) NOT NULL,
                percent_k DECIMAL(18, 8) NOT NULL,
                percent_d DECIMAL(18, 8) NOT NULL,
                ema_greater_sma BOOLEAN NOT NULL,
                rsi_less_than_30 BOOLEAN NOT NULL,
                percent_k_greater_d BOOLEAN NOT NULL
            );
        """)
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        logger.error(f"create_indicator_results_table Error: {e}")


# Insert function


def insert_indicator_result(database_name, table_name, symbol, ema, sma, rsi, percent_k, percent_d, ema_greater_sma, rsi_less_than_30, percent_k_greater_d):
    try:
        connection = create_database_connection(database_name)
        cursor = connection.cursor()

        cursor.execute(f"""
            INSERT INTO {table_name} (timestamp, symbol, ema, sma, rsi, percent_k, percent_d, ema_greater_sma, rsi_less_than_30, percent_k_greater_d)
            VALUES (NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, (symbol, ema, sma, rsi, percent_k, percent_d, ema_greater_sma, rsi_less_than_30, percent_k_greater_d))

        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        logger.error(f"insert_indicator_result Error: {e}")
