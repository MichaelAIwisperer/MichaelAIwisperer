"""Fees API endpoints."""

from typing import TYPE_CHECKING, Dict, Any, Optional

if TYPE_CHECKING:
    from .rest_base import RESTBase


def get_transaction_summary(
    self: "RESTBase",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    user_native_currency: Optional[str] = None,
    product_type: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Get transaction summary including fees.
    
    Args:
        start_date: Start date for the summary (ISO 8601 format)
        end_date: End date for the summary (ISO 8601 format)
        user_native_currency: User's native currency
        product_type: Type of product (e.g., 'SPOT', 'FUTURE')
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing transaction summary
    """
    params = {**kwargs}
    if start_date:
        params["start_date"] = start_date
    if end_date:
        params["end_date"] = end_date
    if user_native_currency:
        params["user_native_currency"] = user_native_currency
    if product_type:
        params["product_type"] = product_type
        
    return self.get("/api/v3/brokerage/transaction_summary", params=params)
