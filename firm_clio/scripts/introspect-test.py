import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from firm_clio.clio_client import get_clio_client
from firm_clio.clio_sdk.api.contacts_api import ContactsApi

client = get_clio_client()
api = ContactsApi(client)

print("📦 Available methods in ContactsApi:")
print([method for method in dir(api) if not method.startswith("_")])
