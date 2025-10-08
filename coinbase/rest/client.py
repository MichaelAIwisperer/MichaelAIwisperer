from typing import Any, Dict, List, Optional

from coinbase.constants import API_PREFIX
from coinbase.rest_base import RESTBase


# Lightweight response wrappers (identity wrappers for now)
class GetServerTimeResponse(dict):
    pass


class GetProductBookResponse(dict):
    pass


class ListProductsResponse(dict):
    pass


class GetProductResponse(dict):
    pass


class GetProductCandlesResponse(dict):
    pass


class GetMarketTradesResponse(dict):
    pass


class RESTClient(RESTBase):
    def get_unix_time(self, **kwargs) -> GetServerTimeResponse:
        endpoint = f"{API_PREFIX}/time"
        return GetServerTimeResponse(self.get(endpoint, public=True, **kwargs))

    def get_public_product_book(
        self,
        product_id: str,
        limit: Optional[int] = None,
        aggregation_price_increment: Optional[str] = None,
        **kwargs,
    ) -> GetProductBookResponse:
        endpoint = f"{API_PREFIX}/market/product_book"
        params = {
            "product_id": product_id,
            "limit": limit,
            "aggregation_price_increment": aggregation_price_increment,
        }
        return GetProductBookResponse(
            self.get(endpoint, params=params, public=True, **kwargs)
        )

    def get_public_products(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        product_type: Optional[str] = None,
        product_ids: Optional[List[str]] = None,
        contract_expiry_type: Optional[str] = None,
        expiring_contract_status: Optional[str] = None,
        get_all_products: bool = False,
        **kwargs,
    ) -> ListProductsResponse:
        endpoint = f"{API_PREFIX}/market/products"
        params = {
            "limit": limit,
            "offset": offset,
            "product_type": product_type,
            "product_ids": product_ids,
            "contract_expiry_type": contract_expiry_type,
            "expiring_contract_status": expiring_contract_status,
            "get_all_products": get_all_products,
        }
        return ListProductsResponse(
            self.get(endpoint, params=params, public=True, **kwargs)
        )

    def get_public_product(self, product_id: str, **kwargs) -> GetProductResponse:
        endpoint = f"{API_PREFIX}/market/products/{product_id}"
        return GetProductResponse(self.get(endpoint, public=True, **kwargs))

    def get_public_candles(
        self,
        product_id: str,
        start: str,
        end: str,
        granularity: str,
        limit: Optional[int] = None,
        **kwargs,
    ) -> GetProductCandlesResponse:
        endpoint = f"{API_PREFIX}/market/products/{product_id}/candles"
        params = {"start": start, "end": end, "granularity": granularity, "limit": limit}
        return GetProductCandlesResponse(
            self.get(endpoint, params=params, public=True, **kwargs)
        )

    def get_public_market_trades(
        self,
        product_id: str,
        limit: int,
        start: Optional[str] = None,
        end: Optional[str] = None,
        **kwargs,
    ) -> GetMarketTradesResponse:
        endpoint = f"{API_PREFIX}/market/products/{product_id}/ticker"
        params = {"limit": limit, "start": start, "end": end}
        return GetMarketTradesResponse(
            self.get(endpoint, params=params, public=True, **kwargs)
        )

