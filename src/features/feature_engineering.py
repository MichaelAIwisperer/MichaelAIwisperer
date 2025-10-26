from typing import Dict, Any
import numpy as np
import pandas as pd


def build_features(candles: list[dict[str, Any]], best_bid_ask: Any) -> pd.DataFrame:
    if not candles:
        return pd.DataFrame()

    df = pd.DataFrame(candles)
    # Convert numeric fields from strings
    for col in ["low", "high", "open", "close", "volume"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    # Coinbase candle fields are expected as dicts with: start, low, high, open, close, volume, granularity, product_id
    # Normalize and sort
    if "start" in df.columns:
        # Coinbase returns epoch seconds as strings in public candles
        df["start"] = pd.to_datetime(pd.to_numeric(df["start"], errors="coerce"), unit="s", utc=True)
        df = df.sort_values("start").reset_index(drop=True)

    # Basic technicals
    df["ret_1"] = df["close"].pct_change()
    df["vol_sma_10"] = df["volume"].rolling(10, min_periods=1).mean()
    df["price_sma_10"] = df["close"].rolling(10, min_periods=1).mean()
    df["price_sma_50"] = df["close"].rolling(50, min_periods=1).mean()
    df["sma_ratio"] = df["price_sma_10"] / (df["price_sma_50"] + 1e-9)

    # Impute infs
    df = df.replace([np.inf, -np.inf], 0.0).fillna(0.0)
    return df
