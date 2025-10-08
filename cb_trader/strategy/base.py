from abc import ABC, abstractmethod
from typing import Any, Dict


class Strategy(ABC):
    @abstractmethod
    def on_tick(self, market_snapshot: Dict[str, Any]) -> None:
        """Handle a new market snapshot. Implement trading logic here."""
        raise NotImplementedError

