import pytest
from t212.async_client import AsyncTrading212Client
from t212.models import AccountSummary, Cash, Investments


@pytest.mark.asyncio
async def test_fetch_account_summary_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests the successful (200 OK) response of the fetch_account_summary method.
    """
    response = await async_client_fixture.fetch_account_summary()

    assert response is not None
    assert response.id == 12345
    assert response.currency == "GBP"
    assert response.total_value == 1500.0
    assert response.cash is not None
    assert response.cash.available_to_trade == 1000.0
    assert response.cash.reserved_for_orders == 500.0
    assert response.investments is not None
    assert response.investments.current_value == 500.0
    assert response.investments.realized_profit_loss == 50.0
    assert response.investments.total_cost == 400.0
    assert response.investments.unrealized_profit_loss == 100.0
