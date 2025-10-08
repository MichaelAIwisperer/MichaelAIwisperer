#!/usr/bin/env python3
"""Verification script for Coinbase SDK structure."""

import os
import sys

def check_file_exists(filepath):
    """Check if a file exists."""
    if os.path.exists(filepath):
        print(f"✓ {filepath}")
        return True
    else:
        print(f"✗ {filepath} (MISSING)")
        return False

def main():
    """Main verification function."""
    print("Coinbase SDK Structure Verification")
    print("=" * 50)
    
    all_good = True
    
    # Check main files
    print("\nMain Files:")
    all_good &= check_file_exists("README.md")
    all_good &= check_file_exists("LICENSE")
    all_good &= check_file_exists("setup.py")
    all_good &= check_file_exists("requirements.txt")
    all_good &= check_file_exists("example.py")
    all_good &= check_file_exists(".gitignore")
    
    # Check SDK package
    print("\nSDK Package Files:")
    all_good &= check_file_exists("coinbase_sdk/__init__.py")
    all_good &= check_file_exists("coinbase_sdk/rest_base.py")
    all_good &= check_file_exists("coinbase_sdk/rest_client.py")
    
    # Check modules
    print("\nAPI Modules:")
    modules = [
        "accounts", "convert", "data_api", "fees", "futures",
        "market_data", "orders", "payments", "perpetuals",
        "portfolios", "products", "public"
    ]
    
    for module in modules:
        all_good &= check_file_exists(f"coinbase_sdk/{module}.py")
    
    # Try to import
    print("\nImport Test:")
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from coinbase_sdk import RESTClient
        print("✓ Successfully imported RESTClient")
        
        # Check if all methods are available
        methods_to_check = [
            "get_accounts", "get_account", "market_order_buy",
            "limit_order_gtc", "get_products", "get_candles"
        ]
        
        print("\nMethod Availability:")
        for method in methods_to_check:
            if hasattr(RESTClient, method):
                print(f"✓ RESTClient.{method}")
            else:
                print(f"✗ RESTClient.{method} (MISSING)")
                all_good = False
                
    except Exception as e:
        print(f"✗ Import failed: {e}")
        all_good = False
    
    print("\n" + "=" * 50)
    if all_good:
        print("✓ All checks passed! SDK is ready to use.")
        return 0
    else:
        print("✗ Some checks failed. Please review the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
