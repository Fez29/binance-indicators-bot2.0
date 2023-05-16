from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship


Base = declarative_base()


class TradingPair(Base):
    __tablename__ = "binance_trading"

    id = Column(Integer, primary_key=True, autoincrement=True)
    base_currency = Column(String(50), nullable=False)
    base_currency_symbol = Column(String(10), nullable=False)
    quote_currency = Column(String(50), nullable=False)
    quote_currency_symbol = Column(String(10), nullable=False)
    trading_pair = Column(String(10), nullable=False, unique=True)
    active = Column(Boolean, nullable=False)


class IndicatorResults(Base):
    __tablename__ = "indicator_results"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    symbol = Column(String(10), nullable=False)
    indicators = Column(String(50), nullable=False)
    triggered_buy = Column(Boolean, nullable=False)
    buy_order_id = Column(Integer, nullable=True)


class Indicator(Base):
    __tablename__ = 'indicators'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    description = Column(String(100), default=name, unique=False)


class Strategy(Base):
    __tablename__ = 'strategies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    active = Column(Boolean, nullable=False)
    description = Column(String(200), nullable=True, unique=False)
    indicators = relationship('StrategyIndicator', back_populates='strategy')


class StrategyIndicator(Base):
    __tablename__ = 'strategy_indicators'

    id = Column(Integer, primary_key=True, autoincrement=True)
    strategy_id = Column(Integer, ForeignKey('strategies.id'))
    indicator_id = Column(Integer, ForeignKey('indicators.id'))
    strategy = relationship('Strategy', back_populates='indicators')
    indicator = relationship('Indicator')
