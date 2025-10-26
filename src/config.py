import os
from dataclasses import dataclass
from dotenv import load_dotenv


def str_to_bool(value: str) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


@dataclass
class Settings:
    coinbase_api_key: str
    coinbase_api_secret: str
    coinbase_base_url: str = "api.coinbase.com"
    coinbase_timeout_seconds: int = 30

    reuters_api_key: str | None = None
    wsj_api_key: str | None = None
    seeking_alpha_api_key: str | None = None

    product_id: str = "BTC-USD"
    paper_trading: bool = True
    take_profit_pct: float = 0.02
    stop_loss_pct: float = 0.01
    max_position_usd: float = 100.0


def get_settings() -> Settings:
    load_dotenv(override=False)

    return Settings(
        coinbase_api_key=os.getenv("COINBASE_API_KEY", ""),
        coinbase_api_secret=os.getenv("COINBASE_API_SECRET", ""),
        coinbase_base_url=os.getenv("COINBASE_BASE_URL", "api.coinbase.com"),
        coinbase_timeout_seconds=int(os.getenv("COINBASE_TIMEOUT_SECONDS", "30")),
        reuters_api_key=os.getenv("REUTERS_API_KEY"),
        wsj_api_key=os.getenv("WSJ_API_KEY"),
        seeking_alpha_api_key=os.getenv("SEEKING_ALPHA_API_KEY"),
        product_id=os.getenv("PRODUCT_ID", "BTC-USD"),
        paper_trading=str_to_bool(os.getenv("PAPER_TRADING", "true")),
        take_profit_pct=float(os.getenv("TAKE_PROFIT_PCT", "0.02")),
        stop_loss_pct=float(os.getenv("STOP_LOSS_PCT", "0.01")),
        max_position_usd=float(os.getenv("MAX_POSITION_USD", "100.0")),
    )
