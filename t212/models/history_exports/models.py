from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from t212.models.shared import ReportDataIncluded


class EnqueuedReportResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    report_id: int = Field(alias="reportId")


class PublicReportRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    data_included: Optional[ReportDataIncluded] = Field(None, alias="dataIncluded")
    time_from: Optional[datetime] = Field(None, alias="timeFrom")
    time_to: Optional[datetime] = Field(None, alias="timeTo")


class ReportResponseStatus(str, Enum):
    Queued = "Queued"
    Processing = "Processing"
    Running = "Running"
    Canceled = "Canceled"
    Failed = "Failed"
    Finished = "Finished"


class ReportResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    data_included: Optional[ReportDataIncluded] = Field(None, alias="dataIncluded")
    download_link: Optional[str] = Field(None, alias="downloadLink")
    report_id: int = Field(alias="reportId")
    status: Optional[ReportResponseStatus] = None
    time_from: Optional[datetime] = Field(None, alias="timeFrom")
    time_to: Optional[datetime] = Field(None, alias="timeTo")
