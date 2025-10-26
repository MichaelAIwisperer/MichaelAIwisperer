import logging
import os
from typing import Optional


def setup_logger(name: Optional[str] = None) -> logging.Logger:
    logger = logging.getLogger(name if name else __name__)
    if logger.handlers:
        return logger

    level = os.getenv("LOG_LEVEL", "INFO").upper()
    logger.setLevel(getattr(logging, level, logging.INFO))

    ch = logging.StreamHandler()
    ch.setLevel(getattr(logging, level, logging.INFO))
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)5s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
