from flask import Flask, request
import requests
import os
import sys
import json
import time
from dotenv import load_dotenv
# 🔧 Ensure root is in path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.helpers import load_tokens, save_tokens

load_dotenv()

app = Flask(__name__)

CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")
REDIRECT_URI = os.getenv("CLIO_REDIRECT_URI")

@app.route("/")
def home():
    auth_url = (
        f"https://app.clio.com/oauth/authorize?"
        f"client_id={CLIENT_ID}&"
        f"redirect_uri={REDIRECT_URI}&"
        f"response_type=code&"
        f"scope=all"
    )
    return f'<a href="{auth_url}" target="_blank">Click here to authorize Clio</a>'

@app.route("/api/oauth/callback")
def callback():
    code = request.args.get("code")

    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }

    token_response = requests.post("https://app.clio.com/oauth/token", data=payload)
    if token_response.status_code != 200:
        return f"❌ Error: {token_response.text}"

    tokens = token_response.json()
    tokens["expires_at"] = int(time.time()) + tokens.get("expires_in", 3600)

    save_tokens(tokens["access_token"], tokens["refresh_token"])
    return "✅ Clio Authorization complete. Tokens saved!"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
