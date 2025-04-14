import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from firm_qbo.qbo_client import get_qbo_client, get_customer_id_by_name
from firm_qbo.qbo_client import get_qbo_client, create_customer_if_missing

from quickbooks.objects.customer import Customer



def create_subcustomer(contact_display_name, matter_display_name):
    qb = get_qbo_client()

    parent_customer_id = create_customer_if_missing(contact_display_name)
    if not parent_customer_id:
        print("❌ Parent customer not found. Cannot create sub-customer.")
        return

    sub_customer = Customer()
    sub_customer.GivenName = contact_display_name
    sub_customer.DisplayName = f"{contact_display_name} | {matter_display_name}"
    sub_customer.ParentRef = {"value": str(parent_customer_id)}
    sub_customer.BillWithParent = True
    sub_customer.Job = True
    sub_customer.Active = True

    try:
        sub_customer.save(qb=qb)
        print(f"✅ Sub-customer created: {sub_customer.DisplayName} (ID: {sub_customer.Id})")
    except Exception as e:
        print("❌ Failed to create sub-customer:", e)

if __name__ == "__main__":
    contact_name = "Johnathan Mitchell (Clio 2198899562)"
    matter_name = "2025-00057 Mitchell,Johnathan"
    create_subcustomer(contact_name, matter_name)
