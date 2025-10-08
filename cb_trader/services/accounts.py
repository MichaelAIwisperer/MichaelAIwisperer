from typing import Optional

from coinbase.rest import RESTClient
from coinbase.rest.types.accounts_types import ListAccountsResponse


def list_accounts(client: RESTClient, limit: int = 50, cursor: Optional[str] = None) -> ListAccountsResponse:
    return client.get_accounts(limit=limit, cursor=cursor)

