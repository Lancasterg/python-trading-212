from t212.models import Order
from t212.models import FetchAllEquityOrdersResponse
import pytest
from t212.async_client import AsyncTrading212Client


@pytest.mark.asyncio
async def test_fetch_all_equity_orders_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests the successful (200 OK) response of the fetch_all_equity_orders method.
    """
    response = await async_client_fixture.fetch_all_equity_orders()

    assert response == FetchAllEquityOrdersResponse(
        root=[
            Order(id=123, ticker="AAPL_US", quantity=10, type="LIMIT"),
            Order(id=456, ticker="GOOG_US", quantity=5, type="MARKET")
            ])
