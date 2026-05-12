from t212.models import ExchangeResponse
import pytest
import pytest_asyncio
from t212.async_client import AsyncTrading212Client




@pytest.mark.asyncio
async def test_exchange_list_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests the successful (200 OK) response of the exchange_list method.
    """
    response = await async_client_fixture.exchange_list()

    assert response.model_dump() == [
        {
          "id": 1,
          "name": "LSE",
          "working_schedules": []
        },
        {
          "id": 2,
          "name": "NYSE",
          "working_schedules": []
        }
      ]