from src.config.settings import load_settings
from src.clients.coinbase_client import create_coinbase_client
from src.utils.logger import setup_logger


def main():
    logger = setup_logger("balances")
    s = load_settings()

    client = create_coinbase_client(s)
    if not getattr(client, "is_authenticated", False):
        logger.error("Client is not authenticated. Set COINBASE_KEY_FILE_PATH or API key/secret in .env")
        return

    resp = client.get_accounts(limit=250)
    accounts = getattr(resp, "accounts", []) or []

    total_usd = 0.0
    for acc in accounts:
        # acc has fields like available_balance { value, currency }
        bal = getattr(acc, "available_balance", None)
        if not bal:
            continue
        value = float(bal.get("value") if isinstance(bal, dict) else getattr(bal, "value", 0.0))
        currency = bal.get("currency") if isinstance(bal, dict) else getattr(bal, "currency", "")
        logger.info("%s: %s %s", getattr(acc, "currency", "?"), value, currency)
        # Note: converting to USD requires rates; here we sum USD only for simplicity
        if currency == "USD":
            total_usd += value

    logger.info("Total USD (available): %.2f", total_usd)


if __name__ == "__main__":
    main()
