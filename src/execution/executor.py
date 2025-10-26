import uuid
from dataclasses import dataclass
from typing import Optional

from coinbase.rest import RESTClient
from src.utils.logger import setup_logger


logger = setup_logger(__name__)


@dataclass
class OrderResult:
    success: bool
    order_id: Optional[str]
    error: Optional[str]


def place_market_order(
    client: RESTClient,
    product_id: str,
    side: str,
    base_size: Optional[str] = None,
    quote_size: Optional[str] = None,
) -> OrderResult:
    client_order_id = str(uuid.uuid4())
    try:
        resp = client.market_order(
            client_order_id=client_order_id,
            product_id=product_id,
            side=side,
            base_size=base_size,
            quote_size=quote_size,
        )
        return OrderResult(success=True, order_id=resp.order_id, error=None)  # type: ignore[attr-defined]
    except Exception as exc:  # noqa: BLE001
        logger.error("Market order failed: %s", exc)
        return OrderResult(success=False, order_id=None, error=str(exc))


def place_bracket_order_gtc(
    client: RESTClient,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
) -> OrderResult:
    client_order_id = str(uuid.uuid4())
    try:
        resp = client.trigger_bracket_order_gtc(
            client_order_id=client_order_id,
            product_id=product_id,
            side=side,
            base_size=base_size,
            limit_price=limit_price,
            stop_trigger_price=stop_trigger_price,
        )
        return OrderResult(success=True, order_id=resp.order_id, error=None)  # type: ignore[attr-defined]
    except Exception as exc:  # noqa: BLE001
        logger.error("Bracket order failed: %s", exc)
        return OrderResult(success=False, order_id=None, error=str(exc))
