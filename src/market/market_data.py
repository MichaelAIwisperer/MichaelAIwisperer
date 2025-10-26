from datetime import datetime, timedelta, timezone
from typing import List, Dict, Any

from coinbase.rest import RESTClient
from src.utils.logger import setup_logger


logger = setup_logger(__name__)


ISO8601 = "%Y-%m-%dT%H:%M:%SZ"


def isoformat(dt: datetime) -> str:
    return dt.strftime(ISO8601)


def epoch_seconds(dt: datetime) -> str:
    return str(int(dt.timestamp()))


def _granularity_to_minutes(granularity: str) -> int:
    mapping = {
        "ONE_MINUTE": 1,
        "FIVE_MINUTE": 5,
        "FIFTEEN_MINUTE": 15,
        "THIRTY_MINUTE": 30,
        "ONE_HOUR": 60,
        "TWO_HOUR": 120,
        "SIX_HOUR": 360,
        "ONE_DAY": 1440,
    }
    return mapping.get(granularity, 1)


def fetch_public_candles(
    client: RESTClient,
    product_id: str,
    minutes_lookback: int,
    granularity: str,
) -> List[Dict[str, Any]]:
    # Use Coinbase server time to avoid clock skew
    server_time = client.get_unix_time()
    server_now = (
        datetime.strptime(server_time.iso, ISO8601).replace(tzinfo=timezone.utc)
        if getattr(server_time, "iso", None)
        else datetime.now(timezone.utc)
    )

    # Align to minute boundary and keep end strictly < server time
    end = server_now.replace(second=0, microsecond=0) - timedelta(minutes=1)
    total_minutes = max(1, minutes_lookback)
    gran_minutes = _granularity_to_minutes(granularity)
    max_points = 300
    chunk_minutes = max_points * gran_minutes

    candles_all: list[dict[str, Any]] = []

    remaining = total_minutes
    current_end = end
    while remaining > 0:
        window = min(remaining, chunk_minutes)
        start = current_end - timedelta(minutes=window)
        # Ensure alignment to granularity boundary
        if gran_minutes > 1:
            # snap start to multiple of granularity minutes
            start_minute = (start.minute // gran_minutes) * gran_minutes
            start = start.replace(minute=start_minute, second=0, microsecond=0)

        logger.info(
            "Fetching candles product=%s start=%s end=%s granularity=%s (window=%s)",
            product_id,
            epoch_seconds(start),
            epoch_seconds(current_end),
            granularity,
            window,
        )

        # Coinbase public candles require epoch seconds for start/end
        resp = client.get_public_candles(
            product_id=product_id,
            start=epoch_seconds(start),
            end=epoch_seconds(current_end),
            granularity=granularity,
            limit=max_points,
        )
        candles_chunk = getattr(resp, "candles", []) or []
        # Convert Candle objects to dicts uniformly
        normalized = [vars(c) if hasattr(c, "__dict__") else c for c in candles_chunk]
        candles_all.extend(normalized)

        remaining -= window
        current_end = start

    return candles_all


def fetch_order_book(
    client: RESTClient,
    product_id: str,
    limit: int | None = None,
    agg_increment: str | None = None,
):
    logger.info(
        "Fetching order book product=%s limit=%s agg=%s", product_id, limit, agg_increment
    )
    return client.get_public_product_book(
        product_id=product_id,
        limit=limit,
        aggregation_price_increment=agg_increment,
    )


def fetch_best_bid_ask(client: RESTClient, product_id: str):
    # Public endpoint alternative: use ticker to get best bid/ask
    # limit 1 is sufficient for snapshot; returns best_bid/best_ask
    return client.get_public_market_trades(product_id=product_id, limit=1)
