import os
from dataclasses import dataclass
from dotenv import load_dotenv
from typing import Optional


@dataclass
class CoinbaseSettings:
    api_key_id: Optional[str]
    api_secret: Optional[str]
    key_file_path: Optional[str]
    api_base: str


@dataclass
class NewsSettings:
    reuters_api_key: Optional[str]
    wsj_api_key: Optional[str]
    seeking_alpha_api_key: Optional[str]


@dataclass
class TradingSettings:
    product_id: str
    base_currency: str
    quote_currency: str
    live_trading: bool
    dry_run: bool


@dataclass
class RLSettings:
    model_dir: str
    replay_capacity: int
    batch_size: int
    learning_rate: float
    gamma: float
    tau: float


@dataclass
class AppSettings:
    coinbase: CoinbaseSettings
    news: NewsSettings
    trading: TradingSettings
    rl: RLSettings
    candle_granularity: str
    candle_lookback_minutes: int


def load_settings(env_path: Optional[str] = None) -> AppSettings:
    if env_path:
        load_dotenv(env_path)
    else:
        load_dotenv()

    coinbase = CoinbaseSettings(
        api_key_id=os.getenv("COINBASE_API_KEY_ID"),
        api_secret=os.getenv("COINBASE_API_SECRET"),
        # Prefer JSON key file path; fall back to legacy private key path var if present
        key_file_path=os.getenv("COINBASE_KEY_FILE_PATH")
        or os.getenv("COINBASE_PRIVATE_KEY_PATH"),
        api_base=os.getenv("COINBASE_API_BASE", "api.coinbase.com"),
    )

    news = NewsSettings(
        reuters_api_key=os.getenv("REUTERS_API_KEY"),
        wsj_api_key=os.getenv("WSJ_API_KEY"),
        seeking_alpha_api_key=os.getenv("SEEKING_ALPHA_API_KEY"),
    )

    trading = TradingSettings(
        product_id=os.getenv("PRODUCT_ID", "BTC-USD"),
        base_currency=os.getenv("BASE_CURRENCY", "BTC"),
        quote_currency=os.getenv("QUOTE_CURRENCY", "USD"),
        live_trading=os.getenv("LIVE_TRADING", "false").lower() == "true",
        dry_run=os.getenv("DRY_RUN", "true").lower() == "true",
    )

    rl = RLSettings(
        model_dir=os.getenv("RL_MODEL_DIR", "models"),
        replay_capacity=int(os.getenv("RL_REPLAY_CAPACITY", "100000")),
        batch_size=int(os.getenv("RL_BATCH_SIZE", "64")),
        learning_rate=float(os.getenv("RL_LEARNING_RATE", "1e-4")),
        gamma=float(os.getenv("RL_GAMMA", "0.99")),
        tau=float(os.getenv("RL_TAU", "0.005")),
    )

    candle_granularity = os.getenv("CANDLE_GRANULARITY", "ONE_MINUTE")
    candle_lookback_minutes = int(os.getenv("CANDLE_LOOKBACK_MINUTES", "1440"))

    return AppSettings(
        coinbase=coinbase,
        news=news,
        trading=trading,
        rl=rl,
        candle_granularity=candle_granularity,
        candle_lookback_minutes=candle_lookback_minutes,
    )
