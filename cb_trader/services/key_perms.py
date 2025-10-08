from coinbase.rest import RESTClient
from coinbase.rest.types.data_api_types import GetAPIKeyPermissionsResponse


def get_permissions(client: RESTClient) -> GetAPIKeyPermissionsResponse:
    return client.get_api_key_permissions()

