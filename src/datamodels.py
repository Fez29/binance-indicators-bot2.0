from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TradingBotRequest(BaseModel):
    coin_symbol: str
    stop_loss: float
    target_profit: float
    buy_currency: str
    buy_amount: float
    indicator: str

class CancelOpenOrders(BaseModel):
    testnet: bool
    coin_symbol: str

class ResponseData(BaseModel):
    status: str
    buyOrderId: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    symbol: str
    msg: str