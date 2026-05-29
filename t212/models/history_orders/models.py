from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field
from t212.models.shared import Tax
from t212.models.orders.models import Order


class FillWalletImpact(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    currency: Optional[str] = None
    fx_rate: Optional[float] = Field(None, alias="fxRate")
    net_value: Optional[float] = Field(None, alias="netValue")
    realised_profit_loss: Optional[float] = Field(None, alias="realisedProfitLoss")
    taxes: Optional[List[Tax]] = None


class FillTradingMethod(str, Enum):
    TOTV = "TOTV"
    OTC = "OTC"


class FillType(str, Enum):
    TRADE = "TRADE"
    STOCK_SPLIT = "STOCK_SPLIT"
    STOCK_DISTRIBUTION = "STOCK_DISTRIBUTION"
    FOP = "FOP"
    FOP_CORRECTION = "FOP_CORRECTION"
    CUSTOM_STOCK_DISTRIBUTION = "CUSTOM_STOCK_DISTRIBUTION"
    EQUITY_RIGHTS = "EQUITY_RIGHTS"
    SCRIP_STOCK_DIVIDENDS = "SCRIP_STOCK_DIVIDENDS"
    STOCK_DIVIDENDS = "STOCK_DIVIDENDS"
    STOCK_ACQUISITION = "STOCK_ACQUISITION"
    CASH_AND_STOCK_ACQUISITION = "CASH_AND_STOCK_ACQUISITION"
    SPIN_OFF = "SPIN_OFF"


class Fill(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    filled_at: Optional[datetime] = Field(None, alias="filledAt")
    id: int
    price: Optional[float] = None
    quantity: Optional[float] = None
    trading_method: Optional[FillTradingMethod] = Field(None, alias="tradingMethod")
    type: Optional[FillType] = None
    wallet_impact: Optional[FillWalletImpact] = Field(None, alias="walletImpact")


class HistoricalOrder(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    fill: Optional[Fill] = None
    order: Optional[Order] = None


class PaginatedResponseHistoricalOrderResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    items: Optional[List[HistoricalOrder]] = None
    next_page_path: Optional[str] = Field(None, alias="nextPagePath")
