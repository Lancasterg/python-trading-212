from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import AliasChoices, BaseModel, ConfigDict, Field, RootModel


class TimeEventType(str, Enum):
    OPEN = "OPEN"
    CLOSE = "CLOSE"
    BREAK_START = "BREAK_START"
    BREAK_END = "BREAK_END"
    PRE_MARKET_OPEN = "PRE_MARKET_OPEN"
    AFTER_HOURS_OPEN = "AFTER_HOURS_OPEN"
    AFTER_HOURS_CLOSE = "AFTER_HOURS_CLOSE"
    OVERNIGHT_OPEN = "OVERNIGHT_OPEN"


class TimeEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    date: datetime
    type: TimeEventType


class WorkingSchedule(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    time_events: Optional[List[TimeEvent]] = Field(None, alias="timeEvents")


class Exchange(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    name: Optional[str] = None
    working_schedules: Optional[List[WorkingSchedule]] = Field(
        None, alias="workingSchedules"
    )


class ExchangeResponse(RootModel[list[Exchange]]):
    pass


class TradeableInstrumentType(str, Enum):
    CRYPTOCURRENCY = "CRYPTOCURRENCY"
    ETF = "ETF"
    FOREX = "FOREX"
    FUTURES = "FUTURES"
    INDEX = "INDEX"
    STOCK = "STOCK"
    WARRANT = "WARRANT"
    CRYPTO = "CRYPTO"
    CVR = "CVR"
    CORPACT = "CORPACT"


class TradeableInstrument(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    added_on: Optional[datetime] = Field(
        None, alias="addedOn", description="On the platform since"
    )
    currency_code: str = Field(
        ...,
        validation_alias=AliasChoices("currencyCode", "currency"),
        serialization_alias="currencyCode",
        description="ISO 4217",
        max_length=3,
        min_length=3,
        example="USD",
    )
    isin: Optional[str] = None
    max_open_quantity: Optional[float] = Field(None, alias="maxOpenQuantity")
    name: Optional[str] = None
    short_name: Optional[str] = Field(None, alias="shortName")
    ticker: str = Field(..., description="Unique identifier", example="AAPL_US_EQ")
    type: TradeableInstrumentType = Field(..., example="ETF")
    working_schedule_id: Optional[int] = Field(
        None,
        alias="workingScheduleId",
        description="Get items in the /exchanges endpoint",
    )


class InstrumentListResponse(RootModel[list[TradeableInstrument]]):
    pass
