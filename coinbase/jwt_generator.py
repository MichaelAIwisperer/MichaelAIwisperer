"""JWT token generation for Coinbase API authentication"""

import time
from typing import Optional

try:
    import jwt
except ImportError:
    jwt = None


def build_rest_jwt(uri: str, api_key: str, api_secret: str) -> str:
    """
    Build a JWT token for REST API authentication
    
    Args:
        uri: The request URI in format "METHOD host/path"
        api_key: The API key
        api_secret: The API secret
        
    Returns:
        JWT token string
    """
    if jwt is None:
        raise ImportError(
            "PyJWT is required for authentication. Install it with: pip install PyJWT"
        )

    current_time = int(time.time())
    
    payload = {
        "sub": api_key,
        "iss": "coinbase-cloud",
        "nbf": current_time,
        "exp": current_time + 120,  # Token expires in 2 minutes
        "uri": uri,
    }

    return jwt.encode(payload, api_secret, algorithm="ES256")
