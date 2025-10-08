import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
SRC_PATH = os.path.join(PROJECT_ROOT, "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from coinbase_sdk import RESTClient, load_config_from_env  # noqa: E402

def main() -> None:
    client = RESTClient()
    config = load_config_from_env()
    print("Coinbase SDK configured:")
    print(f"  Base URL: {client.base_url}")
    print(f"  Timeout: {config.timeout_seconds}s")
    print(f"  Verbose: {config.verbose_logging}")
    print(f"  Rate limit headers: {config.rate_limit_headers}")
    print("Keys present:", bool(config.api_key))

if __name__ == "__main__":
    main()
