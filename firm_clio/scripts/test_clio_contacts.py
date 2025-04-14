import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from firm_clio.clio_client import get_clio_client
from firm_clio.clio_sdk.api.contacts_api import ContactsApi

from firm_clio.clio_client import get_clio_client
from firm_clio.clio_sdk.api.contacts_api import ContactsApi

def test_contacts():
    client = get_clio_client()
    contacts_api = ContactsApi(client)

    response = contacts_api.contact_index(limit=5)
    for contact in response['data']:
        print(f"📇 {contact['first_name']} {contact['last_name']} (ID: {contact['id']})")

def test_contact_show():
    client = get_clio_client()
    contacts_api = ContactsApi(client)

    contact_id = 2198899562  # ← Replace with actual ID if needed
    contact = contacts_api.contact_show(contact_id)
    
    print("🧾 Contact Details:")
    print(f"Name: {contact['data']['first_name']} {contact['data']['last_name']}")
    print(f"Email: {contact['data']['email']}")
    print(f"Phone: {contact['data']['phone']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Please provide a function name to run: test_contacts or test_contact_show")
    else:
        func_name = sys.argv[1]
        if func_name == "test_contacts":
            test_contacts()
        elif func_name == "test_contact_show":
            test_contact_show()
        else:
            print(f"❌ Unknown function: {func_name}")