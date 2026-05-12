# import pytest
# import aiohttp
# from t212.async_client import AsyncTrading212Client


# @pytest.mark.asyncio
# async def test_fetch_open_position_by_id_200(
#     async_client_fixture: AsyncTrading212Client,
# ):
#     """
#     Tests the successful (200 OK) response of the fetch_open_position_by_id method.
#     """
#     response = await async_client_fixture.fetch_open_position_by_id(position_id=123)

#     assert response is not None
#     assert response.ticker == "AAPL_US"


# @pytest.mark.asyncio
# async def test_fetch_open_position_by_id_400(
#     async_client_fixture: AsyncTrading212Client,
# ):
#     """
#     Tests the 400 Bad Request response of the fetch_open_position_by_id method.
#     """
#     with pytest.raises(aiohttp.ClientResponseError) as excinfo:
#         await async_client_fixture.fetch_open_position_by_id(position_id=400)
#     assert excinfo.value.status == 400


# @pytest.mark.asyncio
# async def test_fetch_open_position_by_id_500(
#     async_client_fixture: AsyncTrading212Client,
# ):
#     """
#     Tests the 500 Internal Server Error response of the fetch_open_position_by_id method.
#     """
#     with pytest.raises(aiohttp.ClientResponseError) as excinfo:
#         await async_client_fixture.fetch_open_position_by_id(position_id=500)
#     assert excinfo.value.status == 500
