from .rest_base import RESTBase


class RESTClient(RESTBase):
    """
    RESTClient
    _____________________________

    Initialize using RESTClient

    Parameters:
      - api_key | Optional (str) - The API key
      - api_secret | Optional (str) - The API key secret
      - base_url | (str) - Base URL for REST requests. Default: https://api.coinbase.com
      - timeout_seconds | Optional (int) - Timeout in seconds for REST requests
      - verbose_logging | Optional (bool) - Enables debug logging. Default: False
      - rate_limit_headers | Optional (bool) - Enables rate limit headers. Default: False
    """

    # API method groups will be added incrementally (accounts, orders, market data, etc.).
    pass
