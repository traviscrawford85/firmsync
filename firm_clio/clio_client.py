# firm_clio/clio_client.py

import os
import time
import requests
from clio_sdk import Configuration, ApiClient
from dotenv import load_dotenv
from clio_sdk import Configuration, ApiClient
from utils.helpers import load_tokens, save_tokens  # 👈 Centralized import

load_dotenv()

TOKEN_PATH = os.getenv("CLIO_TOKEN_PATH")
TOKEN_URL = "https://app.clio.com/oauth/token"


def refresh_token_if_needed(tokens: dict) -> dict:
    if "expires_at" in tokens and int(tokens["expires_at"]) <= int(time.time()):
        print("🔁 Token expired. Please re-authenticate via the OAuth flow.")
        raise Exception("❌ Clio token expired. Re-authentication required.")
    else:
        print("🔐 Token is valid.")
    return tokens


def get_clio_client():
    tokens = load_tokens()
    access_token = tokens["access_token"]
    if not access_token:
        raise ValueError("❌ No access token found in token store.")
    
    config = Configuration(
        host="https://app.clio.com/api/v4"
    )

    # 🛠️ Set the token here — BUT this doesn't automatically inject headers
    config.access_token = access_token

    # 🧠 Here's what makes it work!
    client = ApiClient(config)
    client.default_headers["Authorization"] = f"Bearer {access_token}"  # ✅ Required fix

    print(f"🧪 Token used: {access_token[:16]}...")
    return client


