# firm_clio/auth/oauth_flow.py

import os
import time
import requests
from utils.token_storage import load_token_data, save_token_data

TOKEN_URL = os.getenv("CLIO_TOKEN_URL", "https://app.clio.com/oauth/token")
TOKEN_PATH = os.getenv("CLIO_TOKEN_STORE_PATH", "firm_clio/clio_token_store.json")
CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")
REDIRECT_URI = os.getenv("CLIO_REDIRECT_URI")

def refresh_clio_token_if_needed(tokens: dict) -> dict:
    if "expires_at" in tokens and int(tokens["expires_at"]) > int(time.time()):
        print("🔐 Clio token is still valid.")
        return tokens

    print("🔁 Clio token expired. Refreshing...")

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": tokens["refresh_token"],
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }

    response = requests.post(TOKEN_URL, data=payload)
    if response.status_code != 200:
        raise Exception(f"❌ Clio token refresh failed: {response.text}")

    refreshed = response.json()
    refreshed["expires_at"] = int(time.time()) + refreshed.get("expires_in", 3600)
    save_token_data(refreshed, "clio")

    print("✅ Clio token refreshed.")
    return refreshed

def load_authenticated_clio_token() -> dict:
    try:
        tokens = load_token_data("clio")
        return refresh_clio_token_if_needed(tokens)
    except FileNotFoundError:
        raise Exception("❌ Clio token file not found. Run OAuth flow first.")
