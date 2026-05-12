from t212.models import (
    Order,
    FetchAllEquityOrdersResponse,
    OrderStatus,
    OrderType,
    OrderStrategy,
)
import pytest
from t212.async_client import AsyncTrading212Client


@pytest.mark.asyncio
async def test_fetch_all_equity_orders_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests the successful (200 OK) response of the fetch_all_equity_orders method.
    """
    # Act
    response = await async_client_fixture.fetch_all_equity_orders()

    # Assert
    expected_response = FetchAllEquityOrdersResponse(
        root=[
            Order(
                id=0,
                status=OrderStatus.LOCAL,
                ticker="AAPL_US_EQ",
                type=OrderType.LIMIT,
                quantity=0,
                filledQuantity=0,
                limitPrice=0,
                stopPrice=0,
                value=0,
                filledValue=0,
                strategy=OrderStrategy.QUANTITY,
                # Note: 'creationTime' is not in the JSON, so it remains None
                creationTime=None,
            )
        ]
    )
    assert response == expected_response
