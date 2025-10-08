import time
from typing import Callable

from coinbase.rest import RESTClient

from .strategy.base import Strategy


def run_strategy(
    client: RESTClient,
    strategy: Strategy,
    product_id: str,
    interval_seconds: float = 2.0,
    max_ticks: int = 50,
) -> None:
    """Simple polling runner that feeds last-trade price into the strategy."""
    ticks = 0
    while ticks < max_ticks:
        trades = client.get_public_market_trades(product_id=product_id, limit=1)
        if trades.trades:
            last = trades.trades[0]
            snapshot = {"price": float(last.price), "time": last.time, "side": last.side}
            strategy.on_tick(snapshot)
        ticks += 1
        time.sleep(interval_seconds)

