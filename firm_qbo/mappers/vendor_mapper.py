# firm_qbo/mappers/vendor_mapper.py

from quickbooks.objects.vendor import Vendor
from firm_qbo.qbo_client import get_qbo_client
from firm_core.config.policy_config import ALLOW_VENDOR_CREATION

def get_or_create_vendor(display_name: str) -> str | None:
    """
    Ensure a vendor exists in QBO. Returns the vendor ID or None if not found/created.
    """
    qb = get_qbo_client()

    try:
        existing = Vendor.filter(DisplayName=display_name, qb=qb)
        if existing:
            vendor = existing[0]
            print(f"🟢 Vendor found: {vendor.DisplayName} (ID: {vendor.Id})")
            return vendor.Id
    except Exception as e:
        print(f"⚠️ Error searching vendor '{display_name}': {e}")

    if not ALLOW_VENDOR_CREATION:
        print(f"🚫 Vendor creation disabled in policy_config.py. Skipping creation for: {display_name}")
        return None

    vendor = Vendor()
    vendor.DisplayName = display_name
    vendor.CompanyName = display_name
    vendor.GivenName = display_name.split(" ")[0]
    vendor.FamilyName = display_name.split(" ")[-1]

    try:
        vendor.save(qb=qb)
        print(f"✅ Created new vendor: {display_name} (ID: {vendor.Id})")
        return vendor.Id
    except Exception as e:
        print(f"❌ Failed to create vendor '{display_name}': {e}")
        return None
