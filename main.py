#!/usr/bin/env python3
"""
Coinbase Trading Bot - Main Entry Point
Interactive CLI for trading on Coinbase
"""
from coinbase_trader import CoinbaseTrader
from config import Config
import sys


def print_menu():
    """Print the main menu"""
    print("\n" + "="*60)
    print("COINBASE TRADER - Main Menu")
    print("="*60)
    print("1.  View Portfolio")
    print("2.  View Current Price")
    print("3.  View Product Info")
    print("4.  Market Buy")
    print("5.  Market Sell")
    print("6.  Limit Buy")
    print("7.  Limit Sell")
    print("8.  View Orders")
    print("9.  Cancel Orders")
    print("10. Change Product (Current: {})".format(Config.DEFAULT_PRODUCT_ID))
    print("0.  Exit")
    print("="*60)


def main():
    """Main function to run the trading bot"""
    print("\n" + "="*60)
    print("COINBASE TRADING BOT")
    print("="*60)
    
    # Initialize trader
    try:
        trader = CoinbaseTrader()
        print("✓ Successfully connected to Coinbase API")
    except Exception as e:
        print(f"✗ Failed to initialize trader: {e}")
        print("\nPlease ensure you have:")
        print("1. Created a .env file (copy from .env.example)")
        print("2. Added your Coinbase API credentials")
        print("3. Installed dependencies: pip install -r requirements.txt")
        sys.exit(1)
    
    current_product = trader.product_id
    
    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == '0':
            print("\nExiting Coinbase Trader. Goodbye!")
            break
            
        elif choice == '1':
            print("\nFetching portfolio...")
            trader.display_portfolio()
            
        elif choice == '2':
            product = input(f"Enter product ID (or press Enter for {current_product}): ").strip()
            product = product if product else current_product
            trader.display_price(product)
            
        elif choice == '3':
            product = input(f"Enter product ID (or press Enter for {current_product}): ").strip()
            product = product if product else current_product
            info = trader.get_product_info(product)
            if info:
                print(f"\nProduct Info for {product}:")
                print("-" * 40)
                for key, value in info.items():
                    print(f"{key}: {value}")
                print("-" * 40)
                
        elif choice == '4':
            product = input(f"Enter product ID (or press Enter for {current_product}): ").strip()
            product = product if product else current_product
            trader.display_price(product)
            
            try:
                amount = float(input("Enter USD amount to spend: $"))
                confirm = input(f"Confirm market buy of ${amount} worth of {product}? (yes/no): ")
                if confirm.lower() == 'yes':
                    trader.market_buy(product, amount)
                else:
                    print("Order cancelled.")
            except ValueError:
                print("Invalid amount entered.")
                
        elif choice == '5':
            product = input(f"Enter product ID (or press Enter for {current_product}): ").strip()
            product = product if product else current_product
            trader.display_price(product)
            
            try:
                amount = float(input(f"Enter amount of {product.split('-')[0]} to sell: "))
                confirm = input(f"Confirm market sell of {amount} {product.split('-')[0]}? (yes/no): ")
                if confirm.lower() == 'yes':
                    trader.market_sell(product, amount)
                else:
                    print("Order cancelled.")
            except ValueError:
                print("Invalid amount entered.")
                
        elif choice == '6':
            product = input(f"Enter product ID (or press Enter for {current_product}): ").strip()
            product = product if product else current_product
            trader.display_price(product)
            
            try:
                amount = float(input(f"Enter amount of {product.split('-')[0]} to buy: "))
                limit_price = float(input("Enter limit price: $"))
                confirm = input(f"Confirm limit buy of {amount} {product.split('-')[0]} at ${limit_price}? (yes/no): ")
                if confirm.lower() == 'yes':
                    trader.limit_buy(product, amount, limit_price)
                else:
                    print("Order cancelled.")
            except ValueError:
                print("Invalid input entered.")
                
        elif choice == '7':
            product = input(f"Enter product ID (or press Enter for {current_product}): ").strip()
            product = product if product else current_product
            trader.display_price(product)
            
            try:
                amount = float(input(f"Enter amount of {product.split('-')[0]} to sell: "))
                limit_price = float(input("Enter limit price: $"))
                confirm = input(f"Confirm limit sell of {amount} {product.split('-')[0]} at ${limit_price}? (yes/no): ")
                if confirm.lower() == 'yes':
                    trader.limit_sell(product, amount, limit_price)
                else:
                    print("Order cancelled.")
            except ValueError:
                print("Invalid input entered.")
                
        elif choice == '8':
            product = input(f"Enter product ID (leave blank for all orders): ").strip()
            product = product if product else None
            orders = trader.get_orders(product)
            if orders and 'orders' in orders:
                print(f"\nOrders{' for ' + product if product else ''}:")
                print("-" * 60)
                if len(orders['orders']) == 0:
                    print("No orders found.")
                else:
                    for order in orders['orders']:
                        print(f"ID: {order.get('order_id', 'N/A')}")
                        print(f"  Product: {order.get('product_id', 'N/A')}")
                        print(f"  Side: {order.get('side', 'N/A')}")
                        print(f"  Status: {order.get('status', 'N/A')}")
                        print(f"  Size: {order.get('size', 'N/A')}")
                        print("-" * 60)
            else:
                print("Could not fetch orders.")
                
        elif choice == '9':
            order_ids = input("Enter order IDs to cancel (comma-separated): ").strip()
            if order_ids:
                order_id_list = [oid.strip() for oid in order_ids.split(',')]
                confirm = input(f"Confirm cancellation of {len(order_id_list)} order(s)? (yes/no): ")
                if confirm.lower() == 'yes':
                    trader.cancel_orders(order_id_list)
                else:
                    print("Cancellation aborted.")
            else:
                print("No order IDs provided.")
                
        elif choice == '10':
            new_product = input("Enter new default product ID (e.g., ETH-USD, BTC-USD): ").strip()
            if new_product:
                # Verify it's a valid product
                info = trader.get_product_info(new_product)
                if info:
                    current_product = new_product
                    trader.product_id = new_product
                    print(f"✓ Default product changed to {new_product}")
                else:
                    print(f"✗ Invalid product ID: {new_product}")
            else:
                print("No product ID entered.")
        
        else:
            print("\n✗ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
