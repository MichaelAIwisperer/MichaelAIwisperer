"""Example usage of the Coinbase Payment Methods SDK"""

import requests
from coinbase.rest.payments import PaymentMethodsMixin


class CoinbaseClient(PaymentMethodsMixin):
    """Example Coinbase API client implementation"""
    
    def __init__(self, api_key: str, api_secret: str, base_url: str = "https://api.coinbase.com"):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
    
    def get(self, endpoint: str, **kwargs):
        """Make a GET request to the Coinbase API"""
        url = f"{self.base_url}{endpoint}"
        
        # Add authentication headers
        headers = {
            "CB-ACCESS-KEY": self.api_key,
            # In a real implementation, you would add proper authentication
            # including CB-ACCESS-SIGN, CB-ACCESS-TIMESTAMP, etc.
        }
        
        response = requests.get(url, headers=headers, **kwargs)
        response.raise_for_status()
        
        return response.json()


def main():
    """Example usage"""
    
    # Initialize the client (replace with your actual credentials)
    client = CoinbaseClient(
        api_key="your_api_key_here",
        api_secret="your_api_secret_here"
    )
    
    try:
        # List all payment methods
        print("Fetching payment methods...")
        methods_response = client.list_payment_methods()
        print(f"Found {len(methods_response.payment_methods)} payment methods")
        
        for method in methods_response.payment_methods:
            print(f"  - {method.get('type')}: {method.get('id')}")
        
        # Get details for a specific payment method (if available)
        if methods_response.payment_methods:
            first_method_id = methods_response.payment_methods[0].get('id')
            print(f"\nFetching details for payment method: {first_method_id}")
            
            method_response = client.get_payment_method(first_method_id)
            print(f"Payment method details: {method_response.payment_method}")
    
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
