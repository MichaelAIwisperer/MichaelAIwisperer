import logging
from typing import Optional, Union, IO


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


class APIBase:
    def __init__(
        self,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        key_file: Optional[Union[IO, str]] = None,
        base_url: str = "api.coinbase.com",
        timeout: Optional[int] = None,
        verbose: Optional[bool] = False,
    ) -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.key_file = key_file
        self.base_url = base_url
        self.timeout = timeout or 30
        self.verbose = bool(verbose)

    @property
    def is_authenticated(self) -> bool:
        return bool(self.api_key and self.api_secret)

