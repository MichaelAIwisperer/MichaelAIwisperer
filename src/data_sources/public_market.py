from typing import Dict, Any
from coinbase.rest import RESTClient


def fetch_public_order_book(client: RESTClient, product_id: str, limit: int = 50) -> Dict[str, Any]:
    return client.get_public_product_book(product_id=product_id, limit=limit)


def fetch_public_market_trades(client: RESTClient, product_id: str, limit: int = 100) -> Dict[str, Any]:
    return client.get_public_market_trades(product_id=product_id, limit=limit)
