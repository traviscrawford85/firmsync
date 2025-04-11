# firm_qbo/create_customer.py

from quickbooks.objects.customer import Customer
from quickbooks.objects.base import Ref
from firm_qbo.qbo_client import qb_client


# This function creates a new customer in QuickBooks Online using the QuickBooks Python SDK.
def create_customer(display_name="John Doe", email="john.doe@example.com"):
    customer = Customer()
    customer.DisplayName = display_name
    customer.PrimaryEmailAddr = {"Address": email}
    customer.CompanyName = "Doe Legal Services"

    result = customer.save(qb=qb_client)
    print(f"✅ Customer created: {result.DisplayName} (ID: {result.Id})")
    return result


if __name__ == "__main__":
    # Example usage
    customer = create_customer()
    print(f"Customer ID: {customer.Id}")
    print(f"Customer Display Name: {customer.DisplayName}")
    print(f"Customer Email: {customer.PrimaryEmailAddr['Address']}")
