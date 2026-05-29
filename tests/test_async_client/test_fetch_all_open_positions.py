from t212.models import Position, PositionResponse
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

    expected_response = PositionResponse.model_validate(
        [
            {
                "averagePricePaid": 100,
                "createdAt": "2019-08-24T14:15:22Z",
                "currentPrice": 110,
                "instrument": {
                    "currency": "USD",
                    "isin": "string",
                    "name": "string",
                    "ticker": "AAPL_US_EQ",
                },
                "quantity": 10,
                "quantityAvailableForTrading": 10,
                "quantityInPies": 0,
                "walletImpact": {
                    "currency": "string",
                    "currentValue": 1100,
                    "fxImpact": 0,
                    "totalCost": 1000,
                    "unrealizedProfitLoss": 100,
                },
            }
        ]
    )
    assert response == expected_response
