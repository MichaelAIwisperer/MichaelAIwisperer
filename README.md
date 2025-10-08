# Coinbase SDK

A comprehensive Python SDK for the Coinbase API, providing easy access to trading, portfolio management, market data, and more.

## Features

- **Full API Coverage**: Support for all major Coinbase API endpoints
- **Easy Authentication**: Simple API key setup with multiple authentication methods
- **Type Safety**: Comprehensive type hints for better IDE support
- **Convenient Helper Methods**: Pre-built order functions for common trading operations
- **Market Data**: Access to real-time and historical market data
- **Portfolio Management**: Create and manage portfolios
- **Futures & Perpetuals**: Full support for derivatives trading

## Installation

```bash
pip install -e .
```

Or install from requirements:

```bash
pip install -r requirements.txt
```

## Quick Start

### Basic Setup

```python
from coinbase_sdk import RESTClient

# Initialize with API credentials
client = RESTClient(
    api_key="your_api_key",
    api_secret="your_api_secret"
)

# Or load from a key file
client = RESTClient(key_file="path/to/credentials.json")
```

### Getting Market Data

```python
# Get all products
products = client.get_products()

# Get specific product
btc_product = client.get_product("BTC-USD")

# Get candles (OHLCV data)
candles = client.get_candles(
    product_id="BTC-USD",
    start="2024-01-01T00:00:00Z",
    end="2024-01-02T00:00:00Z",
    granularity="ONE_HOUR"
)
```

### Trading

```python
import uuid

# Create a market order
order = client.market_order_buy(
    client_order_id=str(uuid.uuid4()),
    product_id="BTC-USD",
    quote_size="100"  # $100 worth of BTC
)

# Create a limit order
limit_order = client.limit_order_gtc_buy(
    client_order_id=str(uuid.uuid4()),
    product_id="BTC-USD",
    base_size="0.001",  # 0.001 BTC
    limit_price="50000",  # at $50,000
    post_only=True
)

# Preview an order before placing it
preview = client.preview_market_order_buy(
    product_id="BTC-USD",
    quote_size="100"
)
```

### Account Management

```python
# Get all accounts
accounts = client.get_accounts()

# Get specific account
account = client.get_account("account-uuid")

# Get account balances
balances = client.get_accounts()
```

### Order Management

```python
# List orders
orders = client.list_orders(
    product_id="BTC-USD",
    order_status=["OPEN", "PENDING"]
)

# Get specific order
order = client.get_order("order-id")

# Cancel orders
cancel_result = client.cancel_orders(["order-id-1", "order-id-2"])

# Get fills
fills = client.get_fills(product_id="BTC-USD")
```

### Portfolio Management

```python
# Create portfolio
portfolio = client.create_portfolio(name="My Trading Portfolio")

# Get portfolios
portfolios = client.get_portfolios()

# Get portfolio breakdown
breakdown = client.get_portfolio_breakdown("portfolio-uuid")

# Move funds between portfolios
client.move_portfolio_funds({
    "from": "portfolio-uuid-1",
    "to": "portfolio-uuid-2",
    "amount": "1000",
    "currency": "USD"
})
```

### Futures Trading

```python
# Get futures positions
positions = client.list_futures_positions()

# Get specific position
position = client.get_futures_position("BTC-PERP")

# Schedule futures sweep
sweep = client.schedule_futures_sweep(usd_amount="1000")

# Get futures balance summary
balance = client.get_futures_balance_summary()
```

## API Reference

### RESTClient

The main client class that provides access to all API endpoints.

#### Parameters

- `api_key` (str, optional): The API key
- `api_secret` (str, optional): The API key secret
- `key_file` (IO | str, optional): Path to API key file or file-like object
- `base_url` (str): The base URL for REST requests. Default: "https://api.coinbase.com"
- `timeout` (int, optional): Timeout in seconds for REST requests. Default: 30
- `verbose` (bool): Enable debug logging. Default: False
- `rate_limit_headers` (bool): Enable rate limit headers. Default: False

### Available Modules

- **Accounts**: `get_accounts()`, `get_account()`
- **Orders**: `create_order()`, `list_orders()`, `cancel_orders()`, `get_order()`, `get_fills()`
- **Market Data**: `get_candles()`, `get_market_trades()`
- **Products**: `get_products()`, `get_product()`, `get_product_book()`, `get_best_bid_ask()`
- **Portfolios**: `create_portfolio()`, `get_portfolios()`, `edit_portfolio()`, `delete_portfolio()`
- **Futures**: `list_futures_positions()`, `get_futures_balance_summary()`, `schedule_futures_sweep()`
- **Perpetuals**: `list_perps_positions()`, `get_perps_portfolio_summary()`, `allocate_portfolio()`
- **Payments**: `list_payment_methods()`, `get_payment_method()`
- **Fees**: `get_transaction_summary()`
- **Public**: `get_public_products()`, `get_public_candles()`, `get_unix_time()`

### Order Types

The SDK provides convenient helper methods for common order types:

#### Market Orders
- `market_order()`, `market_order_buy()`, `market_order_sell()`

#### Limit Orders (Good Till Canceled)
- `limit_order_gtc()`, `limit_order_gtc_buy()`, `limit_order_gtc_sell()`

#### Limit Orders (Good Till Date)
- `limit_order_gtd()`, `limit_order_gtd_buy()`, `limit_order_gtd_sell()`

#### Limit Orders (Immediate or Cancel)
- `limit_order_ioc()`, `limit_order_ioc_buy()`, `limit_order_ioc_sell()`

#### Limit Orders (Fill or Kill)
- `limit_order_fok()`, `limit_order_fok_buy()`, `limit_order_fok_sell()`

#### Stop Limit Orders
- `stop_limit_order_gtc()`, `stop_limit_order_gtd()`

#### Trigger Bracket Orders
- `trigger_bracket_order_gtc()`, `trigger_bracket_order_gtd()`

All order types also have corresponding `preview_*` functions to preview orders before placing them.

## Authentication

### Using API Keys

```python
client = RESTClient(
    api_key="your_api_key",
    api_secret="your_api_secret"
)
```

### Using a Key File

Create a JSON file with your credentials:

```json
{
    "api_key": "your_api_key",
    "api_secret": "your_api_secret"
}
```

Then load it:

```python
client = RESTClient(key_file="credentials.json")
```

## Error Handling

```python
from requests.exceptions import HTTPError

try:
    order = client.market_order_buy(
        client_order_id=str(uuid.uuid4()),
        product_id="BTC-USD",
        quote_size="100"
    )
except HTTPError as e:
    print(f"API Error: {e.response.status_code}")
    print(f"Details: {e.response.json()}")
```

## Development

### Install Development Dependencies

```bash
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

### Code Formatting

```bash
black coinbase_sdk/
```

### Type Checking

```bash
mypy coinbase_sdk/
```

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This SDK is not officially supported by Coinbase. Use at your own risk. Always test thoroughly before using in production with real funds.

## Support

For issues and questions:
- Create an issue on GitHub
- Check the [Coinbase API Documentation](https://docs.cloud.coinbase.com/)

## Changelog

### Version 1.0.0
- Initial release
- Full API coverage for Coinbase Advanced Trade API
- Support for all order types
- Portfolio management
- Futures and perpetuals trading
- Market data endpoints
- Public API endpoints
