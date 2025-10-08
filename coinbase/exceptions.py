"""Custom exceptions for Coinbase SDK"""


class AuthenticationError(Exception):
    """Raised when authentication fails or is missing for private endpoints"""
    pass
