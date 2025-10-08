"""Market Data API endpoints."""

from typing import TYPE_CHECKING, Dict, Any, Optional

if TYPE_CHECKING:
    from .rest_base import RESTBase


def get_candles(
    self: "RESTBase",
    product_id: str,
    start: str,
    end: str,
    granularity: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Get candles (OHLCV data) for a product.
    
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
    return self.get(f"/api/v3/brokerage/products/{product_id}/candles", params=params)


def get_market_trades(
    self: "RESTBase",
    product_id: str,
    limit: Optional[int] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Get market trades for a product.
    
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
        
    return self.get(f"/api/v3/brokerage/products/{product_id}/ticker", params=params)
