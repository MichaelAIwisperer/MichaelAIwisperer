from coinbase.rest.client import RESTClient


def main() -> None:
    client = RESTClient(verbose=True, rate_limit_headers=True)
    print("Server time:", client.get_unix_time())
    print("Products sample:", client.get_public_products(limit=2))


if __name__ == "__main__":
    main()

