import os
import sys
from typing import Any, Dict

from coinbase.rest import RESTClient


def format_balance(account: Dict[str, Any]) -> str:
    currency = account.get("currency") or account.get("balance", {}).get("currency")
    available = (
        account.get("available_balance", {}).get("value")
        if isinstance(account.get("available_balance"), dict)
        else None
    )
    hold = (
        account.get("hold", {}).get("value")
        if isinstance(account.get("hold"), dict)
        else None
    )
    total = (
        account.get("balance", {}).get("value")
        if isinstance(account.get("balance"), dict)
        else None
    )
    name = account.get("name") or account.get("uuid")
    return f"{name}: available={available} {currency}, hold={hold} {currency}, total={total} {currency}"


def main() -> int:
    api_key = os.getenv("COINBASE_API_KEY")
    api_secret = os.getenv("COINBASE_API_SECRET")
    private_key_file = os.getenv("COINBASE_PRIVATE_KEY_FILE")

    if not api_key:
        print("ERROR: Please export COINBASE_API_KEY.")
        return 1

    if private_key_file:
        client = RESTClient(api_key=api_key, key_file=private_key_file)
    else:
        if not api_secret:
            print("ERROR: Please export COINBASE_API_SECRET or COINBASE_PRIVATE_KEY_FILE.")
            return 1
        client = RESTClient(api_key=api_key, api_secret=api_secret)

    try:
        accounts_resp = client.get_accounts(limit=250)
    except Exception as exc:
        print("Failed to fetch accounts:", exc)
        return 1

    accounts = accounts_resp.get("accounts", []) if isinstance(accounts_resp, dict) else []
    if not accounts:
        print("No accounts returned.")
        return 0

    # Print summary and per-account balances
    print(f"Accounts found: {len(accounts)}")
    for acct in accounts:
        print(format_balance(acct))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

