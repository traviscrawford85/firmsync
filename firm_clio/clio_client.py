# firm_clio/clio_client.py

import os
from firm_clio.clio_provider import ClioProvider

def get_clio_client():
    provider = ClioProvider(
        client_id=os.getenv("CLIO_CLIENT_ID"),
        client_secret=os.getenv("CLIO_CLIENT_SECRET"),
        token_url=os.getenv("CLIO_TOKEN_URL"),
        api_url=os.getenv("CLIO_API_URL")
    )
    return provider.get_api_client()

def get_clio_service():
    provider = ClioProvider(
        client_id=os.getenv("CLIO_CLIENT_ID"),
        client_secret=os.getenv("CLIO_CLIENT_SECRET"),
        token_url=os.getenv("CLIO_TOKEN_URL"),
        api_url=os.getenv("CLIO_API_URL")
    )
    return provider.get_service_layer()
