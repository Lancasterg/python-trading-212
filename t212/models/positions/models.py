from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, RootModel
from t212.models.shared import Instrument


class PositionWalletImpact(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    currency: Optional[str] = None
    current_value: Optional[float] = Field(None, alias="currentValue")
    fx_impact: Optional[float] = Field(None, alias="fxImpact")
    total_cost: Optional[float] = Field(None, alias="totalCost")
    unrealized_profit_loss: Optional[float] = Field(None, alias="unrealizedProfitLoss")


class Position(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    average_price_paid: Optional[float] = Field(None, alias="averagePricePaid")
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    current_price: Optional[float] = Field(None, alias="currentPrice")
    instrument: Optional[Instrument] = None
    quantity: Optional[float] = None
    quantity_available_for_trading: Optional[float] = Field(
        None, alias="quantityAvailableForTrading"
    )
    quantity_in_pies: Optional[float] = Field(None, alias="quantityInPies")
    wallet_impact: Optional[PositionWalletImpact] = Field(None, alias="walletImpact")


class PositionResponse(RootModel[list[Position]]):
    pass


class PositionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    ticker: Optional[str] = None
