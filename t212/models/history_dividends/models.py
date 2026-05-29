from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field
from t212.models.shared import Instrument


class HistoryDividendItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    amount: Optional[float] = Field(None, description="In account currency")
    amount_in_euro: Optional[float] = Field(None, alias="amountInEuro")
    gross_amount_per_share: Optional[float] = Field(
        None, alias="grossAmountPerShare", description="In instrument currency"
    )
    instrument: Optional[Instrument] = None
    paid_on: Optional[datetime] = Field(None, alias="paidOn")
    quantity: Optional[float] = None
    reference: Optional[str] = None
    ticker: Optional[str] = None
    type: Optional[str] = None


class PaginatedResponseHistoryDividendItemResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    items: Optional[List[HistoryDividendItem]] = None
    next_page_path: Optional[str] = Field(None, alias="nextPagePath")
