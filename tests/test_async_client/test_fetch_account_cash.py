import pytest
from t212.async_client import AsyncTrading212Client


@pytest.mark.asyncio
async def test_fetch_account_cash_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests the successful (200 OK) response of the fetch_account_cash method.
    """
    response = await async_client_fixture.fetch_account_cash()

    assert response is not None
    assert response.free == 1000.0
    assert response.total == 1500.0
