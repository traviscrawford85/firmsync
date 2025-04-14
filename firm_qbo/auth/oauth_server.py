import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# This is a simple Flask server to handle OAuth2 authorization for QuickBooks Online.
from flask import Flask, request
from intuitlib.client import AuthClient
from intuitlib.enums import Scopes
from utils.helpers import load_tokens, save_tokens
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Initialize QuickBooks OAuth client
auth_client = AuthClient(
    client_id=os.getenv('QB_CLIENT_ID'),
    client_secret=os.getenv('QB_CLIENT_SECRET'),
    environment=os.getenv('QB_ENVIRONMENT'),
    redirect_uri=os.getenv('QB_REDIRECT_URI')
)

@app.route("/")
def home():
    auth_url = auth_client.get_authorization_url([Scopes.ACCOUNTING])
    return f'<a href="{auth_url}" target="_blank">Click here to authorize QuickBooks</a>'

@app.route("/callback")
def callback():
    auth_code = request.args.get("code")
    state = request.args.get("state")

    # Exchange the code for tokens
    auth_client.get_bearer_token(auth_code)
    save_tokens(auth_client.access_token, auth_client.refresh_token)

    return "✅ Authorization complete! Tokens saved to token_store.json."

if __name__ == "__main__":
    app.run(port=3000)
