## Coinbase Trading Bot (DQN + LSTM) - Scaffold

This repository is scaffolded to build a Coinbase Advanced Trade bot that consumes public market data (order book, trades) and later integrates a news/sentiment module (Reuters, WSJ, Seeking Alpha). The final goal is a DQN/LSTM policy that learns from executions, with risk controls (TP/SL) and optional paper trading.

### Quick start

1) Create your environment file by copying the example:
```bash
cp .env.example .env
```

2) Fill in `.env` locally with your API values. Do NOT commit secrets.

3) Install dependencies:
```bash
pip3 install -r requirements.txt
```

4) Run a quick public data check:
```bash
python3 -m src.main
```

### Environment variables (.env)

- `COINBASE_API_KEY`: Your Coinbase API key "name" (optional for public endpoints)
- `COINBASE_API_SECRET`: Your EC private key PEM contents
- `COINBASE_BASE_URL`: Defaults to `api.coinbase.com`
- `COINBASE_TIMEOUT_SECONDS`: Request timeout in seconds
- `REUTERS_API_KEY`, `WSJ_API_KEY`, `SEEKING_ALPHA_API_KEY`: News providers (optional placeholders)
- `PRODUCT_ID`: e.g., `BTC-USD`
- `PAPER_TRADING`: `true` to avoid placing live orders
- `TAKE_PROFIT_PCT`, `STOP_LOSS_PCT`, `MAX_POSITION_USD`: Risk settings

`.env` is already git-ignored. Never paste secrets into commits or issues.

### Notes on Coinbase keys

The SDK builds a JWT from `COINBASE_API_KEY` and the EC private key in `COINBASE_API_SECRET`. Public endpoints (order book, trades) work without auth; private endpoints (placing orders) require valid trade permissions. Prefer paper trading while validating logic.

### Next steps (planned)

- Market data ingestion and feature engineering (L2 depth, spreads, imbalance)
- News/sentiment adapters (Reuters, WSJ, Seeking Alpha)
- Reward shaping and DQN+LSTM training loop
- Execution module with TP/SL and learning from outcomes

