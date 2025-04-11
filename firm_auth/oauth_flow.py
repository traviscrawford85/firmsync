import os
from dotenv import load_dotenv
from intuitlib.client import AuthClient
from utils.helpers import load_tokens, save_tokens
from intuitlib.exceptions import AuthClientError

load_dotenv()

def get_auth_client():
    return AuthClient(
        client_id=os.getenv("QB_CLIENT_ID"),
        client_secret=os.getenv("QB_CLIENT_SECRET"),
        environment=os.getenv("QB_ENVIRONMENT"),
        redirect_uri=os.getenv("QB_REDIRECT_URI")
    )

def load_authenticated_client():
    try:
        tokens = load_tokens()
    except FileNotFoundError:
        raise Exception("❌ token_store.json not found. Run OAuth login first.")

    auth_client = get_auth_client()
    auth_client.access_token = tokens["access_token"]
    auth_client.refresh_token = tokens["refresh_token"]

    # Try refreshing the access token if needed
    try:
        auth_client.refresh()
        save_tokens(auth_client.access_token, auth_client.refresh_token)
        print("🔁 Token refresh successful.")
    except AuthClientError as e:
        raise Exception(f"❌ Token refresh failed: {e}")

    return auth_client
