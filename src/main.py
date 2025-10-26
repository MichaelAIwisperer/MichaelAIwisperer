from src.config.settings import load_settings
from src.clients.coinbase_client import create_coinbase_client, verify_connectivity
from src.market.market_data import fetch_public_candles, fetch_best_bid_ask
from src.features.feature_engineering import build_features
from src.utils.logger import setup_logger


def main():
    logger = setup_logger("main")
    settings = load_settings()

    client = create_coinbase_client(settings)
    if not verify_connectivity(client):
        logger.error("Coinbase connectivity failed. Exiting.")
        return

    candles = fetch_public_candles(
        client,
        product_id=settings.trading.product_id,
        minutes_lookback=settings.candle_lookback_minutes,
        granularity=settings.candle_granularity,
    )
    bid_ask = fetch_best_bid_ask(client, settings.trading.product_id)
    df = build_features(candles, bid_ask)
    logger.info("Feature frame shape: %s", df.shape)


if __name__ == "__main__":
    main()
