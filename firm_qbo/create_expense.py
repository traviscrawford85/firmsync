# firm_qbo/create_expense.py

from quickbooks.objects.purchase import Purchase
from quickbooks.objects.base import Ref
from firm_qbo.qbo_client import qb_client


# This function creates an expense for a sub-customer (matter) in QuickBooks Online.
def create_expense(sub_customer_id, amount=150.00, memo="Filing Fee"):
    purchase = Purchase()
    purchase.PaymentType = "Cash"
    purchase.TotalAmt = amount
    purchase.Memo = memo
    purchase.AccountRef = Ref(value="82")  # Common sandbox account: Advanced Client Costs

    purchase.EntityRef = Ref(value=sub_customer_id, type="Customer")  # Must be set for sub-customer

    purchase.Line = [{
        "Amount": amount,
        "DetailType": "AccountBasedExpenseLineDetail",
        "AccountBasedExpenseLineDetail": {
            "AccountRef": {"value": "82"}
        }
    }]

    result = purchase.save(qb=client)
    print(f"✅ Expense created: ${amount} for Sub-Customer ID {sub_customer_id}")
    return result


if __name__ == "__main__":
    # Example usage
    sub_customer_id = "123456789"  # Replace with the actual sub-customer ID
    expense = create_expense(sub_customer_id)
    print(f"Expense ID: {expense.Id}")
    print(f"Expense Amount: {expense.TotalAmt}")
    print(f"Expense Memo: {expense.Memo}")
    print(f"Expense EntityRef: {expense.EntityRef.value}")