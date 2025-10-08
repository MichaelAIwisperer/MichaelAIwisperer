"""Base class for Coinbase REST API client."""

import json
import time
from typing import Any, Dict, Optional, Union, IO
import hmac
import hashlib
import requests
from urllib.parse import urljoin


class RESTBase:
    """Base class for Coinbase REST API interactions."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        key_file: Optional[Union[IO, str]] = None,
        base_url: str = "https://api.coinbase.com",
        timeout: Optional[int] = 30,
        verbose: bool = False,
        rate_limit_headers: bool = False,
    ):
        """
        Initialize REST base client.

        Args:
            api_key: The API key
            api_secret: The API key secret
            key_file: Path to API key file or file-like object
            base_url: The base URL for REST requests
            timeout: Set timeout in seconds for REST requests
            verbose: Enables debug logging
            rate_limit_headers: Enables rate limit headers
        """
        self.base_url = base_url
        self.timeout = timeout
        self.verbose = verbose
        self.rate_limit_headers = rate_limit_headers
        self.session = requests.Session()

        # Handle API credentials
        if key_file:
            self._load_key_file(key_file)
        else:
            self.api_key = api_key
            self.api_secret = api_secret

    def _load_key_file(self, key_file: Union[IO, str]) -> None:
        """Load API key from file."""
        if isinstance(key_file, str):
            with open(key_file, 'r') as f:
                data = json.load(f)
        else:
            data = json.load(key_file)
        
        self.api_key = data.get('api_key')
        self.api_secret = data.get('api_secret')

    def _generate_signature(
        self, timestamp: str, method: str, path: str, body: str = ""
    ) -> str:
        """Generate HMAC signature for authenticated requests."""
        if not self.api_secret:
            raise ValueError("API secret is required for authenticated requests")
        
        message = f"{timestamp}{method}{path}{body}"
        signature = hmac.new(
            self.api_secret.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        return signature

    def _get_headers(
        self, method: str, path: str, body: Optional[Dict[str, Any]] = None
    ) -> Dict[str, str]:
        """Generate headers for API request."""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        if self.api_key and self.api_secret:
            timestamp = str(int(time.time()))
            body_str = json.dumps(body) if body else ""
            signature = self._generate_signature(timestamp, method, path, body_str)
            
            headers.update({
                "CB-ACCESS-KEY": self.api_key,
                "CB-ACCESS-SIGN": signature,
                "CB-ACCESS-TIMESTAMP": timestamp,
            })

        return headers

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make HTTP request to API."""
        url = urljoin(self.base_url, endpoint)
        headers = self._get_headers(method, endpoint, data)

        if self.verbose:
            print(f"[{method}] {url}")
            if params:
                print(f"Params: {params}")
            if data:
                print(f"Data: {data}")

        response = self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data,
            timeout=self.timeout,
        )

        if self.rate_limit_headers:
            rate_limit_info = {
                "limit": response.headers.get("X-RateLimit-Limit"),
                "remaining": response.headers.get("X-RateLimit-Remaining"),
                "reset": response.headers.get("X-RateLimit-Reset"),
            }
            if self.verbose:
                print(f"Rate Limit Info: {rate_limit_info}")

        response.raise_for_status()
        return response.json() if response.text else {}

    def get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make GET request."""
        return self._request("GET", endpoint, params=params)

    def post(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make POST request."""
        return self._request("POST", endpoint, params=params, data=data)

    def put(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make PUT request."""
        return self._request("PUT", endpoint, params=params, data=data)

    def delete(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make DELETE request."""
        return self._request("DELETE", endpoint, params=params)
