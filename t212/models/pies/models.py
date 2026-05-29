from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field, RootModel
from t212.models.shared import DividendDetails, InvestmentResult


class DividendCashAction(str, Enum):
    REINVEST = "REINVEST"
    TO_ACCOUNT_CASH = "TO_ACCOUNT_CASH"


class AccountBucketDetailedResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    creation_date: datetime = Field(alias="creationDate")
    dividend_cash_action: DividendCashAction = Field(alias="dividendCashAction")
    end_date: Optional[datetime] = Field(None, alias="endDate")
    goal: Optional[float] = None
    icon: Optional[str] = None
    id: int
    initial_investment: Optional[float] = Field(None, alias="initialInvestment")
    instrument_shares: Optional[Dict[str, float]] = Field(
        None, alias="instrumentShares"
    )
    name: Optional[str] = None
    public_url: Optional[str] = Field(None, alias="publicUrl")


class InstrumentIssueName(str, Enum):
    DELISTED = "DELISTED"
    SUSPENDED = "SUSPENDED"
    NO_LONGER_TRADABLE = "NO_LONGER_TRADABLE"
    MAX_POSITION_SIZE_REACHED = "MAX_POSITION_SIZE_REACHED"
    APPROACHING_MAX_POSITION_SIZE = "APPROACHING_MAX_POSITION_SIZE"
    COMPLEX_INSTRUMENT_APP_TEST_REQUIRED = "COMPLEX_INSTRUMENT_APP_TEST_REQUIRED"
    PRICE_TOO_LOW = "PRICE_TOO_LOW"


class InstrumentIssueSeverity(str, Enum):
    IRREVERSIBLE = "IRREVERSIBLE"
    REVERSIBLE = "REVERSIBLE"
    INFORMATIVE = "INFORMATIVE"


class InstrumentIssue(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: InstrumentIssueName
    severity: InstrumentIssueSeverity


class AccountBucketInstrumentResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    current_share: Optional[float] = Field(None, alias="currentShare")
    expected_share: Optional[float] = Field(None, alias="expectedShare")
    issues: Optional[List[InstrumentIssue]] = None
    owned_quantity: Optional[float] = Field(None, alias="ownedQuantity")
    result: Optional[InvestmentResult] = None
    ticker: Optional[str] = None


class AccountBucketInstrumentsDetailedResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    instruments: Optional[List[AccountBucketInstrumentResult]] = None
    settings: Optional[AccountBucketDetailedResponse] = None


class AccountBucketResultResponseStatus(str, Enum):
    AHEAD = "AHEAD"
    ON_TRACK = "ON_TRACK"
    BEHIND = "BEHIND"


class AccountBucketResultResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    cash: Optional[float] = Field(
        None, description="Amount of money put into the pie in account currency"
    )
    dividend_details: Optional[DividendDetails] = Field(None, alias="dividendDetails")
    id: int
    progress: Optional[float] = Field(
        None, description="Progress of the pie based on the set goal", example=0.5
    )
    result: Optional[InvestmentResult] = None
    status: Optional[AccountBucketResultResponseStatus] = Field(
        None, description="Status of the pie based on the set goal"
    )


class DuplicateBucketRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    icon: Optional[str] = None
    name: Optional[str] = None


class PieRequestDividendCashAction(str, Enum):
    REINVEST = "REINVEST"
    TO_ACCOUNT_CASH = "TO_ACCOUNT_CASH"


class PieRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    dividend_cash_action: Optional[PieRequestDividendCashAction] = Field(
        None, alias="dividendCashAction"
    )
    end_date: Optional[datetime] = Field(None, alias="endDate")
    goal: Optional[float] = Field(
        None, description="Total desired value of the pie in account currency"
    )
    icon: Optional[str] = None
    instrument_shares: Optional[Dict[str, float]] = Field(
        None, alias="instrumentShares", example={"AAPL_US_EQ": 0.5, "MSFT_US_EQ": 0.5}
    )
    name: Optional[str] = None


class FetchAllPiesResponse(RootModel[list[AccountBucketResultResponse]]):
    pass


class FetchAPieResponse(RootModel[list[AccountBucketInstrumentsDetailedResponse]]):
    pass
