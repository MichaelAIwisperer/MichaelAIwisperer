import os
from dotenv import load_dotenv
from coinbase.rest import RESTClient


def main() -> None:
    load_dotenv()

    timeout = int(os.getenv("COINBASE_TIMEOUT", "30"))
    verbose = os.getenv("COINBASE_VERBOSE", "false").lower() == "true"

    client = RESTClient(timeout=timeout, verbose=verbose)

    products = client.get_public_products(limit=5)
    # Print a small subset to confirm SDK works
    for p in products.products:
        print(f"{p.product_id} status={p.status}")


if __name__ == "__main__":
    main()

