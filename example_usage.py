"""Example usage of the Coinbase REST API client"""

from coinbase.rest import RESTClient

# Initialize the client
client = RESTClient(
    api_key="your_api_key_here",
    api_secret="your_api_secret_here"
)

# Get API key permissions
try:
    permissions_response = client.get_api_key_permissions()
    print(f"Permissions: {permissions_response.permissions}")
    print(f"Portfolio ID: {permissions_response.portfolio_id}")
    print(f"Raw Response: {permissions_response.raw_response}")
except Exception as e:
    print(f"Error: {e}")
