import pytest
from t212.async_client import AsyncTrading212Client


@pytest.mark.asyncio
async def test_instrument_list_200(async_client_fixture: AsyncTrading212Client):
    """
    Tests the successful (200 OK) response of the instrument_list method.
    """
    response = await async_client_fixture.instrument_list()

    assert response is not None
    # Add assertions based on the actual model structure
    assert len(response.root) == 2
    assert response.root[0].name == "Apple"
