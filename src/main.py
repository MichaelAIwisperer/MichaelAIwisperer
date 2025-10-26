from src.config import get_settings
from src.coinbase_client import CoinbaseClientFactory
from src.data_sources.public_market import fetch_public_order_book, fetch_public_market_trades


def main() -> None:
    settings = get_settings()

    client = CoinbaseClientFactory.create(
        api_key=settings.coinbase_api_key or None,
        api_secret=settings.coinbase_api_secret or None,
        base_url=settings.coinbase_base_url,
        timeout_seconds=settings.coinbase_timeout_seconds,
    )

    ob = fetch_public_order_book(client, settings.product_id, limit=50)
    trades = fetch_public_market_trades(client, settings.product_id, limit=50)

    best_bid = getattr(trades, "best_bid", None)
    best_ask = getattr(trades, "best_ask", None)
    bid_count = len(getattr(ob.pricebook, "bids", []) if hasattr(ob, "pricebook") else [])
    ask_count = len(getattr(ob.pricebook, "asks", []) if hasattr(ob, "pricebook") else [])
    last_trade_price = trades.trades[0].price if getattr(trades, "trades", None) else None

    print({
        "best_bid": best_bid,
        "best_ask": best_ask,
        "bid_count": bid_count,
        "ask_count": ask_count,
        "last_trade_price": last_trade_price,
    })


if __name__ == "__main__":
    main()
