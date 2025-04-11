# firm_qbo/create_subcustomer.py

from quickbooks.objects.customer import Customer
from quickbooks.objects.base import Ref
from firm_qbo.qbo_client import qb_client

# This function creates a sub-customer (matter) under a parent customer in QuickBooks Online.
def create_sub_customer(parent_id, display_name="2025-00001 Doe,John"):
    sub_customer = Customer()
    sub_customer.DisplayName = display_name
    sub_customer.ParentRef = Ref(value=parent_id)
    sub_customer.BillWithParent = False  # Important: matters are separate billable entities

    result = sub_customer.save(qb=client)
    print(f"✅ Sub-Customer (Matter) created: {result.DisplayName} (ID: {result.Id})")
    return result

if __name__ == "__main__":
    # Example usage
    parent_id = "123456789"  # Replace with the actual parent customer ID
    sub_customer = create_sub_customer(parent_id)
    print(f"Sub-Customer ID: {sub_customer.Id}")
    print(f"Sub-Customer Display Name: {sub_customer.DisplayName}")
    print(f"Sub-Customer Parent ID: {sub_customer.ParentRef.value}")
