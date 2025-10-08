from typing import Optional

from coinbase.rest import RESTClient
from coinbase.rest.types.orders_types import CreateOrderResponse, PreviewOrderResponse


def market_buy(
    client: RESTClient,
    product_id: str,
    quote_size: str,
    client_order_id: Optional[str] = None,
) -> CreateOrderResponse:
    return client.market_order_buy(
        product_id=product_id, quote_size=quote_size, client_order_id=client_order_id
    )


def market_sell(
    client: RESTClient,
    product_id: str,
    base_size: str,
    client_order_id: Optional[str] = None,
) -> CreateOrderResponse:
    return client.market_order_sell(
        product_id=product_id, base_size=base_size, client_order_id=client_order_id
    )


def preview_market_buy(
    client: RESTClient,
    product_id: str,
    quote_size: Optional[str] = None,
    base_size: Optional[str] = None,
) -> PreviewOrderResponse:
    return client.preview_market_order_buy(
        product_id=product_id, quote_size=quote_size, base_size=base_size
    )


def preview_market_sell(
    client: RESTClient,
    product_id: str,
    base_size: str,
) -> PreviewOrderResponse:
    return client.preview_market_order_sell(product_id=product_id, base_size=base_size)

