from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class Cash(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    available_to_trade: Optional[float] = Field(None, alias="availableToTrade")
    in_pies: Optional[float] = Field(None, alias="inPies")
    reserved_for_orders: Optional[float] = Field(None, alias="reservedForOrders")


class Investments(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    current_value: Optional[float] = Field(None, alias="currentValue")
    realized_profit_loss: Optional[float] = Field(None, alias="realisedProfitLoss")
    total_cost: Optional[float] = Field(None, alias="totalCost")
    unrealized_profit_loss: Optional[float] = Field(None, alias="unrealizedProfitLoss")


class AccountSummary(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    cash: Optional[Cash] = None
    currency: Optional[str] = None
    id: int
    investments: Optional[Investments] = None
    total_value: Optional[float] = Field(None, alias="totalValue")


class AccountResponse(BaseModel):
    # Backward compatibility model for account response info if needed by old tests
    model_config = ConfigDict(populate_by_name=True)

    currency_code: str = Field(
        ..., alias="currencyCode", description="ISO 4217", max_length=3, min_length=3
    )
    id: int
