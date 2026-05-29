from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import AliasChoices, BaseModel, ConfigDict, Field


class HistoryTransactionItemType(str, Enum):
    WITHDRAW = "WITHDRAW"
    DEPOSIT = "DEPOSIT"
    FEE = "FEE"
    TRANSFER = "TRANSFER"


class HistoryTransactionItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    amount: Optional[float] = Field(None, description="In the account currency")
    date_time: Optional[datetime] = Field(None, alias="dateTime")
    reference: Optional[str] = Field(
        None,
        validation_alias=AliasChoices("reference", "id"),
        serialization_alias="reference",
        description="ID",
    )
    type: Optional[HistoryTransactionItemType] = None


class PaginatedResponseHistoryTransactionItemResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    items: Optional[List[HistoryTransactionItem]] = None
    next_page_path: Optional[str] = Field(None, alias="nextPagePath")
