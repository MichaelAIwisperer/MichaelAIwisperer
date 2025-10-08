# Coinbase Payment Methods SDK

A Python SDK for interacting with Coinbase Advanced Trade API payment methods.

## Overview

This SDK provides a clean interface for managing payment methods through the Coinbase Advanced Trade API.

## Project Structure

```
coinbase/
├── __init__.py
├── constants.py
├── rest/
│   ├── __init__.py
│   ├── payments.py
│   └── types/
│       ├── __init__.py
│       └── payments_types.py
```

## Features

### Payment Methods API

The SDK includes the following payment methods functionality:

- **List Payment Methods**: Retrieve all payment methods for the current user
- **Get Payment Method**: Get details about a specific payment method

## Installation

```bash
pip install -r requirements.txt
```

## Usage

The payment methods are implemented as a mixin class that can be integrated into a Coinbase client:

```python
from coinbase.rest.payments import PaymentMethodsMixin

# Assuming you have a base client class with a get() method
class CoinbaseClient(PaymentMethodsMixin):
    def get(self, endpoint, **kwargs):
        # Your HTTP GET implementation
        pass

# Use the client
client = CoinbaseClient()

# List all payment methods
response = client.list_payment_methods()
print(response.payment_methods)

# Get a specific payment method
response = client.get_payment_method("payment_method_id_here")
print(response.payment_method)
```

## API Reference

### list_payment_methods(**kwargs)

Get a list of payment methods for the current user.

**Endpoint**: `GET /api/v3/brokerage/payment_methods`

**Returns**: `ListPaymentMethodsResponse`

### get_payment_method(payment_method_id: str, **kwargs)

Get information about a specific payment method.

**Endpoint**: `GET /api/v3/brokerage/payment_methods/{payment_method_id}`

**Parameters**:
- `payment_method_id` (str): The ID of the payment method to retrieve

**Returns**: `GetPaymentMethodResponse`

## Official Documentation

For more information, visit the [Coinbase Advanced Trade API Documentation](https://docs.cdp.coinbase.com/advanced-trade/reference/).

## License

This project is open source and available under the MIT License.
