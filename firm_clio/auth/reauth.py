# firm_clio/auth/reauth.py

import os
import time
import json
import requests
from dotenv import load_dotenv
from custom_utils.token_store import save_tokens

load_dotenv()

CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")
REDIRECT_URI = os.getenv("CLIO_REDIRECT_URI")
TOKEN_URL = "https://app.clio.com/oauth/token"

def reauth():
    print("🔑 Manual re-authentication with Clio")

    code = input("Paste your OAuth 'code' from the redirect URL: ").strip()
    if not code:
        print("❌ No code entered. Exiting.")
        return

    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
    }

    print("🔄 Requesting new tokens...")
    response = requests.post(TOKEN_URL, data=payload)
    if response.status_code != 200:
        print(f"❌ Failed to get token: {response.text}")
        return

    tokens = response.json()
    tokens["expires_at"] = int(time.time()) + tokens.get("expires_in", 3600)
    save_tokens(tokens)

    print("✅ Token acquired and saved successfully.")

if __name__ == "__main__":
    reauth()
