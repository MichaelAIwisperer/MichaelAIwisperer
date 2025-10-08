# Coinbase REST API Client Setup

This project provides a Python client for the Coinbase Advanced Trade API.

## Project Structure

```
coinbase/
├── __init__.py
├── constants.py              # API constants and configuration
└── rest/
    ├── __init__.py
    ├── rest_client.py        # Main REST client with API methods
    └── types/
        ├── __init__.py
        └── data_api_types.py # Response type definitions
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Initialize the Client

```python
from coinbase.rest import RESTClient

client = RESTClient(
    api_key="your_api_key_here",
    api_secret="your_api_secret_here"
)
```

### Get API Key Permissions

```python
# Get information about your CDP API key permissions
permissions_response = client.get_api_key_permissions()

print(f"Permissions: {permissions_response.permissions}")
print(f"Portfolio ID: {permissions_response.portfolio_id}")
print(f"Portfolio UUID: {permissions_response.portfolio_uuid}")
```

## Implementation Details

### Fixed Issues

1. **Completed the return statement** - The original code had a trailing dot that was removed:
   ```python
   # Original (incorrect):
   return GetAPIKeyPermissionsResponse(self.get(endpoint, **kwargs)).
   
   # Fixed:
   return GetAPIKeyPermissionsResponse(self.get(endpoint, **kwargs))
   ```

2. **Created complete project structure** with proper module organization

3. **Implemented response type** with proper data handling and attributes

### Key Components

- **RESTClient**: Main client class with HTTP methods and API endpoints
- **GetAPIKeyPermissionsResponse**: Response object that parses and exposes API data
- **Constants**: Centralized API configuration

## Example

See `example_usage.py` for a complete working example.

## API Documentation

For more information about the Coinbase Advanced Trade API, visit:
- [Get API Key Permissions Endpoint](https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getapikeypermissions)
