import pytest
import aiohttp
from t212.async_client import AsyncTrading212Client


@pytest.mark.asyncio
async def test_historical_order_data_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests the successful (200 OK) response of the historical_order_data method.
    """
    response = await async_client_fixture.historical_order_data(0, "GOOG")

    assert response is not None
    assert len(response.items) == 1
    assert response.items[0].id == 1


@pytest.mark.asyncio
async def test_historical_order_data_400(async_client_fixture: AsyncTrading212Client):
    """
    Tests the 400 Bad Request response of the historical_order_data method.
    """
    with pytest.raises(aiohttp.ClientResponseError) as excinfo:
        await async_client_fixture.historical_order_data(400, "GOOG")
    assert excinfo.value.status == 400


@pytest.mark.asyncio
async def test_historical_order_data_500(async_client_fixture: AsyncTrading212Client):
    """
    Tests the 500 Internal Server Error response of the historical_order_data method.
    """
    with pytest.raises(aiohttp.ClientResponseError) as excinfo:
        await async_client_fixture.historical_order_data(500, "GOOG")
    assert excinfo.value.status == 500
