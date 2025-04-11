from flask import Flask, request, redirect
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load from .env
CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")
REDIRECT_URI = os.getenv("CLIO_REDIRECT_URI")

# Clio OAuth2 constants
AUTH_URL = "https://app.clio.com/oauth/authorize"
TOKEN_URL = "https://app.clio.com/oauth/token"
SCOPE = "read:all write:all"

@app.route("/")
def authorize():
    auth_link = (
        f"{AUTH_URL}?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope={SCOPE}"
        f"&state=xyz"
    )
    return f'<a href="{auth_link}" target="_blank">🔐 Click to authorize Clio</a>'

@app.route("/api/oauth/callback")
def oauth_callback():
    code = request.args.get("code")
    state = request.args.get("state")

    if not code:
        return "❌ No code provided in callback", 400

    # Exchange auth code for token
    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }

    response = requests.post(TOKEN_URL, data=payload)

    if response.status_code != 200:
        return f"❌ Failed to exchange token: {response.text}", 500

    tokens = response.json()

    # Optionally calculate expiry timestamp
    import time
    tokens["expires_at"] = int(time.time()) + tokens.get("expires_in", 3600)

    with open("firm_clio/clio_token_store.json", "w") as f:
        json.dump(tokens, f)

    print("✅ Clio OAuth token exchange completed and saved.")
    return "✅ Clio authorization successful! Tokens saved."

if __name__ == "__main__":
    app.run(port=5000)
