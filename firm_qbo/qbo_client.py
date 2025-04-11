import os
from firm_auth.oauth_flow import load_authenticated_client
from quickbooks import QuickBooks
from quickbooks.objects.customer import Customer

def get_qbo_client():
    auth_client = load_authenticated_client()

    return QuickBooks(
        sandbox=True,
        auth_client=auth_client,
        refresh_token=auth_client.refresh_token,
        company_id=os.getenv("QB_REALM_ID")
    )
# this function will Searches Quickbooks online for a customer with an exact display name match
# and returns the customer ID if found, or None if not found.
def get_customer_id_by_name(display_name):
    qb = get_qbo_client()

    try:
        customers = Customer.filter(DisplayName=display_name, qb=qb)
        if customers:
            print(f"🔍 Found customer: {customers[0].DisplayName} (ID: {customers[0].Id})")
            return customers[0].Id
        else:
            print(f"⚠️ No customer found with display name: {display_name}")
            return None
    except Exception as e:
        print("❌ Error searching for customer:", e)
        return None
    

# this function will create a new customer if one does not exist with the same display name
def create_customer_if_missing(display_name):
    from quickbooks.objects.customer import Customer

    qb = get_qbo_client()

    # First try to find the customer
    try:
        existing = Customer.filter(DisplayName=display_name, qb=qb)
        if existing:
            print(f"🟢 Customer already exists: {display_name} (ID: {existing[0].Id})")
            return existing[0].Id
    except Exception as e:
        print(f"⚠️ Error searching for existing customer '{display_name}': {e}")

    # If not found, create a new one
    new_customer = Customer()
    new_customer.DisplayName = display_name
    new_customer.GivenName = display_name.split(" ")[0]  # Simple default logic
    new_customer.FamilyName = display_name.split(" ")[-1]
    new_customer.CompanyName = display_name  # Optional

    try:
        new_customer.save(qb=qb)
        print(f"✅ Created new customer: {display_name} (ID: {new_customer.Id})")
        return new_customer.Id
    except Exception as e:
        print("❌ Failed to create new customer:", e)
        return None
