import os
import time
import json
import requests
import webbrowser
from urllib.parse import urlencode, urlparse, parse_qs
from flask import Flask, request
from clio_sdk import Configuration, ApiClient

from dotenv import load_dotenv
load_dotenv()

# Load env vars
CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")
REDIRECT_URI = os.getenv("CLIO_REDIRECT_URI")
TOKEN_STORE_PATH = os.getenv("TOKEN_STORE_PATH", "firm_clio/clio_token_store.json")
CLIO_REGION = os.getenv("CLIO_REGION", "app.clio.com")

AUTH_URL = f"https://{CLIO_REGION}/oauth/authorize"
TOKEN_URL = f"https://{CLIO_REGION}/oauth/token"

app = Flask(__name__)

@app.route("/callback")
def clio_callback():
    code = request.args.get("code")
    if not code:
        return "No auth code received.", 400

    # Exchange auth code for tokens
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }

    res = requests.post(TOKEN_URL, data=payload)
    if res.status_code != 200:
        return f"Token exchange failed: {res.text}", 500

    tokens = res.json()
    tokens["expires_at"] = int(time.time()) + tokens.get("expires_in", 3600)

    os.makedirs(os.path.dirname(TOKEN_STORE_PATH), exist_ok=True)
    with open(TOKEN_STORE_PATH, "w") as f:
        json.dump(tokens, f)

    print("✅ Token stored in:", TOKEN_STORE_PATH)
    return "🎉 Success! You can close this tab and return to the terminal."

def start_auth_flow():
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": "all",
    }

    url = f"{AUTH_URL}?{urlencode(params)}"
    print(f"🌐 Opening browser for Clio authorization:\n{url}")
    webbrowser.open(url)

    app.run(port=urlparse(REDIRECT_URI).port or 5000)

# Add this to clio_auth.py

# This function is used to load the tokens from the token store.
def get_valid_token():
    """
    Returns a valid access token. Refreshes it if expired.
    """
    from custom_utils.token_store import load_tokens, save_tokens  # clean separation
    tokens = load_tokens()

    if int(tokens.get("expires_at", 0)) <= int(time.time()):
        print("🔁 Token expired, refreshing...")

        payload = {
            "grant_type": "refresh_token",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "refresh_token": tokens["refresh_token"],
        }

        response = requests.post(TOKEN_URL, data=payload)
        if response.status_code != 200:
            raise Exception(f"❌ Failed to refresh token: {response.text}")

        tokens = response.json()
        tokens["expires_at"] = int(time.time()) + tokens.get("expires_in", 3600)
        save_tokens(tokens)

        print("✅ Token refreshed and saved.")
    else:
        print("🔐 Token is valid.")

    return tokens["access_token"]

# This function is used to get an authenticated session with the Clio API.
def get_access_token() -> str:
    """
    Returns a valid access token. Refreshes it if expired.
    """
    access_token = get_valid_token()
    return access_token

def get_authenticated_api_client() -> ApiClient:
    access_token = get_valid_token()

    configuration = Configuration(
        host="https://app.clio.com/api/v4",
        access_token=access_token
    )
    return ApiClient(configuration=configuration)




if __name__ == "__main__":
    start_auth_flow()
