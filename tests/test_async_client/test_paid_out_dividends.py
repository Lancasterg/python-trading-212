import pytest
import aiohttp
from t212.async_client import AsyncTrading212Client


@pytest.mark.asyncio
async def test_paid_out_dividends_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests the successful (200 OK) response of the paid_out_dividends method.
    """
    response = await async_client_fixture.paid_out_dividends(cursor=0, ticker="AAPL_US")

    assert response is not None
    assert len(response.items) == 1
    assert response.items[0].id == "d1"


@pytest.mark.asyncio
async def test_paid_out_dividends_400(async_client_fixture: AsyncTrading212Client):
    """
    Tests the 400 Bad Request response of the paid_out_dividends method.
    """
    with pytest.raises(aiohttp.ClientResponseError) as excinfo:
        await async_client_fixture.paid_out_dividends(cursor=400, ticker="AAPL_US")
    assert excinfo.value.status == 400


@pytest.mark.asyncio
async def test_paid_out_dividends_500(async_client_fixture: AsyncTrading212Client):
    """
    Tests the 500 Internal Server Error response of the paid_out_dividends method.
    """
    with pytest.raises(aiohttp.ClientResponseError) as excinfo:
        await async_client_fixture.paid_out_dividends(cursor=500, ticker="AAPL_US")
    assert excinfo.value.status == 500
