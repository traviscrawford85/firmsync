# firm_qbo/auth/oauth_flow.py

import os
import json
from intuitlib.client import AuthClient
from intuitlib.exceptions import AuthClientError
from dotenv import load_dotenv

load_dotenv()

def get_auth_client():
    return AuthClient(
        client_id=os.getenv("QB_CLIENT_ID"),
        client_secret=os.getenv("QB_CLIENT_SECRET"),
        environment=os.getenv("QB_ENVIRONMENT"),
        redirect_uri=os.getenv("QB_REDIRECT_URI")
    )

def load_authenticated_client():
    token_path = os.getenv("QB_TOKEN_STORE_PATH")

    with open(token_path, "r") as f:
        tokens = json.load(f)

    auth_client = get_auth_client()
    auth_client.access_token = tokens["access_token"]
    auth_client.refresh_token = tokens["refresh_token"]

    try:
        auth_client.refresh()
        updated = {
            "access_token": auth_client.access_token,
            "refresh_token": auth_client.refresh_token,
            "expires_at": getattr(auth_client, "expires_at", 0)
        }

        with open(token_path, "w") as f:
            json.dump(updated, f, indent=2)

        print("🔁 QBO token refreshed successfully.")
    except AuthClientError as e:
        raise Exception(f"❌ QBO token refresh failed: {e}")

    return auth_client
