# firm_clio/sdk/client_factory.py

import os
from dotenv import load_dotenv
from clio_sdk.api_client import ApiClient
from clio_sdk.configuration import Configuration

load_dotenv()

def get_clio_api_client():
    access_token = os.getenv("CLIO_ACCESS_TOKEN")
    if not access_token:
        raise Exception("❌ CLIO_ACCESS_TOKEN not set in .env")

    config = Configuration(
        host="https://app.clio.com/api/v4",
        access_token=access_token
    )

    return ApiClient(configuration=config)
