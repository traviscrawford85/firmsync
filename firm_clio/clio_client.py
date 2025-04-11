import time
import os
import json
import requests
from dotenv import load_dotenv
from clio_sdk import ApiClient, Configuration

load_dotenv()

def get_clio_client():
    with open("firm_clio/clio_token_store.json", "r") as f:
        tokens = json.load(f)

    # Check if token is expired
    if "expires_at" in tokens and int(tokens["expires_at"]) <= int(time.time()):
        print("🔁 Token expired, refreshing...")

        payload = {
            "grant_type": "refresh_token",
            "client_id": os.getenv("CLIO_CLIENT_ID"),
            "client_secret": os.getenv("CLIO_CLIENT_SECRET"),
            "refresh_token": tokens["refresh_token"],
        }

        response = requests.post("https://app.clio.com/oauth/token", data=payload)
        if response.status_code != 200:
            raise Exception(f"❌ Failed to refresh token: {response.text}")

        tokens = response.json()
        tokens["expires_at"] = int(time.time()) + tokens.get("expires_in", 3600)

        with open("firm_clio/clio_token_store.json", "w") as f:
            json.dump(tokens, f)

        print("✅ Token refreshed and saved.")
    else:
        print("🔐 Using existing token.")
        print(f"🔐 Using token: {tokens['access_token'][:10]}...")

    config = Configuration(
        host="https://app.clio.com/api/v4",
        access_token=tokens["access_token"]
    )
    return ApiClient(configuration=config)