import pytest_asyncio

from t212.async_client import AsyncTrading212Client


@pytest_asyncio.fixture
async def async_client_fixture():
    """
    Provides a configured instance of the AsyncTrading212Client for testing,
    ensuring the session is properly closed after the test.
    """
    AsyncTrading212Client.init_client()
    test_client = AsyncTrading212Client
    # Point the client to the mock server
    test_client.base_url = "http://localhost:8080"
    yield test_client
    # Teardown: close the client session
    await test_client.close_client()
