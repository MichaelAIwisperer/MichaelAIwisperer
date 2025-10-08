"""Public API endpoints (no authentication required)."""

from typing import TYPE_CHECKING, Dict, Any, Optional

if TYPE_CHECKING:
    from .rest_base import RESTBase


def get_unix_time(self: "RESTBase", **kwargs) -> Dict[str, Any]:
    """
    Get the current Unix time from the server.
    
    Args:
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing Unix time
    """
    return self.get("/api/v3/brokerage/time", params=kwargs)


def get_public_products(
    self: "RESTBase",
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    product_type: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Get list of public products (no authentication required).
    
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
        
    return self.get("/api/v3/brokerage/market/products", params=params)


def get_public_product(
    self: "RESTBase",
    product_id: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Get a specific public product (no authentication required).
    
    Args:
        product_id: The product ID (e.g., 'BTC-USD')
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing product information
    """
    return self.get(f"/api/v3/brokerage/market/products/{product_id}", params=kwargs)


def get_public_product_book(
    self: "RESTBase",
    product_id: str,
    limit: Optional[int] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Get public product order book (no authentication required).
    
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
        
    return self.get(f"/api/v3/brokerage/market/product_book", params={**params, "product_id": product_id})


def get_public_candles(
    self: "RESTBase",
    product_id: str,
    start: str,
    end: str,
    granularity: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Get public candles (OHLCV data) for a product (no authentication required).
    
    Args:
        product_id: The product ID (e.g., 'BTC-USD')
        start: Start time in ISO 8601 format
        end: End time in ISO 8601 format
        granularity: Granularity (e.g., 'ONE_MINUTE', 'FIVE_MINUTE', 'ONE_HOUR', 'ONE_DAY')
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing candle data
    """
    params = {
        "start": start,
        "end": end,
        "granularity": granularity,
        **kwargs
    }
    return self.get(f"/api/v3/brokerage/market/products/{product_id}/candles", params=params)


def get_public_market_trades(
    self: "RESTBase",
    product_id: str,
    limit: Optional[int] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Get public market trades for a product (no authentication required).
    
    Args:
        product_id: The product ID (e.g., 'BTC-USD')
        limit: Number of trades to return
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing market trades
    """
    params = {**kwargs}
    if limit is not None:
        params["limit"] = limit
        
    return self.get(f"/api/v3/brokerage/market/products/{product_id}/ticker", params=params)
