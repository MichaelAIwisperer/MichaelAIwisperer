"""Accounts API endpoints."""

from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from .rest_base import RESTBase


def get_accounts(self: "RESTBase", **kwargs) -> Dict[str, Any]:
    """
    Get a list of authenticated accounts for the current user.
    
    Args:
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing accounts information
    """
    return self.get("/api/v3/brokerage/accounts", params=kwargs)


def get_account(self: "RESTBase", account_id: str, **kwargs) -> Dict[str, Any]:
    """
    Get information for a single account.
    
    Args:
        account_id: The account ID
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing account information
    """
    return self.get(f"/api/v3/brokerage/accounts/{account_id}", params=kwargs)
