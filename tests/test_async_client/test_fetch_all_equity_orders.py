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
    expected_response = FetchAllEquityOrdersResponse.model_validate(
        [
            {
                "createdAt": "2019-08-24T14:15:22Z",
                "currency": "string",
                "extendedHours": True,
                "filledQuantity": 0,
                "filledValue": 0,
                "id": 0,
                "initiatedFrom": "API",
                "instrument": {
                    "currency": "string",
                    "isin": "string",
                    "name": "string",
                    "ticker": "AAPL_US_EQ",
                },
                "limitPrice": 0,
                "quantity": 0,
                "side": "BUY",
                "status": "LOCAL",
                "stopPrice": 0,
                "strategy": "QUANTITY",
                "ticker": "AAPL_US_EQ",
                "timeInForce": "DAY",
                "type": "LIMIT",
                "value": 0,
            }
        ]
    )
    assert response == expected_response
