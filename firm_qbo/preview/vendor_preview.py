# scripts/vendor_preview.py

from firm_clio.clio_client import get_clio_client
from clio_sdk.api.contacts_api import ContactsApi
from firm_core.config.policy_config import IGNORE_CONTACTS_WITHOUT_MATTER
from firm_qbo.mappers.vendor_mapper import get_or_create_vendor  # Will NOT create if policy is False

def preview_vendor_sync(limit: int = 10):
    """
    Preview Clio contacts for potential vendor mapping to QBO.
    """
    client = get_clio_client()
    api = ContactsApi(client)

    try:
        response = api.contact_index(limit=limit)
        contacts = response.data  # List[Contact] — actual Pydantic models

        print(f"\n🔍 Previewing {len(contacts)} Clio contacts for vendor sync:\n")
        for contact in contacts:
            name = contact.name or f"{contact.first_name or ''} {contact.last_name or ''}".strip()
            matter_count = getattr(contact, "matters_count", 0)
            print(f" • {name:<30} | Matters: {'Yes' if matter_count > 0 else 'No'}")

    except Exception as e:
        print(f"❌ Failed to load contacts: {e}")

if __name__ == "__main__":
    preview_vendor_sync()
