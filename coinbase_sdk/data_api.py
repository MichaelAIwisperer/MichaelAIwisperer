"""Data API endpoints."""

from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from .rest_base import RESTBase


def get_api_key_permissions(self: "RESTBase", **kwargs) -> Dict[str, Any]:
    """
    Get permissions for the current API key.
    
    Args:
        **kwargs: Additional query parameters
        
    Returns:
        Dict containing API key permissions
    """
    return self.get("/api/v3/brokerage/key_permissions", params=kwargs)
