import os
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN_STORE_PATH = os.getenv("TOKEN_STORE_PATH", "firm_clio/clio_token_store.json")

def load_tokens():
    if not os.path.exists(TOKEN_STORE_PATH):
        raise FileNotFoundError("❌ Token file not found. Please run the auth script.")
    with open(TOKEN_STORE_PATH, "r") as f:
        return json.load(f)

def save_tokens(tokens: dict):
    os.makedirs(os.path.dirname(TOKEN_STORE_PATH), exist_ok=True)
    with open(TOKEN_STORE_PATH, "w") as f:
        json.dump(tokens, f)
