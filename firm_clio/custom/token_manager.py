# custom/token_manager.py

import os
import time
import json
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN_STORE_PATH = "firm_clio/clio_token_store.json"
CLIO_OAUTH_URL = "https://app.clio.com/oauth/token"

def load_tokens():
    with open(TOKEN_STORE_PATH, "r") as f:
        return json.load(f)

def save_tokens(tokens):
    with open(TOKEN_STORE_PATH, "w") as f:
        json.dump(tokens, f)

def is_expired(tokens):
    return int(tokens.get("expires_at", 0)) <= int(time.time())

def refresh_token(tokens):
    print("🔁 Token expired, refreshing...")

    payload = {
        "grant_type": "refresh_token",
        "client_id": os.getenv("CLIO_CLIENT_ID"),
        "client_secret": os.getenv("CLIO_CLIENT_SECRET"),
        "refresh_token": tokens["refresh_token"]
    }

    response = requests.post(CLIO_OAUTH_URL, data=payload)
    if response.status_code != 200:
        raise Exception(f"❌ Failed to refresh token: {response.text}")

    new_tokens = response.json()
    new_tokens["expires_at"] = int(time.time()) + new_tokens.get("expires_in", 3600)

    save_tokens(new_tokens)
    print("✅ Token refreshed and saved.")
    return new_tokens
