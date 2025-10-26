from typing import Optional
import os
from coinbase.rest import RESTClient
from src.config.settings import AppSettings
from src.utils.logger import setup_logger


logger = setup_logger(__name__)


def create_coinbase_client(settings: AppSettings) -> RESTClient:
    api_key = settings.coinbase.api_key_id
    api_secret = settings.coinbase.api_secret
    key_file = settings.coinbase.key_file_path
    base_url = settings.coinbase.api_base

    # If a key file is provided, must NOT pass api_secret; SDK forbids both
    if key_file and os.path.exists(key_file):
        logger.info("Initializing Coinbase RESTClient with key_file only")
        return RESTClient(key_file=key_file, base_url=base_url)

    if api_key and api_secret:
        logger.info("Initializing Coinbase RESTClient with API key and secret")
        return RESTClient(api_key=api_key, api_secret=api_secret, base_url=base_url)

    logger.info("Initializing Coinbase RESTClient without credentials (public endpoints only)")
    return RESTClient(base_url=base_url)


def verify_connectivity(client: RESTClient) -> bool:
    try:
        _ = client.get_public_products()
        return True
    except Exception as exc:  # noqa: BLE001
        logger.error("Coinbase connectivity check failed: %s", exc)
        return False
