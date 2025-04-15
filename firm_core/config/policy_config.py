# firm_qbo/qbo_helpers.py

from quickbooks.objects.vendor import Vendor
from quickbooks import QuickBooks

def search_vendor_by_name(name: str, qb: QuickBooks) -> Vendor | None:
    try:
        results = Vendor.filter(DisplayName=name, qb=qb)
        return results[0] if results else None
    except Exception as e:
        print(f"❌ Error searching for vendor '{name}': {e}")
        return None

# Allow new vendors to be created in QBO if they don't exist
ALLOW_VENDOR_CREATION = True

# Optionally ignore syncing contacts without a matter
IGNORE_CONTACTS_WITHOUT_MATTER = True