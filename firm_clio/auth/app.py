from flask import Flask, redirect, request
from urllib.parse import urlencode
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
  # Add the current directory to sys.path
from dotenv import load_dotenv

# ✅ Add this to import the Contacts API correctly
from clio_sdk import ApiClient, Configuration
from clio_sdk.api import contacts_api, users_api  # THIS IS THE CRITICAL IMPORT

# Load environment variables
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.env'))
# Check if the .env file exists
if not os.path.exists(dotenv_path):
    raise FileNotFoundError(f"Environment file not found: {dotenv_path}")
load_dotenv(dotenv_path)


# Define env_path globally
env_path = dotenv_path

app = Flask(__name__)

CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")
REDIRECT_URI = os.getenv("CLIO_REDIRECT_URI")
AUTH_URL = os.getenv("CLIO_AUTH_URL")
TOKEN_URL = os.getenv("CLIO_TOKEN_URL")
SCOPE = "users.read contacts.read"
  # Define the required scopes

# Step 1: Redirect user to Clio's authorization page
@app.route("/")
def authorize():
    query = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "users.read contacts.read"
    }
    auth_link = f"{AUTH_URL}?{urlencode(query)}"
    print("🔗 Auth URL:", auth_link)
    return redirect(auth_link)

# Step 2: Handle the OAuth callback
@app.route("/api/oauth/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "Authorization failed."

    # Step 3: Exchange authorization code for access token
    token_response = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "authorization_code",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "redirect_uri": REDIRECT_URI,
            "code": code,
        },
    )

    # Debugging: Print the raw token response
    token_data = token_response.json()
    print("✅ Received Scopes:", token_data.get("scope"))
    print("🔁 Full token response:", token_response.json())
    print("🔁 Status Code:", token_response.status_code)
    print("Token Response:", token_response.json())

    if token_response.status_code == 200:
        access_token = token_response.json().get("access_token")
        if access_token:
            # Save token to the root .env
            with open(env_path, "r+") as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if not line.startswith("CLIO_ACCESS_TOKEN="):
                        f.write(line)
                f.write(f"CLIO_ACCESS_TOKEN={access_token}\n")
                f.truncate()

            # ✅ Redirect to the dashboard after successful authorization
            return redirect("/dashboard")
        else:
            return "Authorization successful, but no token found in the response."
    else:
        return f"Error: {token_response.text}"

# ✅ Step 4: Dashboard to Display Clio Contacts
import requests

@app.route("/dashboard")
def dashboard():
    dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.env'))
    load_dotenv(dotenv_path)

    access_token = os.getenv("CLIO_ACCESS_TOKEN")
    headers = {"Authorization": f"Bearer {access_token}"}

    # 🚨 Let's try the /api/v4/users endpoint
    response = requests.get("https://app.clio.com/api/v4/users", headers=headers)

    print("🔍 Status:", response.status_code)
    print("🔍 Response:", response.text)

    return f"<pre>{response.status_code}\n{response.text}</pre>"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
