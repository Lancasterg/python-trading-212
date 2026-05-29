import pytest
from t212.async_client import AsyncTrading212Client
from t212.models import (
    Order,
    LimitRequestTimeValidity,
    StopRequestTimeValidity,
    StopLimitRequestTimeValidity,
)


@pytest.mark.asyncio
async def test_place_limit_order_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests placing a limit order.
    """
    response = await async_client_fixture.place_limit_order(
        limit_price=100.23,
        quantity=10.0,
        ticker="AAPL_US_EQ",
        time_validity=LimitRequestTimeValidity.DAY,
    )

    assert response is not None
    assert response.id == 101
    assert response.limit_price == 100.23
    assert response.quantity == 10.0
    assert response.ticker == "AAPL_US_EQ"
    assert response.type.value == "LIMIT"


@pytest.mark.asyncio
async def test_place_market_order_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests placing a market order.
    """
    response = await async_client_fixture.place_market_order(
        quantity=10.0,
        ticker="AAPL_US_EQ",
    )

    assert response is not None
    assert response.id == 102
    assert response.quantity == 10.0
    assert response.ticker == "AAPL_US_EQ"
    assert response.type.value == "MARKET"


@pytest.mark.asyncio
async def test_place_stop_order_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests placing a stop order.
    """
    response = await async_client_fixture.place_stop_order(
        quantity=10.0,
        stop_price=100.23,
        ticker="AAPL_US_EQ",
        time_validity=StopRequestTimeValidity.DAY,
    )

    assert response is not None
    assert response.id == 103
    assert response.stop_price == 100.23
    assert response.quantity == 10.0
    assert response.ticker == "AAPL_US_EQ"
    assert response.type.value == "STOP"


@pytest.mark.asyncio
async def test_place_stop_limit_order_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests placing a stop-limit order.
    """
    response = await async_client_fixture.place_stop_limit_order(
        limit_price=100.23,
        quantity=10.0,
        stop_price=100.23,
        ticker="AAPL_US_EQ",
        time_validity=StopLimitRequestTimeValidity.DAY,
    )

    assert response is not None
    assert response.id == 104
    assert response.limit_price == 100.23
    assert response.stop_price == 100.23
    assert response.quantity == 10.0
    assert response.ticker == "AAPL_US_EQ"
    assert response.type.value == "STOP_LIMIT"


@pytest.mark.asyncio
async def test_cancel_pending_order_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests cancelling a pending order.
    """
    await async_client_fixture.cancel_pending_order(order_id=123)
