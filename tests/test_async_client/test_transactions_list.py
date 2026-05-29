import pytest
import aiohttp
from t212.async_client import AsyncTrading212Client


@pytest.mark.asyncio
async def test_transactions_list_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests the successful (200 OK) response of the transactions_list method.
    """
    response = await async_client_fixture.transactions_list(cursor=0, ticker="AAPL_US")

    assert response is not None
    assert len(response.items) == 1
    assert response.items[0].reference == "t1"


@pytest.mark.asyncio
async def test_transactions_list_400(async_client_fixture: AsyncTrading212Client):
    """
    Tests the 400 Bad Request response of the transactions_list method.
    """
    with pytest.raises(aiohttp.ClientResponseError) as excinfo:
        await async_client_fixture.transactions_list(cursor=400, ticker="AAPL_US")
    assert excinfo.value.status == 400


@pytest.mark.asyncio
async def test_transactions_list_500(async_client_fixture: AsyncTrading212Client):
    """
    Tests the 500 Internal Server Error response of the transactions_list method.
    """
    with pytest.raises(aiohttp.ClientResponseError) as excinfo:
        await async_client_fixture.transactions_list(cursor=500, ticker="AAPL_US")
    assert excinfo.value.status == 500
