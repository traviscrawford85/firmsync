# firm_qbo/auth/oauth_server.py

import os
from flask import Flask, request
from intuitlib.client import AuthClient
from intuitlib.enums import Scopes
from dotenv import load_dotenv
import json

load_dotenv()
app = Flask(__name__)

auth_client = AuthClient(
    client_id=os.getenv("QB_CLIENT_ID"),
    client_secret=os.getenv("QB_CLIENT_SECRET"),
    environment=os.getenv("QB_ENVIRONMENT"),
    redirect_uri=os.getenv("QB_REDIRECT_URI")
)

@app.route("/")
def home():
    auth_url = auth_client.get_authorization_url([Scopes.ACCOUNTING])
    return f'<a href="{auth_url}" target="_blank">Click here to authorize QuickBooks</a>'

@app.route("/callback")
def callback():
    auth_code = request.args.get("code")
    state = request.args.get("state")

    auth_client.get_bearer_token(auth_code)

    token_data = {
        "access_token": auth_client.access_token,
        "refresh_token": auth_client.refresh_token,
        "expires_at": auth_client.expires_at
    }

    with open(os.getenv("QB_TOKEN_STORE_PATH"), "w") as f:
        json.dump(token_data, f, indent=2)

    return "✅ Authorization complete! Tokens saved."

if __name__ == "__main__":
    app.run(port=3000, debug=True)
