"""Base API class for Coinbase SDK"""

import logging
from typing import IO, Optional, Union


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance"""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


class APIBase:
    """Base class for API clients"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        key_file: Optional[Union[IO, str]] = None,
        base_url: str = "api.coinbase.com",
        timeout: Optional[int] = None,
        verbose: Optional[bool] = False,
    ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.key_file = key_file
        self.base_url = base_url
        self.timeout = timeout
        self.verbose = verbose

        # Handle key file if provided
        if key_file:
            if isinstance(key_file, str):
                with open(key_file, "r") as f:
                    self._load_key_file(f)
            else:
                self._load_key_file(key_file)

    def _load_key_file(self, file_obj: IO):
        """Load API credentials from a file"""
        import json

        data = json.load(file_obj)
        if not self.api_key:
            self.api_key = data.get("api_key")
        if not self.api_secret:
            self.api_secret = data.get("api_secret")

    @property
    def is_authenticated(self) -> bool:
        """Check if the client is authenticated"""
        return bool(self.api_key and self.api_secret)
