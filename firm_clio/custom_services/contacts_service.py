from clio_sdk.api.contacts_api import ContactsApi
from custom_models.contact import ContactModel  # Define this like MatterModel

def get_contacts(client, limit=5):
    api = ContactsApi(client)
    response = api.contact_index(limit=limit)
    return [ContactModel(**data) for data in response.get("data", [])]