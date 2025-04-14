import os
import json
import time
from dotenv import load_dotenv
from clio_sdk.api.contacts_api import ContactsApi
from clio_sdk.models.contact import Contact
from firm_clio.clio_client import get_clio_client
from typing import List

load_dotenv()

def load_tokens(path=None):
    if path is None:
        path = os.getenv("CLIO_TOKEN_STORE_PATH") or os.getenv("QB_TOKEN_STORE_PATH")
        if not path:
            raise ValueError("❌ No token store path provided and no environment variable set.")
    print(f"📦 Using token store (load): {path}")
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ Token store file not found at: {path}")


def save_tokens(access_token, refresh_token, path=None, expires_in=3600):
    if path is None:
        path = os.getenv("CLIO_TOKEN_STORE_PATH") or os.getenv("QB_TOKEN_STORE_PATH")
        if not path:
            raise ValueError("❌ No token store path provided and no environment variable set.")
    print(f"📦 Using token store (save): {path}")
    
    with open(path, "w") as f:
        json.dump({
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_at": int(time.time()) + expires_in
        }, f)
        print("✅ Tokens saved successfully.")

# print_matters function to display matters in a user-friendly format
def print_matters(matters):
    for matter in matters:
        print(f"🗂️ ID: {matter.id}")
        print(f"📎 Display Number: {matter.display_number}")
        print(f"📝 Description: {matter.description}")
        print(f"📌 Status: {matter.status}")
        print("-" * 40)
        if not matters:
            print("📭 No matters found.")


# 
def search_contacts_by_name(query: str) -> list[Contact]:
    from firm_clio.clio_client import get_clio_client  # <-- moved here
    api = ContactsApi(get_clio_client())
    response = api.contact_index(query=query)
    return response.data



def print_contacts(contacts: List[Contact]):
    for c in contacts:
        print(f"👤 ID: {c.id}")
        print(f"🧾 Name: {c.name}")
        print(f"📧 Email: {getattr(c, 'primary_email_address', 'N/A')}")
        print(f"📞 Phone: {getattr(c, 'primary_phone_number', 'N/A')}")
        print("-" * 40)
        if not contacts:
            print("📭 No contacts found.")
