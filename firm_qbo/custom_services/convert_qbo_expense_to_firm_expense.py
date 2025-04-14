# firm_qbo/custom_services/convert_qbo_expense_to_firm_expense.py


from datetime import datetime, timezone
from typing import List, Optional
from firm_qbo.custom_models.qbo_expense_model import QBOExpense
from firm_core.models import FirmExpense, FirmExpenseLineItem


def convert_qbo_expense_to_firm_expense(qbo_expense: QBOExpense) -> FirmExpense:
    line_items = [
        FirmExpenseLineItem(
            description=line.description,
            amount=line.amount,
            account=line.account_name,
            billable=(line.billable_status == "Billable")
        )
        for line in qbo_expense.lines
    ]

    return FirmExpense(
        external_id=qbo_expense.id,
        system="qbo",
        date=datetime.strptime(qbo_expense.txn_date, "%Y-%m-%d").date(),
        amount=qbo_expense.total_amount,
        vendor=qbo_expense.vendor_name,
        account_name=qbo_expense.account_name,
        note=qbo_expense.memo,
        reference=qbo_expense.id,  # You could replace this with DocNumber if available
        currency="USD",  # Pull from QBO if you add currency support later
        line_items=line_items,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )
