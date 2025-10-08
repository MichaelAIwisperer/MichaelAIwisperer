## cb-trader scaffold

Activate venv:

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -e .
```

Env file:

```bash
cp .env.example .env
# fill COINBASE_API_KEY and COINBASE_API_SECRET for private endpoints
```

CLI usage:

```bash
cb public --limit 5
cb accounts --limit 20
cb run --product BTC-USD --short 5 --long 20 --interval 2 --ticks 20

Convert (requires private credentials and correct account UUIDs):

```bash
cb convert quote FROM_ACCOUNT_UUID TO_ACCOUNT_UUID 10.0
cb convert get TRADE_ID FROM_ACCOUNT_UUID TO_ACCOUNT_UUID
cb convert commit TRADE_ID FROM_ACCOUNT_UUID TO_ACCOUNT_UUID
```

Key permissions (auth):

```bash
cb key-perms
```

Fees summary (auth):

```bash
cb fees --product_type SPOT

Market data:

```bash
# candles (ISO8601 times)
cb candles BTC-USD 2025-01-01T00:00:00Z 2025-01-01T02:00:00Z ONE_MINUTE --limit 100

# trades snapshot
cb trades BTC-USD 5
```

Orders (paper by default; add --live to place):

```bash
# Preview market buy (quote size in quote currency)
cb order market-buy BTC-USD --quote_size 10

# Preview market sell (base size in base currency)
cb order market-sell BTC-USD --base_size 0.001

# Execute live (CAUTION: places real orders)
cb order market-buy BTC-USD --quote_size 10 --live
cb order market-sell BTC-USD --base_size 0.001 --live
```
```
```
