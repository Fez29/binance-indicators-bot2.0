import pandas as pd
import numpy as np
from shared import logger, lookback_period, rsi_threshold, write_to_csv
import pandas_ta as pta
from decimal import Decimal, ROUND_DOWN
import inspect

# Global variable to store the state of the MACD cross condition
condition_macd_cross = None


class IndicatorFunctions:
    @staticmethod
    def ema_50_200_cross(df):
        try:
            indicator = "50ema_200ema_cross"
            latest_data = df.iloc[-1]
            previous_data = df.iloc[-2]

            current_50ema_200ema_cross = latest_data["EMA_50"] > latest_data["EMA_200"]
            previous_50ema_200ema_cross = previous_data["EMA_50"] <= previous_data["EMA_200"]
            condition_50ema_200ema = current_50ema_200ema_cross and previous_50ema_200ema_cross

            buy_signal = condition_50ema_200ema

            return buy_signal, indicator
        except Exception as e:
            print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            logger.error(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            raise Exception(
                f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")

    @staticmethod    
    def indicator_sma_cross(df):
        try:
            indicator = "bb"
            latest_data = df.iloc[-1]
            previous_data = df.iloc[-2]

            latest_sma_short = latest_data["SMA_short"]
            latest_sma_long = latest_data["SMA_long"]
            previous_sma_short = previous_data["SMA_short"]
            previous_sma_long = previous_data["SMA_long"]

            if latest_sma_short > latest_sma_long and previous_sma_short <= previous_sma_long:
                condition_ma_crossover = True
            elif latest_sma_short < latest_sma_long and previous_sma_short >= previous_sma_long:
                condition_ma_crossover = False

            if condition_ma_crossover == None:
                condition_ma_crossover = False

            buy_signal = condition_ma_crossover

            return buy_signal, indicator
        except Exception as e:
            print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            logger.error(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            raise Exception(
                f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")

    @staticmethod
    def ema_sma_cross(df):
        try:
            indicator = "ema_sma_cross"
            latest_data = df.iloc[-1]
            previous_data = df.iloc[-2]

            current_ema_sma_cross = latest_data["EMA"] > latest_data["SMA"]
            previous_ema_sma_cross = previous_data["EMA"] <= previous_data["SMA"]
            condition_ema_sma = current_ema_sma_cross and previous_ema_sma_cross

            buy_signal = condition_ema_sma

            return buy_signal, indicator
        except Exception as e:
            print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            logger.error(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            raise Exception(
                f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")

    @staticmethod
    def rsi(df):
        try:
            indicator = "rsi"
            condition_rsi = (df.iloc[-1]
                             ["RSI"] < rsi_threshold).all()
            buy_signal = condition_rsi

            return buy_signal, indicator
        except Exception as e:
            print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            logger.error(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            raise Exception(
                f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")

    @staticmethod
    def stoch(df):
        try:
            indicator = "stoch"
            condition_stoch = all(
                df.iloc[-lookback_period:]["%K"] > df.iloc[-lookback_period:]["%D"])
            buy_signal = condition_stoch

            return buy_signal, indicator
        except Exception as e:
            print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            logger.error(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            raise Exception(
                f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")

    @staticmethod
    def volume(df):
        try:
            indicator = "volume"
            latest_data = df.iloc[-1]

            current_volume = latest_data["volume"]
            previous_volumes = df.iloc[-lookback_period:]["volume"]
            condition_volume = (previous_volumes < current_volume).all()

            buy_signal = condition_volume

            return buy_signal, indicator
        except Exception as e:
            print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            logger.error(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            raise Exception(
                f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")

    @staticmethod
    def macd_cross(df):
        global condition_macd_cross  # Indicate that we're using the global variable

        try:
            indicator = "indicator_macd_cross"
            latest_data = df.iloc[-1]
            previous_data = df.iloc[-2]

            # Retrieve the MACD and MACD signal values for the latest and previous data points
            latest_macd = latest_data["macd"]
            latest_macdsignal = latest_data["macdsignal"]
            previous_macd = previous_data["macd"]
            previous_macdsignal = previous_data["macdsignal"]

            # Check for MACD crossover conditions and update the global variable accordingly
            if latest_macd > latest_macdsignal and previous_macd <= previous_macdsignal:
                condition_macd_cross = True
            elif latest_macd < latest_macdsignal and previous_macd >= previous_macdsignal:
                condition_macd_cross = False

            # If the condition_macd_cross variable is not updated, do not generate a buy signal
            if condition_macd_cross == None:
                condition_macd_cross = False

            buy_signal = condition_macd_cross

            return buy_signal, indicator
        except Exception as e:
            print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            logger.error(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            raise Exception(
                f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")

    @staticmethod
    def macd_cross_above_zero(df):
        try:
            indicator = "macd_below_zero"
            latest_data = df.iloc[-1]
            previous_data = df.iloc[-lookback_period:-1]

            # Get MACD and MACD signal values for the latest and previous data
            latest_macd = latest_data["macd"]
            latest_macdsignal = latest_data["macdsignal"]
            previous_macd = previous_data["macd"]
            previous_macdsignal = previous_data["macdsignal"]

            # Check if both MACD and MACD signal are below zero for the previous data
            previous_below_zero = is_below_zero(
                previous_macd) and is_below_zero(previous_macdsignal)
            # Check if both MACD and MACD signal are above zero for the latest data
            latest_above_zero = is_above_zero(
                latest_macd) and is_above_zero(latest_macdsignal)

            # Generate a buy signal if previous data is below zero and latest data is above zero
            buy_signal = previous_below_zero and latest_above_zero

            return buy_signal, indicator
        except Exception as e:
            print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            logger.error(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            raise Exception(
                f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")

    @staticmethod
    def bolingerbands(df):
        try:
            indicator = "bb"
            latest_data = df.iloc[-1]
            # Bollinger Bands conditions
            condition_bb_lower = latest_data["close"] < latest_data["BB_lower"]
            buy_signal = condition_bb_lower

            return buy_signal, indicator
        except Exception as e:
            print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            logger.error(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            raise Exception(
                f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")

    @staticmethod
    def bollingerbands_zones(df):
        try:
            indicator = "bb_zones"
            latest_data = df.iloc[-1]
            # Bollinger Bands zones conditions
            buy_zone = latest_data["BBBuyZone"]
            sell_zone = latest_data["BBSellZone"]
            neutral_zone = latest_data["BBNeutralZone"]

            # Can be adjusted in future if handling selling
            if buy_zone:
                return True, indicator
            elif sell_zone:
                return False, indicator
            elif neutral_zone:
                return False, indicator
            else:
                return False, indicator

        except Exception as e:
            print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            logger.error(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            raise Exception(f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")


    # RSIDivergence

    @staticmethod
    def rsi_divergence(df, rsi_column="RSI", lookback=lookback_period):
        try:
            indicator = "rsi_divergence"
            buy_signal = False
            # Find local highs and lows in the price
            price_highs = df["close"][df["close"] > df["close"].shift(1)].index
            price_lows = df["close"][df["close"] < df["close"].shift(1)].index

            # Find local highs and lows in the RSI
            rsi_highs = df[rsi_column][df[rsi_column]
                                       > df[rsi_column].shift(1)].index
            rsi_lows = df[rsi_column][df[rsi_column]
                                      < df[rsi_column].shift(1)].index

            # Find bearish divergence (price makes a higher high, RSI makes a lower high)
            for ph_index in price_highs[-lookback:]:
                if ph_index in rsi_highs:
                    continue
                nearest_rsi_high = rsi_highs[np.argmin(
                    np.abs(rsi_highs - ph_index))]
                if df["close"][ph_index] > df["close"][nearest_rsi_high] and df[rsi_column][ph_index] < df[rsi_column][nearest_rsi_high]:
                    print("Bearish divergence detected at index", ph_index)
                    buy_signal = False
                    return buy_signal, indicator

            # Find bullish divergence (price makes a lower low, RSI makes a higher low)
            for pl_index in price_lows[-lookback:]:
                if pl_index in rsi_lows:
                    continue
                nearest_rsi_low = rsi_lows[np.argmin(
                    np.abs(rsi_lows - pl_index))]
                if df["close"][pl_index] < df["close"][nearest_rsi_low] and df[rsi_column][pl_index] > df[rsi_column][nearest_rsi_low]:
                    print("Bullish divergence detected at index", pl_index)
                    buy_signal = True
                    return buy_signal, indicator

            logger.info("No divergence detected")
            return buy_signal, indicator

        except Exception as e:
            print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            raise Exception(f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")

    # # Define strategy for detect_rsi_divergence2
    # def __init__(self, consecutive_bullish_divergences_threshold=3, bullish_divergences_in_period_threshold=3, lookback_period=5):
    #     self.consecutive_bullish_divergences_threshold = consecutive_bullish_divergences_threshold
    #     self.bullish_divergences_in_period_threshold = bullish_divergences_in_period_threshold
    #     self.lookback_period = lookback_period
    #     self.consecutive_bullish_divergences = 0
    #     self.bullish_divergences_in_period = 0
    #     self.start_time = None

    def rsi_divergence_v2(df, rsi_column="RSI", use_consecutive_divergences=True):
        try:
            # Define strategy for detect_rsi_divergence2
            consecutive_bullish_divergences_threshold=3 
            bullish_divergences_in_period_threshold=3
            lookback_period=5
            consecutive_bullish_divergences = 0
            bullish_divergences_in_period = 0
            start_time = None
            indicator = "rsi_divergence"
            buy_signal = False
            # Find local highs and lows in the price
            price_highs = df["close"][df["close"] > df["close"].shift(1)].index
            price_lows = df["close"][df["close"] < df["close"].shift(1)].index

            # Find local highs and lows in the RSI
            rsi_highs = df[rsi_column][df[rsi_column]
                                       > df[rsi_column].shift(1)].index
            rsi_lows = df[rsi_column][df[rsi_column]
                                      < df[rsi_column].shift(1)].index

            # Find bearish divergence (price makes a higher high, RSI makes a lower high)
            for ph_index in price_highs[-lookback_period:]:
                if ph_index in rsi_highs:
                    continue
                nearest_rsi_high = rsi_highs[np.argmin(
                    np.abs(rsi_highs - ph_index))]
                if df["close"][ph_index] > df["close"][nearest_rsi_high] and df[rsi_column][ph_index] < df[rsi_column][nearest_rsi_high]:
                    print("Bearish divergence detected at index", ph_index)
                    buy_signal = False
                    return buy_signal, indicator

            # Find bullish divergence (price makes a lower low, RSI makes a higher low)
            for pl_index in price_lows[-lookback_period:]:
                if pl_index in rsi_lows:
                    continue
                nearest_rsi_low = rsi_lows[np.argmin(
                    np.abs(rsi_lows - pl_index))]
                if df["close"][pl_index] < df["close"][nearest_rsi_low] and df[rsi_column][pl_index] > df[rsi_column][nearest_rsi_low]:
                    if use_consecutive_divergences:
                        if start_time is None:
                            start_time = df.loc[pl_index, "open_time"]
                            consecutive_bullish_divergences += 1
                        elif start_time != df.loc[pl_index, "open_time"]:
                            start_time = df.loc[pl_index, "open_time"]
                            consecutive_bullish_divergences += 1
                        if consecutive_bullish_divergences >= consecutive_bullish_divergences_threshold:
                            print("Bullish divergence detected at index", pl_index)
                            buy_signal = True
                            consecutive_bullish_divergences = 0
                            start_time = None
                    else:  # use divergences in period
                        bullish_divergences_in_period += 1
                        if bullish_divergences_in_period >= bullish_divergences_in_period_threshold:
                            print("Bullish divergence detected at index", pl_index)
                            buy_signal = True
                            bullish_divergences_in_period = 0
                    return buy_signal, indicator

            logger.info("No divergence detected")
            return buy_signal, indicator

        except Exception as e:
            print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            raise Exception(f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")

    def rsi_breakout(df):
        try:
            indicator = "rsi_breakout"
            # Get the latest row in the DataFrame
            latest_row = df.iloc[-1]

            # Check if there is a breakout in the latest row
            buy_signal = latest_row["rsi_breakout"]

            return buy_signal, indicator
        except Exception as e:
            print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            raise Exception(f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")
        

    def supertrend(df):
        try:
            indicator = "supertrend"
            # Get the latest row in the DataFrame
            latest_row = df.iloc[-1]

            # Check if there is a breakout in the latest row
            buy_signal = latest_row["supertrend"]

            return buy_signal, indicator
        except Exception as e:
            print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
            raise Exception(f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")


def execute_indicator_functions_as_list(function_names, df):
    try:
        buy_signals = []
        indicators_execute_function = []

        for funct_name in function_names:
            # Limit function to only be able to call class IndicatorFunctions
            if funct_name in dir(IndicatorFunctions):
                function = getattr(IndicatorFunctions, funct_name, None)
                if callable(function):
                    buy_signal, indicator = function(df)
                    buy_signals.append(buy_signal)
                    indicators_execute_function.append(indicator)
                else:
                    print(f"{funct_name} is not a callable function")
            else:
                print(f"Invalid function name: {funct_name}")

        return buy_signals, indicators_execute_function
    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")

def is_below_zero(series):
    return (series <= 0).all()


def is_above_zero(series):
    return (series >= 0).all()


def indicator_sma_cross(df):
    try:
        indicator = "bb"
        latest_data = df.iloc[-1]
        previous_data = df.iloc[-2]

        latest_sma_short = latest_data["SMA_short"]
        latest_sma_long = latest_data["SMA_long"]
        previous_sma_short = previous_data["SMA_short"]
        previous_sma_long = previous_data["SMA_long"]

        if latest_sma_short > latest_sma_long and previous_sma_short <= previous_sma_long:
            condition_ma_crossover = True
        elif latest_sma_short < latest_sma_long and previous_sma_short >= previous_sma_long:
            condition_ma_crossover = False

        if condition_ma_crossover == None:
            condition_ma_crossover = False

        buy_signal = condition_ma_crossover

        return buy_signal, indicator
    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        logger.error(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(
            f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")


# Pandas-ta

def get_data(client, symbol, interval, period, indicator_window):
    try:

        # Get historical klines
        klines = client.get_historical_klines(symbol, interval, period)

        # Create a DataFrame
        df = pd.DataFrame(klines, columns=["open_time", "open", "high", "low", "close", "volume", "close_time",
                                           "quote_asset_volume", "num_trades", "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"])

        # Convert Price and Volume columns to appropriate data types
        df["close"] = pd.to_numeric(df["close"])
        df["high"] = pd.to_numeric(df["high"])
        df["low"] = pd.to_numeric(df["low"])
        df["volume"] = pd.to_numeric(df["volume"])

        # Simple and Exponential Moving Averages
        df["SMA"] = pta.sma(df["close"], length=indicator_window)
        df["EMA"] = pta.ema(df["close"], length=indicator_window)

        # Stoch
        stoch = pta.stoch(df["high"], df["low"],
                          df["close"], k=indicator_window, d=3)
        df["%K"] = stoch[f"STOCHk_{indicator_window}_3_3"]
        df["%D"] = stoch[f"STOCHd_{indicator_window}_3_3"]

        # MACD
        macd = pta.macd(df["close"], length=indicator_window)
        df["macd"] = macd["MACD_12_26_9"]
        df["macdsignal"] = macd["MACDs_12_26_9"]

        # Bolinger Bands
        bbands = pta.bbands(df["close"], length=indicator_window)
        df["BB_lower"] = bbands[f"BBL_{indicator_window}_2.0"]
        df["BB_middle"] = bbands[f"BBM_{indicator_window}_2.0"]
        df["BB_upper"] = bbands[f"BBU_{indicator_window}_2.0"]

        # Calculate the moving average
        df['MA'] = df['close'].rolling(window=20).mean()

        # Calculate standard deviation
        df['SD'] = df['close'].rolling(window=20).std()

        # Create the two sets of Bollinger Bands
        df['UpperBand1'] = df['MA'] + df['SD']
        df['LowerBand1'] = df['MA'] - df['SD']
        df['UpperBand2'] = df['MA'] + (2 * df['SD'])
        df['LowerBand2'] = df['MA'] - (2 * df['SD'])

        # Define the trading zones
        df['BBBuyZone'] = np.where((df['close'] > df['UpperBand1']) & (df['close'] < df['UpperBand2']), 1, 0)
        df['BBSellZone'] = np.where((df['close'] < df['LowerBand1']) & (df['close'] > df['LowerBand2']), 1, 0)
        df['BBNeutralZone'] = np.where((df['close'] > df['LowerBand1']) & (df['close'] < df['UpperBand1']), 1, 0)


        # Calculate short-term and long-term SMAs for Moving Average Crossover
        short_term_window = 50
        long_term_window = 200
        df["SMA_short"] = pta.sma(df["close"], length=short_term_window)
        df["SMA_long"] = pta.sma(df["close"], length=long_term_window)

        # Calculate ATR Average True Range
        df["ATR"] = pta.atr(df["high"], df["low"],
                            df["close"], length=indicator_window)

        # RSI
        # Calculate rolling min and max for the RSI
        df["RSI"] = pta.rsi(df["close"], length=indicator_window)
        df["RSI_min"] = df["RSI"].rolling(window=lookback_period).min()
        df["RSI_max"] = df["RSI"].rolling(window=lookback_period).max()

        # Identify support levels (local minimums)
        df["RSI_support"] = df.apply(
            lambda row: row["RSI"] if row["RSI"] == row["RSI_min"] else None, axis=1)

        # Identify resistance levels (local maximums)
        df["RSI_resistance"] = df.apply(
            lambda row: row["RSI"] if row["RSI"] == row["RSI_max"] else None, axis=1)

        # Identify support levels (local minimums)
        df["RSI_support"] = df.apply(
            lambda row: row["RSI"] if row["RSI"] == row["RSI_min"] else None, axis=1)

        # Identify resistance levels (local maximums)
        df["RSI_resistance"] = df.apply(
            lambda row: row["RSI"] if row["RSI"] == row["RSI_max"] else None, axis=1)

        # Identify when RSI breaks above the resistance level
        confirmation_period = 3  # Number of periods to confirm breakout
        # Volume must be this times greater than average to confirm breakout
        volume_multiplier = 2
        # Calculate moving average of volume
        df["volume_ma"] = df["volume"].rolling(
            window=confirmation_period).mean()
        # Detect potential breakouts
        df["rsi_potential_breakout"] = (df["RSI"] > df["RSI_resistance"].shift(1)) & (
            df["RSI"].shift(1) <= df["RSI_resistance"].shift(1))
        # Confirm breakouts with volume and confirmation period

        # Calculate the 14-period EMA of the RSI
        df["rsi_ema"] = df["RSI"].ewm(span=14, adjust=False).mean()

        # Define the breakout condition
        df["rsi_breakout"] = df["rsi_potential_breakout"] & \
            (df["volume"] > volume_multiplier * df["volume_ma"]) & \
            (df["rsi_potential_breakout"].shift(confirmation_period - 1).rolling(window=confirmation_period).sum() == confirmation_period) & \
            (df["RSI"] > df["rsi_ema"]) | \
            (df["RSI"] > 70)

        df["EMA_50"] = pta.ema(df["close"], length=50)
        df["EMA_200"] = pta.ema(df["close"], length=200)

        # Calculate the Supertrend
        supertrend = pta.supertrend(df["high"], df["low"], df["close"], length=7, multiplier=3)

        # Append the Supertrend columns to the original DataFrame
        # "SUPERT_7_3.0" represents the Supertrend line.
        # "SUPERTd_7_3.0" represents the direction of the Supertrend line: 1 for up-trend and -1 for down-trend.

        df["SUPERT"] = supertrend["SUPERT_7_3.0"]
        df["SUPERTd"] = supertrend["SUPERTd_7_3.0"]

        df["supertrend"] = bool(df["SUPERTd"].iloc[-1])


        if write_to_csv == True:
            df.to_csv(f'./csv_files/{symbol}.csv', index=False)

        return df

    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        logger.error(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(
            f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")


def get_stop_loss_factor_based_on_atr_value_for_symbol(df):
    try:
        atr_value = df["ATR"].iloc[-1]
        if atr_value is not None:
            # Define a multiplier for the ATR-based stop loss (Recommended is 2 times the ATR)
            multiplier = 4
            close_price = df["close"].iloc[-1]
            stop_loss_percentage = (
                float(atr_value) * float(multiplier)) / float(close_price) * 100
            stop_loss_factor = Decimal(1 - (float(stop_loss_percentage) / 100))
            stop_loss_factor = stop_loss_factor.quantize(
                Decimal('.01'), rounding=ROUND_DOWN)
            return stop_loss_factor
        else:
            print("Failed to calculate ATR.")
            logger.error(
                f"get_stop_loss_factor_based_on_atr_value_for_symbol Failed to calculate ATR.")
    except Exception as e:
        print(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        logger.error(f"{inspect.currentframe().f_code.co_name} Error: {e}")
        raise Exception(
            f"{inspect.currentframe().f_code.co_name} An error occurred: {e}")
