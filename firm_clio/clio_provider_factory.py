import os
from dotenv import load_dotenv
from firm_clio.clio_provider import ClioProvider

load_dotenv()  # Loads the .env file automatically

_provider = None


def get_clio_provider():
    global _provider
    if _provider is None:
        _provider = ClioProvider(
            client_id=os.getenv("CLIO_CLIENT_ID"),
            client_secret=os.getenv("CLIO_CLIENT_SECRET"),
            token_url=os.getenv("CLIO_TOKEN_URL"),
            api_url=os.getenv("CLIO_API_URL")
        )

        # Optionally: Set token storage location from .env
        token_store_path = os.getenv("CLIO_TOKEN_STORE_PATH")
        if token_store_path:
            _provider.token_store_path = token_store_path

    return _provider
