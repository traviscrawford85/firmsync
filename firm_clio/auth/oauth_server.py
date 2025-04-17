# firm_clio/auth/oauth_server.py

from flask import Flask, request
import requests, os, time
from utils.token_storage import save_token_data
import webbrowser
from urllib.parse import urlencode
from flask import redirect

app = Flask(__name__)

def build_auth_url():
    return (
        f"https://app.clio.com/oauth/authorize?"
        f"client_id={os.getenv('CLIO_CLIENT_ID')}&"
        f"redirect_uri={os.getenv('CLIO_REDIRECT_URI')}&"
        f"response_type=code&"
        f"scope=all"
    )

@app.route("/")
def home():
    auth_url = build_auth_url()
    return redirect(auth_url)

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
    import sys
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        # This block runs only on the initial Flask launch, not on reload
        webbrowser.open("http://localhost:5000/")

    app.run(debug=True, port=5000)
