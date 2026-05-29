import pytest
import aiohttp
from t212.async_client import AsyncTrading212Client
from t212.models import (
    PieRequest,
    DuplicateBucketRequest,
    PublicReportRequest,
    ReportDataIncluded,
)


@pytest.mark.asyncio
async def test_cancel_order(async_client_fixture: AsyncTrading212Client):
    """
    Tests the cancel_order method.
    """
    # Simply verify it runs and returns success (status 200 mapped in wiremock)
    await async_client_fixture.cancel_order(123)


@pytest.mark.asyncio
async def test_pie_crud(async_client_fixture: AsyncTrading212Client):
    """
    Tests create, update, delete, and duplicate pie endpoints.
    """
    pie_request = PieRequest(name="My Pie")

    # Create
    created = await async_client_fixture.create_pie(pie_request)
    assert created is not None
    assert created.id == 1
    assert created.name == "My Pie"

    # Update
    updated = await async_client_fixture.update_pie(1, pie_request)
    assert updated is not None
    assert updated.id == 1
    assert updated.name == "My Updated Pie"

    # Duplicate
    dup_req = DuplicateBucketRequest(name="My Duplicated Pie")
    duplicated = await async_client_fixture.duplicate_pie(1, dup_req)
    assert duplicated is not None
    assert duplicated.id == 2
    assert duplicated.name == "My Duplicated Pie"

    # Delete
    await async_client_fixture.delete_pie(1)


@pytest.mark.asyncio
async def test_csv_reports(async_client_fixture: AsyncTrading212Client):
    """
    Tests list_generated_reports and request_csv_report endpoints.
    """
    # List
    reports = await async_client_fixture.list_generated_reports()
    assert len(reports) == 1
    assert reports[0].report_id == 123
    assert reports[0].status == "Finished"

    # Request
    req = PublicReportRequest(data_included=ReportDataIncluded(include_dividends=True))
    enqueued = await async_client_fixture.request_csv_report(req)
    assert enqueued.report_id == 123
