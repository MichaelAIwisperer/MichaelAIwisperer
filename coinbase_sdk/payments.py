"""Payments API endpoints."""

from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from .rest_base import RESTBase


def list_payment_methods(self: "RESTBase", **kwargs) -> Dict[str, Any]:
    """
    List payment methods.
    
    Args:
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing list of payment methods
    """
    return self.get("/api/v3/brokerage/payment_methods", params=kwargs)


def get_payment_method(
    self: "RESTBase",
    payment_method_id: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Get a specific payment method.
    
    Args:
        payment_method_id: The payment method ID
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing payment method information
    """
    return self.get(f"/api/v3/brokerage/payment_methods/{payment_method_id}", params=kwargs)
