"""Convert API endpoints."""

from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from .rest_base import RESTBase


def create_convert_quote(
    self: "RESTBase",
    from_account: str,
    to_account: str,
    amount: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Create a convert quote between two accounts.
    
    Args:
        from_account: The source account ID
        to_account: The destination account ID
        amount: The amount to convert
        **kwargs: Additional parameters
        
    Returns:
        Dict containing quote information
    """
    data = {
        "from_account": from_account,
        "to_account": to_account,
        "amount": amount,
        **kwargs
    }
    return self.post("/api/v3/brokerage/convert/quote", data=data)


def get_convert_trade(self: "RESTBase", trade_id: str, **kwargs) -> Dict[str, Any]:
    """
    Get a convert trade by trade ID.
    
    Args:
        trade_id: The trade ID
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing trade information
    """
    return self.get(f"/api/v3/brokerage/convert/trade/{trade_id}", params=kwargs)


def commit_convert_trade(
    self: "RESTBase",
    trade_id: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Commit a convert trade.
    
    Args:
        trade_id: The trade ID to commit
        **kwargs: Additional parameters
        
    Returns:
        Dict containing committed trade information
    """
    data = {"trade_id": trade_id, **kwargs}
    return self.post(f"/api/v3/brokerage/convert/trade/{trade_id}", data=data)
