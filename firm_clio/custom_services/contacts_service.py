from clio_sdk.api.contacts_api import ContactsApi
from firm_clio.custom_models.contact import ContactModel  # Define this like MatterModel
from firm_clio.clio_client import get_clio_client  # ✅ this works with token
from typing import List

def get_contacts(client, limit=5):
    api = ContactsApi(client)
    response = api.contact_index(limit=limit)
    return [ContactModel(**data) for data in response.get("data", [])]

# def get_contact_by_id(client, contact_id):
def get_client_by_id(client_id: int):
    api = ContactsApi(get_clio_client())
    response = api.contact_show(client_id)
    return response.data