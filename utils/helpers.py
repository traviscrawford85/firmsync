import json
import os

# This file contains helper functions for handling OAuth2 tokens.
# It includes functions to save and load tokens from a JSON file.
def save_tokens(access_token, refresh_token, path="firm_auth/token_store.json"):
    with open(path, "w") as f:
        json.dump({
            "access_token": access_token,
            "refresh_token": refresh_token
        }, f)

def load_tokens(path="firm_auth/token_store.json"):
    with open(path, "r") as f:
        return json.load(f)



