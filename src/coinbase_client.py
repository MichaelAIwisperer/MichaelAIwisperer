from typing import Optional
from coinbase.rest import RESTClient
from coinbase.constants import API_ENV_KEY, API_SECRET_ENV_KEY
import os


class CoinbaseClientFactory:
    @staticmethod
    def create(api_key: Optional[str], api_secret: Optional[str], base_url: str, timeout_seconds: int) -> RESTClient:
        # Prefer passing explicitly; package also reads env if None
        if api_key and api_secret:
            return RESTClient(api_key=api_key, api_secret=api_secret, base_url=base_url, timeout=timeout_seconds)

        # Fallback to environment variables
        os.environ.setdefault(API_ENV_KEY, api_key or "")
        os.environ.setdefault(API_SECRET_ENV_KEY, api_secret or "")
        return RESTClient(base_url=base_url, timeout=timeout_seconds)
