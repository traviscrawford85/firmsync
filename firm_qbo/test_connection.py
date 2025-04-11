import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from firm_qbo.qbo_client import get_qbo_client
from quickbooks.objects.customer import Customer


# This script is used to test the connection to QuickBooks Online and fetch a list of customers.
# It uses the QuickBooks Python SDK to interact with the QuickBooks API.
def test_get_customers():
    try:
        qb = get_qbo_client()
        print("🔎 Fetching customers...")

        customers = Customer.all(qb=qb)  # Correct SDK keyword is `qb`

        print("✅ Customers fetched successfully!")
        print(f"📊 Found {len(customers)} customers:")
        for customer in customers:
            print(f"🧾 Customer ID: {customer.Id}, Name: {customer.DisplayName}")

    except Exception as e:
        print("❌ Failed to fetch customers from QuickBooks.")
        print("🧠 Error details:", e)

if __name__ == "__main__":
    test_get_customers()
