"""
Coinbase Trading Bot - Main trading logic
"""
from coinbase.rest import RESTClient
from config import Config
import json
from datetime import datetime


class CoinbaseTrader:
    """Main trading bot class for Coinbase Advanced Trade API"""
    
    def __init__(self):
        """Initialize the trader with API credentials"""
        Config.validate()
        self.client = RESTClient(
            api_key=Config.API_KEY,
            api_secret=Config.API_SECRET
        )
        self.product_id = Config.DEFAULT_PRODUCT_ID
        
    def get_accounts(self):
        """Get all account balances"""
        try:
            accounts = self.client.get_accounts()
            return accounts
        except Exception as e:
            print(f"Error fetching accounts: {e}")
            return None
    
    def get_product_info(self, product_id=None):
        """Get information about a trading pair"""
        if product_id is None:
            product_id = self.product_id
        try:
            product = self.client.get_product(product_id=product_id)
            return product
        except Exception as e:
            print(f"Error fetching product info: {e}")
            return None
    
    def get_current_price(self, product_id=None):
        """Get current price for a product"""
        if product_id is None:
            product_id = self.product_id
        try:
            product = self.client.get_product(product_id=product_id)
            if product and 'price' in product:
                return float(product['price'])
            return None
        except Exception as e:
            print(f"Error fetching price: {e}")
            return None
    
    def get_24h_stats(self, product_id=None):
        """Get 24-hour stats for a product"""
        if product_id is None:
            product_id = self.product_id
        try:
            candles = self.client.get_candles(
                product_id=product_id,
                start=None,
                end=None,
                granularity="ONE_DAY"
            )
            return candles
        except Exception as e:
            print(f"Error fetching 24h stats: {e}")
            return None
    
    def market_buy(self, product_id, amount_usd):
        """
        Place a market buy order
        
        Args:
            product_id: Trading pair (e.g., 'BTC-USD')
            amount_usd: Amount in USD to spend
        """
        try:
            order = self.client.market_order_buy(
                client_order_id=f"buy_{datetime.now().timestamp()}",
                product_id=product_id,
                quote_size=str(amount_usd)
            )
            print(f"✓ Market buy order placed: {amount_usd} USD of {product_id}")
            return order
        except Exception as e:
            print(f"✗ Error placing buy order: {e}")
            return None
    
    def market_sell(self, product_id, amount_base):
        """
        Place a market sell order
        
        Args:
            product_id: Trading pair (e.g., 'BTC-USD')
            amount_base: Amount of base currency to sell (e.g., BTC amount)
        """
        try:
            order = self.client.market_order_sell(
                client_order_id=f"sell_{datetime.now().timestamp()}",
                product_id=product_id,
                base_size=str(amount_base)
            )
            print(f"✓ Market sell order placed: {amount_base} of {product_id}")
            return order
        except Exception as e:
            print(f"✗ Error placing sell order: {e}")
            return None
    
    def limit_buy(self, product_id, amount_base, limit_price):
        """
        Place a limit buy order
        
        Args:
            product_id: Trading pair
            amount_base: Amount of base currency
            limit_price: Limit price
        """
        try:
            order = self.client.limit_order_gtc_buy(
                client_order_id=f"limit_buy_{datetime.now().timestamp()}",
                product_id=product_id,
                base_size=str(amount_base),
                limit_price=str(limit_price)
            )
            print(f"✓ Limit buy order placed: {amount_base} {product_id} at ${limit_price}")
            return order
        except Exception as e:
            print(f"✗ Error placing limit buy order: {e}")
            return None
    
    def limit_sell(self, product_id, amount_base, limit_price):
        """
        Place a limit sell order
        
        Args:
            product_id: Trading pair
            amount_base: Amount of base currency
            limit_price: Limit price
        """
        try:
            order = self.client.limit_order_gtc_sell(
                client_order_id=f"limit_sell_{datetime.now().timestamp()}",
                product_id=product_id,
                base_size=str(amount_base),
                limit_price=str(limit_price)
            )
            print(f"✓ Limit sell order placed: {amount_base} {product_id} at ${limit_price}")
            return order
        except Exception as e:
            print(f"✗ Error placing limit sell order: {e}")
            return None
    
    def get_orders(self, product_id=None):
        """Get list of orders"""
        try:
            if product_id:
                orders = self.client.list_orders(product_id=product_id)
            else:
                orders = self.client.list_orders()
            return orders
        except Exception as e:
            print(f"Error fetching orders: {e}")
            return None
    
    def cancel_orders(self, order_ids):
        """Cancel specific orders by ID"""
        try:
            result = self.client.cancel_orders(order_ids=order_ids)
            print(f"✓ Cancelled orders: {order_ids}")
            return result
        except Exception as e:
            print(f"✗ Error cancelling orders: {e}")
            return None
    
    def display_portfolio(self):
        """Display current portfolio balances"""
        accounts = self.get_accounts()
        if not accounts:
            print("Could not fetch accounts")
            return
        
        print("\n" + "="*60)
        print("PORTFOLIO SUMMARY")
        print("="*60)
        
        if 'accounts' in accounts:
            for account in accounts['accounts']:
                balance = float(account.get('available_balance', {}).get('value', 0))
                if balance > 0.01:  # Only show accounts with significant balance
                    currency = account.get('currency', 'N/A')
                    print(f"{currency:10s}: {balance:.8f}")
        print("="*60 + "\n")
    
    def display_price(self, product_id=None):
        """Display current price for a product"""
        if product_id is None:
            product_id = self.product_id
            
        price = self.get_current_price(product_id)
        if price:
            print(f"\n{product_id} Current Price: ${price:,.2f}\n")
        else:
            print(f"Could not fetch price for {product_id}")
