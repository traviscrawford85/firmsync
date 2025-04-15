# utils/token_storage.py

import os
import json
from dotenv import load_dotenv

# 🌱 Only run once when imported
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

def get_token_path(source: str) -> str:
    key = f"{source.upper()}_TOKEN_STORE_PATH"
    path = os.getenv(key)

    if not path:
        print(f"🚨 ENV var '{key}' is missing. Ensure it's defined in your .env file.")
        raise ValueError(f"❌ Missing environment variable for token store path: {key}")

    return path

def load_token_data(source: str) -> dict:
    path = get_token_path(source)
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ Token file not found for {source.upper()}: {path}")
    with open(path, "r") as f:
        print(f"📦 Loading tokens for {source.upper()} → {path}")
        return json.load(f)

def save_token_data(data: dict, source: str):
    path = get_token_path(source)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        print(f"💾 Saved tokens for {source.upper()} → {path}")
