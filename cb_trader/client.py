from coinbase.rest import RESTClient

from .config import AppConfig


def make_client(config: AppConfig) -> RESTClient:
    kwargs = {
        "timeout": config.timeout_seconds,
        "verbose": config.verbose,
    }

    # Only include auth via api_key/api_secret OR key_file when provided
    api_key = (config.api_key or "").strip()
    api_secret = (config.api_secret or "").strip()
    key_file = (config.api_key_file or "").strip()

    if key_file:
        kwargs["key_file"] = key_file
    elif api_key and api_secret:
        kwargs["api_key"] = api_key
        kwargs["api_secret"] = api_secret

    return RESTClient(**kwargs)

