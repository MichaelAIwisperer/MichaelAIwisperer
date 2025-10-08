"""Example usage of the Coinbase SDK."""

from coinbase_sdk import RESTClient
import uuid

def main():
    # Initialize the client
    # Option 1: With API credentials directly
    client = RESTClient(
        api_key="your_api_key",
        api_secret="your_api_secret",
        verbose=True  # Enable debug logging
    )
    
    # Option 2: Load from key file
    # client = RESTClient(key_file="credentials.json")
    
    # Get public market data (no authentication required)
    print("=== Getting Public Market Data ===")
    products = client.get_public_products(limit=5)
    print(f"Products: {products}")
    
    # Get BTC-USD product information
    btc_product = client.get_public_product("BTC-USD")
    print(f"BTC-USD Product: {btc_product}")
    
    # Get candles for BTC-USD
    candles = client.get_public_candles(
        product_id="BTC-USD",
        start="2024-01-01T00:00:00Z",
        end="2024-01-02T00:00:00Z",
        granularity="ONE_HOUR"
    )
    print(f"Candles: {candles}")
    
    # Authenticated endpoints (requires valid API credentials)
    print("\n=== Authenticated Endpoints ===")
    
    # Get accounts
    try:
        accounts = client.get_accounts()
        print(f"Accounts: {accounts}")
    except Exception as e:
        print(f"Error getting accounts: {e}")
    
    # Preview a market order (doesn't execute)
    try:
        preview = client.preview_market_order_buy(
            product_id="BTC-USD",
            quote_size="10"  # $10 worth of BTC
        )
        print(f"Order Preview: {preview}")
    except Exception as e:
        print(f"Error previewing order: {e}")
    
    # Create a market order (uncomment to execute)
    # WARNING: This will place a real order!
    # try:
    #     order = client.market_order_buy(
    #         client_order_id=str(uuid.uuid4()),
    #         product_id="BTC-USD",
    #         quote_size="10"
    #     )
    #     print(f"Order placed: {order}")
    # except Exception as e:
    #     print(f"Error placing order: {e}")
    
    # Create a limit order (uncomment to execute)
    # WARNING: This will place a real order!
    # try:
    #     limit_order = client.limit_order_gtc_buy(
    #         client_order_id=str(uuid.uuid4()),
    #         product_id="BTC-USD",
    #         base_size="0.0001",  # 0.0001 BTC
    #         limit_price="40000",  # at $40,000
    #         post_only=True
    #     )
    #     print(f"Limit order placed: {limit_order}")
    # except Exception as e:
    #     print(f"Error placing limit order: {e}")
    
    # List orders
    try:
        orders = client.list_orders(
            product_id="BTC-USD",
            limit=10
        )
        print(f"Orders: {orders}")
    except Exception as e:
        print(f"Error listing orders: {e}")
    
    # Get portfolios
    try:
        portfolios = client.get_portfolios()
        print(f"Portfolios: {portfolios}")
    except Exception as e:
        print(f"Error getting portfolios: {e}")

if __name__ == "__main__":
    main()
