from typing import List, Optional

from coinbase.rest import RESTClient


def list_top_products(client: RESTClient, limit: int = 10) -> List[str]:
    products = client.get_public_products(limit=limit)
    return [p.product_id for p in products.products]


def get_candles(
    client: RESTClient,
    product_id: str,
    start: str,
    end: str,
    granularity: str,
    limit: Optional[int] = None,
):
    return client.get_public_candles(
        product_id=product_id,
        start=start,
        end=end,
        granularity=granularity,
        limit=limit,
    )


def get_market_trades(
    client: RESTClient,
    product_id: str,
    limit: int,
    start: Optional[str] = None,
    end: Optional[str] = None,
):
    return client.get_public_market_trades(
        product_id=product_id,
        limit=limit,
        start=start,
        end=end,
    )

