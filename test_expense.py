from firm_core.custom_models.firm_expense import FirmExpense, FirmExpenseLineItem
from datetime import datetime, timezone, date

expense = FirmExpense(
    external_id="12345",
    system="qbo",
    date=date.today(),
    amount=100.00,
    vendor="Amazon",
    account_name="Credit Card",
    note="Office supplies",
    reference="QBO-REF-001",
    currency="USD",
    line_items=[
        FirmExpenseLineItem(description="Paper", amount=50.00, account="Office Supplies", billable=True),
        FirmExpenseLineItem(description="Pens", amount=50.00, account="Office Supplies", billable=False),
    ],
    created_at=datetime.now(timezone.utc),
    updated_at=datetime.now(timezone.utc)

)

print(expense.json(indent=2))
