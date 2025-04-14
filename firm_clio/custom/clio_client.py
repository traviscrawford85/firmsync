# firm_clio/custom_services/clio_client.py

from clio_sdk import Configuration, ApiClient
from firm_clio.auth.clio_auth import get_valid_token

def get_clio_client():
    token = get_valid_token()
    config = Configuration(
        host="https://app.clio.com/api/v4",
        access_token=token,
    )
    return ApiClient(configuration=config)
