from typing import TypeVar, List

import requests

from t212 import config
from t212.exceptions import not_implemented_api_field
from t212.models import (
    AccountSummary,
    ExchangeResponse,
    FetchAllEquityOrdersResponse,
    FetchAllPiesResponse,
    FetchAPieResponse,
    InstrumentListResponse,
    LimitRequestTimeValidity,
    Order,
    PaginatedResponseHistoricalOrderResponse,
    PaginatedResponseHistoryDividendItemResponse,
    PaginatedResponseHistoryTransactionItemResponse,
    PositionResponse,
    PieRequest,
    AccountBucketDetailedResponse,
    DuplicateBucketRequest,
    PublicReportRequest,
    ReportResponse,
    EnqueuedReportResponse,
)

T = TypeVar("T")


class Trading212Client:
    client: requests.Session | None = None
    base_url: str = f"https://{config.T212_ENVIRONMENT}.trading212.com/api/v0/equity"
    headers: dict[str, str] = {
        "Authorization": config.T212_API_KEY,
        "Content-Type": "application/json",
    }

    @classmethod
    def init_client(cls) -> requests.Session:
        if cls.client is None:
            cls.client = requests.Session()
        return cls.client

    @classmethod
    def close_client(cls) -> None:
        if cls.client is not None:
            cls.client.close()
            cls.client = None

    @classmethod
    def get(
        cls, url_suffix: str, params: dict[str | str] | None, response_type: type[T]
    ):
        client = cls.init_client()
        url = f"{cls.base_url}/{url_suffix}"

        with client.get(f"{url}", params=params, headers=cls.headers) as response:
            response.raise_for_status()
            return response_type.model_validate(response.json())

    @classmethod
    def post(
        cls, url_suffix: str, data: dict[str | str] | None, response_type: type[T]
    ):
        client = cls.init_client()
        url = f"{cls.base_url}/{url_suffix}"

        with client.post(f"{url}", json=data, headers=cls.headers) as response:
            response.raise_for_status()
            return response_type.model_validate(response.json())

    @classmethod
    def exchange_list(cls) -> ExchangeResponse:
        url = "metadata/exchanges"
        return cls.get(url, None, ExchangeResponse)

    @classmethod
    def instrument_list(cls) -> InstrumentListResponse:
        url = "metadata/instruments"
        return cls.get(url, None, InstrumentListResponse)

    @classmethod
    def fetch_all_pies(cls) -> FetchAllPiesResponse:
        url = "pies"
        return cls.get(url, None, FetchAllPiesResponse)

    @classmethod
    def fetch_a_pie(cls, pie_id: int) -> FetchAPieResponse:
        url = f"pies/{pie_id}"
        return cls.get(url, None, FetchAPieResponse)

    @classmethod
    def fetch_all_equity_orders(cls) -> FetchAllEquityOrdersResponse:
        url = "orders"
        return cls.get(url, None, FetchAllEquityOrdersResponse)

    @classmethod
    def fetch_by_id(cls, order_id: int) -> Order:
        url = f"orders/{order_id}"
        return cls.get(url, None, Order)

    @classmethod
    def fetch_account_summary(cls) -> AccountSummary:
        url = "account/summary"
        return cls.get(url, None, AccountSummary)

    @classmethod
    def fetch_all_open_positions(cls, ticker: str | None = None) -> PositionResponse:
        url = "positions"
        params = {}
        if ticker is not None:
            params["ticker"] = ticker
        return cls.get(url, params, PositionResponse)

    @classmethod
    def search_position_by_ticker(
        cls,
        ticker: str,
    ) -> PositionResponse:
        url = "positions"
        params = {"ticker": ticker}
        return cls.get(url, params, PositionResponse)

    @classmethod
    def cancel_order(cls, order_id: int) -> None:
        client = cls.init_client()
        url = f"{cls.base_url}/orders/{order_id}"
        with client.delete(url, headers=cls.headers) as response:
            response.raise_for_status()

    @classmethod
    def create_pie(cls, pie_request: PieRequest) -> AccountBucketDetailedResponse:
        url = "pies"
        return cls.post(
            url,
            pie_request.model_dump(mode="json", exclude_none=True),
            AccountBucketDetailedResponse,
        )

    @classmethod
    def delete_pie(cls, pie_id: int) -> None:
        client = cls.init_client()
        url = f"{cls.base_url}/pies/{pie_id}"
        with client.delete(url, headers=cls.headers) as response:
            response.raise_for_status()

    @classmethod
    def update_pie(
        cls, pie_id: int, pie_request: PieRequest
    ) -> AccountBucketDetailedResponse:
        client = cls.init_client()
        url = f"{cls.base_url}/pies/{pie_id}"
        with client.put(
            url,
            json=pie_request.model_dump(mode="json", exclude_none=True),
            headers=cls.headers,
        ) as response:
            response.raise_for_status()
            return AccountBucketDetailedResponse.model_validate(response.json())

    @classmethod
    def duplicate_pie(
        cls, pie_id: int, duplicate_request: DuplicateBucketRequest
    ) -> AccountBucketDetailedResponse:
        url = f"pies/{pie_id}/duplicate"
        return cls.post(
            url,
            duplicate_request.model_dump(mode="json", exclude_none=True),
            AccountBucketDetailedResponse,
        )

    @classmethod
    def list_generated_reports(cls) -> List[ReportResponse]:
        client = cls.init_client()
        url = f"{cls.base_url}/history/exports"
        with client.get(url, headers=cls.headers) as response:
            response.raise_for_status()
            items = response.json()
            return [ReportResponse.model_validate(item) for item in items]

    @classmethod
    def request_csv_report(
        cls, public_report_request: PublicReportRequest
    ) -> EnqueuedReportResponse:
        url = "history/exports"
        return cls.post(
            url,
            public_report_request.model_dump(mode="json", exclude_none=True),
            EnqueuedReportResponse,
        )

    @classmethod
    def historical_order_data(
        cls, cursor: int, ticker: str | None, limit: int = 20
    ) -> PaginatedResponseHistoricalOrderResponse:
        url = "history/orders"
        params = {"cursor": cursor, "limit": limit}
        if ticker is not None:
            params["ticker"] = ticker
        return cls.get(url, params, PaginatedResponseHistoricalOrderResponse)

    @classmethod
    def paid_out_dividends(
        cls, cursor: int, ticker: str, limit: int = 20
    ) -> PaginatedResponseHistoryDividendItemResponse:
        url = "history/dividends"
        params = {"cursor": cursor, "ticker": ticker, "limit": limit}
        return cls.get(url, params, PaginatedResponseHistoryDividendItemResponse)

    @classmethod
    def transactions_list(
        cls, cursor: int, ticker: str, limit: int = 20
    ) -> PaginatedResponseHistoryTransactionItemResponse:
        url = "history/transactions"
        params = {"cursor": cursor, "ticker": ticker, "limit": limit}
        return cls.get(url, params, PaginatedResponseHistoryTransactionItemResponse)

    @classmethod
    def place_limit_order(
        cls,
        limit_price: float,
        quantity: float,
        ticker: str,
        time_validity: LimitRequestTimeValidity,
    ) -> Order:
        """Returns 403 forbidden"""
        url = "orders/limit"
        json_data = {
            "limitPrice": limit_price,
            "quantity": quantity,
            "ticker": ticker,
            "timeValidity": time_validity,
        }
        return cls.post(url, json_data, Order)

    @classmethod
    @not_implemented_api_field
    def place_market_order(
        cls,
        quantity: float,
        ticker: str,
    ) -> Order:
        """Returns 403 forbidden"""
        url = "orders/market"
        json_data = {
            "quantity": quantity,
            "ticker": ticker,
        }
        return cls.post(url, json_data, Order)

    @classmethod
    @not_implemented_api_field
    def place_stop_order(
        cls,
        limit_price: float,
        quantity: float,
        ticker: str,
        time_validity: LimitRequestTimeValidity,
    ) -> Order:
        """Returns 403 forbidden"""
        url = "orders/stop"
        json_data = {
            "limitPrice": limit_price,
            "quantity": quantity,
            "ticker": ticker,
            "timeValidity": time_validity,
        }
        return cls.post(url, json_data, Order)

    @classmethod
    @not_implemented_api_field
    def place_stop_limit_order(
        cls,
        limit_price: float,
        quantity: float,
        stop_price: float,
        ticker: str,
        time_validity: LimitRequestTimeValidity,
    ) -> Order:
        """Returns 403 forbidden"""
        url = "orders/stop_limit"
        json_data = {
            "limitPrice": limit_price,
            "quantity": quantity,
            "stopPrice": stop_price,
            "ticker": ticker,
            "timeValidity": time_validity,
        }
        return cls.post(url, json_data, Order)


if __name__ == "__main__":
    print(
        Trading212Client.place_limit_order(1, 1, "sfsdfs", LimitRequestTimeValidity.DAY)
    )
