from firm_core.db_client.faster_suite_db_client import FasterSuiteDBClient
from firm_core.db_client.qbo_sync_db_client import QBOSyncDBClient


def seed_qbo_db_from_faster_suite():
    clio_db = FasterSuiteDBClient()
    qbo_db = QBOSyncDBClient()

    print("🔍 Reading Clio contacts and matters from Faster Suite DB...")

    # Seed Vendors from Clio Contacts
    vendors = clio_db.get_contacts_by_role("vendor")  # You may need to filter differently
    for v in vendors:
        name = v["name"]
        clio_id = v["id"]
        qbo_db.insert_vendor(name=name, qbo_id=f"clio-{clio_id}")
        print(f"✅ Vendor cached: {name}")

    # Seed Clients & Matters
    matters = clio_db.get_all_matters()
    for m in matters:
        client_name = m["client_name"]
        client_id = m["client_id"]
        matter_name = m["display_number"]
        matter_id = m["id"]

        # Insert parent (client)
        if not qbo_db.get_customer_id_by_name(client_name):
            qbo_db.insert_customer(name=client_name, qbo_id=f"clio-client-{client_id}")

        # Insert matter as sub-customer
        qbo_db.insert_customer(
            name=matter_name,
            qbo_id=f"clio-matter-{matter_id}",
            parent_id=f"clio-client-{client_id}"
        )

        print(f"📎 Matter cached: {matter_name} (under {client_name})")

    print("🎉 QBO local sync DB successfully seeded from Faster Suite.")


if __name__ == "__main__":
    seed_qbo_db_from_faster_suite()
