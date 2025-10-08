from typing import Optional

from coinbase.rest import RESTClient
from coinbase.rest.types.fees_types import GetTransactionSummaryResponse


def get_transaction_summary(
    client: RESTClient,
    product_type: Optional[str] = None,
    contract_expiry_type: Optional[str] = None,
    product_venue: Optional[str] = None,
) -> GetTransactionSummaryResponse:
    return client.get_transaction_summary(
        product_type=product_type,
        contract_expiry_type=contract_expiry_type,
        product_venue=product_venue,
    )

