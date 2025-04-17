# firm_qbo/auth/oauth_server.py

import os
from flask import Flask, request
from intuitlib.client import AuthClient
from intuitlib.enums import Scopes
from dotenv import load_dotenv
from flask import redirect
import json
import time
import webbrowser

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
    return redirect(auth_url)

@app.route("/callback")
def callback():
    auth_code = request.args.get("code")
    state = request.args.get("state")

    auth_client.get_bearer_token(auth_code)

    token_data = {
        "access_token": auth_client.access_token,
        "refresh_token": auth_client.refresh_token,
        "expires_at": int(time.time()) + (auth_client.expires_in or 0),
    }

    token_store_path = os.getenv("QB_TOKEN_STORE_PATH")
    if not token_store_path:
        raise ValueError("Environment variable 'QB_TOKEN_STORE_PATH' is not set.")
    with open(token_store_path, "w") as f:
        json.dump(token_data, f, indent=2)

    return "✅ Authorization complete! Tokens saved."

if __name__ == "__main__":
    # Avoid browser re-opening on Flask debug reload
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        webbrowser.open("http://localhost:3000/")
    
    app.run(port=3000, debug=True)
