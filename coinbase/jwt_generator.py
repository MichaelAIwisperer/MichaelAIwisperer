import base64
import hmac
import json
import time
from hashlib import sha256
from typing import Any


def _base64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def build_rest_jwt(uri: str, api_key: str, api_secret: str, now_s: int | None = None) -> str:
    """
    Build a minimal HS256 JWT for Coinbase Advanced Trade REST.

    Header: { "alg": "HS256", "typ": "JWT" }
    Payload includes: iss (api key), nbf/iat (now), exp (now+120s), sub (uri)
    Signature: HMAC-SHA256 over base64url(header).base64url(payload) using api_secret
    """
    if now_s is None:
        now_s = int(time.time())

    header: dict[str, Any] = {"alg": "HS256", "typ": "JWT"}
    payload: dict[str, Any] = {
        "iss": api_key,
        "nbf": now_s,
        "iat": now_s,
        "exp": now_s + 120,
        "sub": uri,
    }

    header_b64 = _base64url_encode(json.dumps(header, separators=(",", ":")).encode("utf-8"))
    payload_b64 = _base64url_encode(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    signing_input = f"{header_b64}.{payload_b64}".encode("ascii")
    signature = hmac.new(api_secret.encode("utf-8"), signing_input, sha256).digest()
    signature_b64 = _base64url_encode(signature)
    return f"{header_b64}.{payload_b64}.{signature_b64}"

