import os
from typing import Optional

from dotenv import load_dotenv
from coinbase.rest import RESTClient
from coinbase.rest.types.accounts_types import ListAccountsResponse


def env_bool(name: str, default: bool = False) -> bool:
    raw: Optional[str] = os.getenv(name)
    if raw is None:
        return default
    return raw.lower() in {"1", "true", "yes", "on"}


def main() -> None:
    load_dotenv()

    api_key = os.getenv("COINBASE_API_KEY")
    api_secret = os.getenv("COINBASE_API_SECRET")
    key_file = os.getenv("COINBASE_API_KEY_FILE")
    timeout = int(os.getenv("COINBASE_TIMEOUT", "30"))
    verbose = env_bool("COINBASE_VERBOSE", False)

    client = RESTClient(
        api_key=api_key,
        api_secret=api_secret,
        key_file=key_file,
        timeout=timeout,
        verbose=verbose,
    )

    accounts: ListAccountsResponse = client.get_accounts(limit=50)
    print(f"count={len(accounts.accounts)} cursor={accounts.cursor}")
    for acct in accounts.accounts:
        print(
            f"{acct.uuid} | {acct.currency} | bal={acct.available_balance.value} {acct.available_balance.currency} | type={acct.type}"
        )


if __name__ == "__main__":
    main()

