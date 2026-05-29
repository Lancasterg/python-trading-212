from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import AliasChoices, BaseModel, ConfigDict, Field


class Instrument(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    currency: Optional[str] = None
    isin: Optional[str] = None
    name: Optional[str] = None
    ticker: Optional[str] = None


class InvestmentResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    price_avg_invested_value: Optional[float] = Field(
        None, alias="priceAvgInvestedValue"
    )
    price_avg_result: Optional[float] = Field(None, alias="priceAvgResult")
    price_avg_result_coef: Optional[float] = Field(None, alias="priceAvgResultCoef")
    price_avg_value: Optional[float] = Field(None, alias="priceAvgValue")


class DividendDetails(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    gained: Optional[float] = None
    in_cash: Optional[float] = Field(None, alias="inCash")
    reinvested: Optional[float] = None


class TaxName(str, Enum):
    COMMISSION_TURNOVER = "COMMISSION_TURNOVER"
    CURRENCY_CONVERSION_FEE = "CURRENCY_CONVERSION_FEE"
    FINRA_FEE = "FINRA_FEE"
    FRENCH_TRANSACTION_TAX = "FRENCH_TRANSACTION_TAX"
    PTM_LEVY = "PTM_LEVY"
    STAMP_DUTY = "STAMP_DUTY"
    STAMP_DUTY_RESERVE_TAX = "STAMP_DUTY_RESERVE_TAX"
    TRANSACTION_FEE = "TRANSACTION_FEE"


class Tax(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    charged_at: Optional[datetime] = Field(None, alias="chargedAt")
    currency: Optional[str] = None
    name: Optional[TaxName] = None
    quantity: Optional[float] = None


class ReportDataIncluded(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    include_dividends: Optional[bool] = Field(None, alias="includeDividends")
    include_interest: Optional[bool] = Field(None, alias="includeInterest")
    include_orders: Optional[bool] = Field(None, alias="includeOrders")
    include_transactions: Optional[bool] = Field(None, alias="includeTransactions")
