import os
import sys
from datetime import datetime, timedelta, timezone

from coinbase.rest import RESTClient


def main() -> int:
    api_key = os.getenv("COINBASE_API_KEY")
    api_secret = os.getenv("COINBASE_API_SECRET")

    # Instantiate client: works for public endpoints without credentials.
    # If api_key and api_secret are provided, authenticated methods are available too.
    client = RESTClient(api_key=api_key, api_secret=api_secret)

    # 1) Server time (public)
    server_time = client.get_unix_time()
    print("Server time:", server_time)

    # 2) List public products (public)
    products = client.get_public_products(limit=10)
    print("Products (first 10):", [p["product_id"] for p in products.get("products", [])])

    # Choose a product for subsequent calls. Default to BTC-USD if present.
    product_id = next(
        (p["product_id"] for p in products.get("products", []) if p.get("product_id") == "BTC-USD"),
        (products.get("products", [{}])[0].get("product_id") if products.get("products") else "BTC-USD"),
    )
    print("Using product:", product_id)

    # 3) Best bid/ask (public)
    bba = client.get_best_bid_ask(product_ids=[product_id])
    print("Best bid/ask:", bba)

    # 4) Order book (public)
    book = client.get_public_product_book(product_id=product_id, limit=10)
    print("Top-of-book bids/asks counts:", len(book.get("bids", [])), len(book.get("asks", [])))

    # 5) Market trades (public)
    trades = client.get_public_market_trades(product_id=product_id, limit=10)
    print("Recent trades count:", len(trades.get("trades", [])))

    # 6) Candles (public) — past 1 hour of 1m candles
    end_dt = datetime.now(timezone.utc).replace(microsecond=0)
    start_dt = end_dt - timedelta(hours=1)
    candles = client.get_public_candles(
        product_id=product_id,
        start=start_dt.isoformat().replace("+00:00", "Z"),
        end=end_dt.isoformat().replace("+00:00", "Z"),
        granularity="ONE_MINUTE",
        limit=60,
    )
    print("Candles fetched:", len(candles.get("candles", [])))

    # 7) Optional authenticated example: list accounts if creds are set
    if api_key and api_secret:
        try:
            accounts = client.get_accounts()
            print("Accounts fetched:", len(accounts.get("accounts", [])))
        except Exception as exc:
            print("Authenticated call failed:", exc)

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

