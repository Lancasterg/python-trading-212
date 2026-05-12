import pytest
from t212.async_client import AsyncTrading212Client


@pytest.mark.asyncio
async def test_fetch_all_open_positions_200(
    async_client_fixture: AsyncTrading212Client,
):
    """
    Tests the successful (200 OK) response of the fetch_all_open_positions method.
    """
    response = await async_client_fixture.fetch_all_open_positions()

    assert response is not None
    assert len(response) == 2
    assert response[0].ticker == "AAPL_US"
