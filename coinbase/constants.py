"""Constants for Coinbase SDK"""

API_ENV_KEY = "COINBASE_API_KEY"
API_SECRET_ENV_KEY = "COINBASE_API_SECRET"
BASE_URL = "api.coinbase.com"
USER_AGENT = "coinbase-python-sdk/0.1.0"

RATE_LIMIT_HEADERS = [
    "X-RateLimit-Limit",
    "X-RateLimit-Remaining",
    "X-RateLimit-Reset",
]
