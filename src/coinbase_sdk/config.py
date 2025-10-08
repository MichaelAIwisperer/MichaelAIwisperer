from dataclasses import dataclass
import os
from typing import Optional

def _parse_bool(value: Optional[str], default: bool = False) -> bool:
    if value is None:
        return default
    value_lower = value.strip().lower()
    return value_lower in {"1", "true", "yes", "y", "on"}

@dataclass
class SDKConfig:
    api_key: Optional[str]
    api_secret: Optional[str]
    base_url: str
    timeout_seconds: int
    verbose_logging: bool
    rate_limit_headers: bool

def load_config_from_env() -> SDKConfig:
    return SDKConfig(
        api_key=os.getenv("COINBASE_API_KEY"),
        api_secret=os.getenv("COINBASE_API_SECRET"),
        base_url=os.getenv("COINBASE_BASE_URL", "https://api.coinbase.com"),
        timeout_seconds=int(os.getenv("REQUEST_TIMEOUT_SECONDS", "30")),
        verbose_logging=_parse_bool(os.getenv("VERBOSE_LOGGING"), False),
        rate_limit_headers=_parse_bool(os.getenv("RATE_LIMIT_HEADERS"), False),
    )
