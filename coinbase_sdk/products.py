"""Products API endpoints."""

from typing import TYPE_CHECKING, Dict, Any, Optional

if TYPE_CHECKING:
    from .rest_base import RESTBase


def get_products(
    self: "RESTBase",
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    product_type: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Get list of products.
    
    Args:
        limit: Number of products to return
        offset: Offset for pagination
        product_type: Type of product (e.g., 'SPOT', 'FUTURE')
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing list of products
    """
    params = {**kwargs}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if product_type:
        params["product_type"] = product_type
        
    return self.get("/api/v3/brokerage/products", params=params)


def get_product(
    self: "RESTBase",
    product_id: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Get a specific product.
    
    Args:
        product_id: The product ID (e.g., 'BTC-USD')
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing product information
    """
    return self.get(f"/api/v3/brokerage/products/{product_id}", params=kwargs)


def get_product_book(
    self: "RESTBase",
    product_id: str,
    limit: Optional[int] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Get product order book.
    
    Args:
        product_id: The product ID (e.g., 'BTC-USD')
        limit: Number of bids/asks to return
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing product order book
    """
    params = {**kwargs}
    if limit is not None:
        params["limit"] = limit
        
    return self.get(f"/api/v3/brokerage/product_book", params={**params, "product_id": product_id})


def get_best_bid_ask(
    self: "RESTBase",
    product_ids: Optional[list] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Get best bid/ask for products.
    
    Args:
        product_ids: List of product IDs
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing best bid/ask information
    """
    params = {**kwargs}
    if product_ids:
        params["product_ids"] = ",".join(product_ids)
        
    return self.get("/api/v3/brokerage/best_bid_ask", params=params)
