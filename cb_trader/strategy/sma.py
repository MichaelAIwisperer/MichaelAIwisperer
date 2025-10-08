from collections import deque
from typing import Deque, Dict, Any, Optional

from .base import Strategy


class SmaCrossoverStrategy(Strategy):
    def __init__(self, short_window: int = 5, long_window: int = 20) -> None:
        if short_window >= long_window:
            raise ValueError("short_window must be < long_window")
        self.short_window = short_window
        self.long_window = long_window
        self.short_prices: Deque[float] = deque(maxlen=short_window)
        self.long_prices: Deque[float] = deque(maxlen=long_window)
        self.position: Optional[str] = None

    def on_tick(self, market_snapshot: Dict[str, Any]) -> None:
        price = float(market_snapshot["price"])
        self.short_prices.append(price)
        self.long_prices.append(price)

        if len(self.short_prices) < self.short_window or len(self.long_prices) < self.long_window:
            return

        short_avg = sum(self.short_prices) / len(self.short_prices)
        long_avg = sum(self.long_prices) / len(self.long_prices)

        if self.position != "long" and short_avg > long_avg:
            # Signal: Golden cross
            self.position = "long"
            print(f"SIGNAL BUY at {price}")
        elif self.position == "long" and short_avg < long_avg:
            # Signal: Death cross
            self.position = None
            print(f"SIGNAL SELL at {price}")

