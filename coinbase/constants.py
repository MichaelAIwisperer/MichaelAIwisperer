"""Constants for Coinbase Advanced Trade API."""

# Environment variable keys for API auth
API_ENV_KEY = "COINBASE_API_KEY"
API_SECRET_ENV_KEY = "COINBASE_API_SECRET"

# Base host and API prefix (path only); requests will format as https://{BASE_URL}{path}
BASE_URL = "api.coinbase.com"
API_PREFIX = "/api/v3/brokerage"

# Headers to surface when rate_limit_headers=True
RATE_LIMIT_HEADERS = [
    "X-RateLimit-Limit",
    "X-RateLimit-Remaining",
    "X-RateLimit-Reset",
    "Retry-After",
]

# User-Agent string
USER_AGENT = "coinbase-python-client/0.1"

