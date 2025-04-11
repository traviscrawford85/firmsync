from flask import Flask, request, redirect
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")
REDIRECT_URI = os.getenv("CLIO_REDIRECT_URI")
AUTH_URL = "https://app.clio.com/oauth/authorize"
TOKEN_URL = "https://app.clio.com/oauth/token"
SCOPE = " ".join([
    "read:all", "write:all"
])

@app.route("/")
def authorize():
    auth_link = (
        f"{AUTH_URL}?"
        f"response_type=code&"
        f"client_id={CLIENT_ID}&"
        f"redirect_uri={REDIRECT_URI}&"
        f"scope={SCOPE}&"
        f"state=xyz"
    )
    return f'<a href="{auth_link}" target="_blank">🔐 Click to authorize Clio</a>'

@app.route("/api/oauth/callback")
def oauth_callback():
    code = request.args.get("code")
    if not code:
        return "❌ No code received", 400

    # Exchange the code for access token
    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code
    }

    res = requests.post(TOKEN_URL, data=payload)
    if res.status_code != 200:
        return f"❌ Token exchange failed: {res.text}", 500

    tokens = res.json()
    with open("firm_clio/clio_token_store.json", "w") as f:
        json.dump(tokens, f)

    return "✅ Clio authorization successful! Tokens saved."

if __name__ == "__main__":
    app.run(port=5000)
