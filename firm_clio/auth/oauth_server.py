# firm_clio/auth/oauth_server.py
from flask import Flask, request
import requests, os, time
from utils.token_storage import save_token_data

app = Flask(__name__)

@app.route("/")
def home():
    auth_url = (
        f"https://app.clio.com/oauth/authorize?"
        f"client_id={os.getenv('CLIO_CLIENT_ID')}&"
        f"redirect_uri={os.getenv('CLIO_REDIRECT_URI')}&"
        f"response_type=code&"
        f"scope=all"
    )
    return f'<a href="{auth_url}" target="_blank">Authorize Clio</a>'

@app.route("/api/oauth/callback")
def callback():
    code = request.args.get("code")

    payload = {
        "grant_type": "authorization_code",
        "client_id": os.getenv("CLIO_CLIENT_ID"),
        "client_secret": os.getenv("CLIO_CLIENT_SECRET"),
        "redirect_uri": os.getenv("CLIO_REDIRECT_URI"),
        "code": code,
    }

    token_response = requests.post("https://app.clio.com/oauth/token", data=payload)

    if token_response.status_code != 200:
        return f"❌ Clio Authorization Error: {token_response.text}"

    tokens = token_response.json()
    tokens["expires_at"] = int(time.time()) + tokens.get("expires_in", 3600)

    save_token_data(tokens, "clio")

    return "✅ Clio Authorization Complete. Tokens Saved!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)