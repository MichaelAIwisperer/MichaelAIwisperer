from typing import Optional

from coinbase.rest import RESTClient
from coinbase.rest.types.convert_types import (
    CreateConvertQuoteResponse,
    GetConvertTradeResponse,
    CommitConvertTradeResponse,
)


def create_quote(
    client: RESTClient,
    from_account: str,
    to_account: str,
    amount: str,
    user_incentive_id: Optional[str] = None,
    code_val: Optional[str] = None,
) -> CreateConvertQuoteResponse:
    return client.create_convert_quote(
        from_account=from_account,
        to_account=to_account,
        amount=amount,
        user_incentive_id=user_incentive_id,
        code_val=code_val,
    )


def get_trade(
    client: RESTClient,
    trade_id: str,
    from_account: str,
    to_account: str,
) -> GetConvertTradeResponse:
    return client.get_convert_trade(
        trade_id=trade_id,
        from_account=from_account,
        to_account=to_account,
    )


def commit_trade(
    client: RESTClient,
    trade_id: str,
    from_account: str,
    to_account: str,
) -> CommitConvertTradeResponse:
    return client.commit_convert_trade(
        trade_id=trade_id,
        from_account=from_account,
        to_account=to_account,
    )

