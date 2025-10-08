from typing import List

from coinbase.rest import RESTClient


def list_top_products(client: RESTClient, limit: int = 10) -> List[str]:
    products = client.get_public_products(limit=limit)
    return [p.product_id for p in products.products]

