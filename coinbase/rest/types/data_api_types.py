"""Data API type definitions"""

from typing import Any, Dict, List, Optional


class GetAPIKeyPermissionsResponse:
    """Response object for Get API Key Permissions endpoint"""
    
    def __init__(self, response: Dict[str, Any]):
        """
        Initialize GetAPIKeyPermissionsResponse
        
        Args:
            response: Raw response dictionary from the API
        """
        self._raw_response = response
        self.permissions = response.get("permissions", [])
        self.portfolio_id = response.get("portfolio_id")
        self.portfolio_uuid = response.get("portfolio_uuid")
    
    @property
    def raw_response(self) -> Dict[str, Any]:
        """Get the raw API response"""
        return self._raw_response
    
    def __repr__(self) -> str:
        return f"GetAPIKeyPermissionsResponse(permissions={self.permissions}, portfolio_id={self.portfolio_id})"
