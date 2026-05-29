from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field, RootModel
from t212.models.shared import Instrument


class OrderStatus(str, Enum):
    LOCAL = "LOCAL"
    UNCONFIRMED = "UNCONFIRMED"
    CONFIRMED = "CONFIRMED"
    NEW = "NEW"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    FILLED = "FILLED"
    REJECTED = "REJECTED"
    REPLACING = "REPLACING"
    REPLACED = "REPLACED"


class OrderStrategy(str, Enum):
    QUANTITY = "QUANTITY"
    VALUE = "VALUE"


class OrderType(str, Enum):
    LIMIT = "LIMIT"
    STOP = "STOP"
    MARKET = "MARKET"
    STOP_LIMIT = "STOP_LIMIT"


class OrderInitiatedFrom(str, Enum):
    API = "API"
    IOS = "IOS"
    ANDROID = "ANDROID"
    WEB = "WEB"
    SYSTEM = "SYSTEM"
    AUTOINVEST = "AUTOINVEST"
    INSTRUMENT_AUTOINVEST = "INSTRUMENT_AUTOINVEST"


class Order(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    created_at: Optional[datetime] = Field(None, alias="createdAt")
    currency: Optional[str] = None
    extended_hours: Optional[bool] = Field(None, alias="extendedHours")
    filled_quantity: Optional[float] = Field(
        None, alias="filledQuantity", description="Applicable to quantity orders"
    )
    filled_value: Optional[float] = Field(
        None, alias="filledValue", description="Applicable to value orders"
    )
    id: int
    initiated_from: Optional[OrderInitiatedFrom] = Field(None, alias="initiatedFrom")
    instrument: Optional[Instrument] = None
    limit_price: Optional[float] = Field(
        None,
        alias="limitPrice",
        description="Applicable to LIMIT and STOP_LIMIT orders",
    )
    quantity: Optional[float] = Field(None, description="Applicable to quantity orders")
    side: Optional[str] = None
    status: Optional[OrderStatus] = None
    stop_price: Optional[float] = Field(
        None, alias="stopPrice", description="Applicable to STOP and STOP_LIMIT orders"
    )
    strategy: Optional[OrderStrategy] = None
    ticker: Optional[str] = Field(
        None,
        description="Unique instrument identifier. Get from the /instruments endpoint",
        example="AAPL_US_EQ",
    )
    time_in_force: Optional[str] = Field(None, alias="timeInForce")
    type: Optional[OrderType] = None
    value: Optional[float] = Field(None, description="Applicable to value orders")


class FetchAllEquityOrdersResponse(RootModel[list[Order]]):
    pass


class LimitRequestTimeValidity(str, Enum):
    DAY = "DAY"
    GOOD_TILL_CANCEL = "GOOD_TILL_CANCEL"


class LimitRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    limit_price: float = Field(..., alias="limitPrice", example=100.23)
    quantity: float = Field(..., example=0.1)
    ticker: str = Field(..., example="AAPL_US_EQ")
    time_validity: LimitRequestTimeValidity = Field(
        ..., alias="timeValidity", description="Expiration", example="DAY"
    )


class MarketRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    quantity: float = Field(..., example=0.1)
    ticker: str = Field(..., example="AAPL_US_EQ")


class StopLimitRequestTimeValidity(str, Enum):
    DAY = "DAY"
    GOOD_TILL_CANCEL = "GOOD_TILL_CANCEL"


class StopLimitRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    limit_price: float = Field(..., alias="limitPrice", example=100.23)
    quantity: float = Field(..., example=0.1)
    stop_price: float = Field(..., alias="stopPrice", example=100.23)
    ticker: str = Field(..., example="AAPL_US_EQ")
    time_validity: StopLimitRequestTimeValidity = Field(
        ..., alias="timeValidity", description="Expiration", example="DAY"
    )


class StopRequestTimeValidity(str, Enum):
    DAY = "DAY"
    GOOD_TILL_CANCEL = "GOOD_TILL_CANCEL"


class StopRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    quantity: float = Field(..., example=0.1)
    stop_price: float = Field(..., alias="stopPrice", example=100.23)
    ticker: str = Field(..., example="AAPL_US_EQ")
    time_validity: StopRequestTimeValidity = Field(
        ..., alias="timeValidity", description="Expiration", example="DAY"
    )


class PlaceOrderErrorCode(str, Enum):
    SellingEquityNotOwned = "SellingEquityNotOwned"
    CantLegalyTradeException = "CantLegalyTradeException"
    InsufficientResources = "InsufficientResources"
    InsufficientValueForStocksSell = "InsufficientValueForStocksSell"
    TargetPriceTooFar = "TargetPriceTooFar"
    TargetPriceTooClose = "TargetPriceTooClose"
    NotEligibleForISA = "NotEligibleForISA"
    ShareLendingAgreementNotAccepted = "ShareLendingAgreementNotAccepted"
    InstrumentNotFound = "InstrumentNotFound"
    MaxEquityBuyQuantityExceeded = "MaxEquityBuyQuantityExceeded"
    MaxEquitySellQuantityExceeded = "MaxEquitySellQuantityExceeded"
    LimitPriceMissing = "LimitPriceMissing"
    StopPriceMissing = "StopPriceMissing"
    TickerMissing = "TickerMissing"
    QuantityMissing = "QuantityMissing"
    MaxQuantityExceeded = "MaxQuantityExceeded"
    InvalidValue = "InvalidValue"
    InsufficientFreeForStocksException = "InsufficientFreeForStocksException"
    MinValueExceeded = "MinValueExceeded"
    MinQuantityExceeded = "MinQuantityExceeded"
    PriceTooFar = "PriceTooFar"
    UNDEFINED = "UNDEFINED"
    NotAvailableForRealMoneyAccounts = "NotAvailableForRealMoneyAccounts"


class PlaceOrderError(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    clarification: Optional[str] = None
    code: Optional[PlaceOrderErrorCode] = None
