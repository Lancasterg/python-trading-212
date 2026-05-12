from t212.models import AccountResponse
import pytest
from t212.async_client import AsyncTrading212Client


@pytest.mark.asyncio
async def test_fetch_account_metadata_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests the successful (200 OK) response of the fetch_account_metadata method.
    """
    response = await async_client_fixture.fetch_account_metadata()

    assert response == AccountResponse(id=12345, currency_code="GBP", account_type="ISA")
