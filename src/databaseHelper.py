from shared import logger, user, password, host, port
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from databaseClassHelper import Base, TradingPair, Indicator, Strategy, StrategyIndicator
import _mysql_connector
import inspect

# Function to establish a connection with the MySQL database


def create_database_session(database_name):
    try:
        # Replace the placeholders with your actual database credentials
        DATABASE_URL = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database_name}'
        engine = create_engine(DATABASE_URL)
        Session = sessionmaker(bind=engine, expire_on_commit=True)
        session = Session()
        return session
    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(
            f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")


# Record results of inidcator checks in database
# Create all tables


def create_all_tables(database_name):
    try:
        session = create_database_session(database_name)
        Base.metadata.create_all(bind=session.get_bind())
        session.commit()
        return
    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(
            f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")
    finally:
        session.close()


# Function to insert trading pair data into the database


def insert_binance_trading(database_name, symbol_data):
    try:
        session = create_database_session(database_name)
        for pair in symbol_data:
            base_currency, base_currency_symbol, quote_currency, quote_currency_symbol, trading_pair, active = pair

            trading_pair_exists = session.query(TradingPair).filter(
                and_(
                    TradingPair.base_currency == base_currency,
                    TradingPair.base_currency_symbol == base_currency_symbol,
                    TradingPair.quote_currency == quote_currency,
                    TradingPair.quote_currency_symbol == quote_currency_symbol,
                    TradingPair.trading_pair == trading_pair
                )
            ).first() is not None

            if not trading_pair_exists:
                new_pair = TradingPair(
                    base_currency=base_currency,
                    base_currency_symbol=base_currency_symbol,
                    quote_currency=quote_currency,
                    quote_currency_symbol=quote_currency_symbol,
                    trading_pair=trading_pair,
                    active=active
                )
                session.add(new_pair)
                session.commit()
                logger.info(
                    f"Inserted trading pair {pair[1:]} into binance_trading table.")
            else:
                logger.info(
                    f"Trading pair {pair[1:]} already exists in binance_trading table.")
        return
    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(
            f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")
    finally:
        session.close()


# Insert data into database for indicators

def insert_indicators(database_name, indicator_list):
    try:
        session = create_database_session(database_name)
        for pair in indicator_list:
            name, description = pair

            trading_pair_exists = session.query(Indicator).filter(
                and_(
                    Indicator.name == name,
                    Indicator.description == description
                )
            ).first() is not None

            if not trading_pair_exists:
                new_pair = Indicator(
                    name=name,
                    description=description
                )
                session.add(new_pair)
                session.commit()
                logger.info(
                    f"Inserted indicator {pair[1:]} into indicators table.")
            else:
                logger.info(
                    f"Indicator already exists in indicators table.")
        return
    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(
            f"{inspect.currentframe().f_code.co_name} An error occurred instering to indicators table: {e}")
    finally:
        session.close()

# Insert data into database for strategy


def insert_strategy(database_name, strategy_list):
    try:
        session = create_database_session(database_name)
        for pair in strategy_list:
            name, active, description = pair

            trading_pair_exists = session.query(Strategy).filter(
                and_(
                    Strategy.name == name,
                    Strategy.active == active,
                    Strategy.description == description
                )
            ).first() is not None

            if not trading_pair_exists:
                new_pair = Strategy(
                    name=name,
                    active=active,
                    description=description
                )
                session.add(new_pair)
                session.commit()
                logger.info(
                    f"Inserted Strategy {pair[1:]} into strategies table.")
            else:
                logger.info(
                    f"Strategy {pair[1:]} already exists in strategies table.")
        return
    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(
            f"{inspect.currentframe().f_code.co_name} An error occurred instering to strategies table: {e}")
    finally:
        session.close()

# Insert data into database for indicators linked to strategies


def insert_strategy_indicators(database_name, strategy_indicators):
    try:
        session = create_database_session(database_name)
        for pair in strategy_indicators:
            strategy_id, indicator_id = pair

            trading_pair_exists = session.query(StrategyIndicator).filter(
                and_(
                    StrategyIndicator.strategy_id == strategy_id,
                    StrategyIndicator.indicator_id == indicator_id
                )
            ).first() is not None

            if not trading_pair_exists:
                new_pair = StrategyIndicator(
                    strategy_id=strategy_id,
                    indicator_id=indicator_id
                )
                session.add(new_pair)
                session.commit()
                logger.info(
                    f"Inserted values {pair[1:]} into strategy_indicators table.")
            else:
                logger.info(
                    f"strategy_indicators {pair[1:]} already exists in strategy_indicators table.")
        return
    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(
            f"{inspect.currentframe().f_code.co_name} An error occurred instering to strategy_indicators table: {e}")
    finally:
        session.close()


def get_active_trading_pairs(database_name):
    try:
        session = create_database_session(database_name)

        active_pairs = session.query(TradingPair.trading_pair).filter(
            TradingPair.active == True).all()

        trading_pairs = [pair[0] for pair in active_pairs]
        return trading_pairs
    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(
            f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")
    finally:
        session.close()


def get_active_strategies_id(database_name):
    try:
        session = create_database_session(database_name)

        active_strategies = session.query(
            Strategy.id).filter(Strategy.active == 1).all()

        return [pair[0] for pair in active_strategies]
    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(
            f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")
    finally:
        session.close()


def get_indicator_names_per_strategy(database_name, id):
    try:
        session = create_database_session(database_name)
        indicators_list = []
        # Retrieve the indicators for strategy ID 1
        strategy = session.query(Strategy).get(id)

        if strategy is not None:
            indicators = strategy.indicators
            for indicator in indicators:
                # print(indicator.indicator.name)
                indicators_list.append(indicator.indicator.name)
            return indicators_list
        else:
            print(f"No strategy found with ID {id}")
    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(
            f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")
    finally:
        session.close()

def get_quote_currency_by_symbol(database_name, symbol):
    try:
        session = create_database_session(database_name)

        quote_currency_symbol = session.query(
            TradingPair.quote_currency_symbol).filter(TradingPair.trading_pair == symbol).first()

        return quote_currency_symbol[0]
    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(
            f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")
    finally:
        session.close()