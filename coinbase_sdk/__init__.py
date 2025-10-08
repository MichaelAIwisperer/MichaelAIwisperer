"""Coinbase SDK - Python client for Coinbase API."""

from .rest_client import RESTClient
from .rest_base import RESTBase

__version__ = "1.0.0"
__all__ = ["RESTClient", "RESTBase"]
