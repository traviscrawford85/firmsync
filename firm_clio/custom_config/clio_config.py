# firm_clio/custom_config/clio_config.py

import os
from dotenv import load_dotenv

load_dotenv()

class ClioConfig:
    CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")
    REDIRECT_URI = os.getenv("CLIO_REDIRECT_URI")
    TOKEN_URL = "https://app.clio.com/oauth/token"
    API_BASE_URL = "https://app.clio.com/api/v4"
    TOKEN_STORE_PATH = os.getenv("TOKEN_STORE_PATH", "firm_clio/clio_token_store.json")

    @classmethod
    def validate(cls):
        missing = []
        for attr in ["CLIENT_ID", "CLIENT_SECRET", "REDIRECT_URI"]:
            if not getattr(cls, attr):
                missing.append(attr)
        if missing:
            raise ValueError(f"Missing required Clio config values: {', '.join(missing)}")
