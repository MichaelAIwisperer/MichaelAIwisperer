## Coinbase SDK (Scaffold)

Minimal scaffold for a Python Coinbase SDK with future market sentiment integration.

### Setup

1. Create and fill `a.env` at the repo root:

```
COINBASE_API_KEY=...
COINBASE_API_SECRET=...
WSJ_API_KEY=...
REUTERS_API_KEY=...
SEEKING_ALPHA_API_KEY=...
COINBASE_BASE_URL=https://api.coinbase.com
REQUEST_TIMEOUT_SECONDS=30
VERBOSE_LOGGING=false
RATE_LIMIT_HEADERS=false
```

2. Install dependencies:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Usage

See `examples/quickstart.py` for a basic usage example:

```bash
python -m examples.quickstart
```

The SDK loads configuration from `a.env`. The `RESTClient` currently provides a request helper and stubs for API methods that will be implemented module-by-module.
