"""REST Client for Coinbase API"""

from typing import Any, Dict, Optional

from coinbase.constants import API_PREFIX
from coinbase.rest.types.data_api_types import GetAPIKeyPermissionsResponse


class RESTClient:
    """Coinbase REST API Client"""
    
    def __init__(self, api_key: str, api_secret: str, base_url: str = "https://api.coinbase.com"):
        """
        Initialize the REST client
        
        Args:
            api_key: Your Coinbase API key
            api_secret: Your Coinbase API secret
            base_url: Base URL for the API (default: https://api.coinbase.com)
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
    
    def get(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """
        Perform a GET request to the API
        
        Args:
            endpoint: API endpoint path
            **kwargs: Additional arguments for the request
            
        Returns:
            Response dictionary from the API
        """
        # This is a placeholder implementation
        # In a real implementation, this would make an actual HTTP request
        import requests
        
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, **kwargs)
        response.raise_for_status()
        return response.json()
    
    def get_api_key_permissions(
        self,
        **kwargs,
    ) -> GetAPIKeyPermissionsResponse:
        """
        **Get Api Key Permissions**
        _____________________________

        [GET] https://api.coinbase.com/api/v3/brokerage/key_permissions

        __________

        **Description:**

        Get information about your CDP API key permissions

        __________

        **Read more on the official documentation:** [Get API Key Permissions](https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getapikeypermissions)
        """
        endpoint = f"{API_PREFIX}/key_permissions"

        return GetAPIKeyPermissionsResponse(self.get(endpoint, **kwargs))
