# firm_qbo/custom_services/qbo_expense_parser.py

from firm_qbo.custom_models.qbo_expense_model import QBOExpense, QBOExpenseLine
from utils.helpers import extract_clio_matter_id_from_qbo
from typing import Dict
from datetime import datetime



def parse_qbo_purchase(purchase_data: Dict) -> QBOExpense:
    lines = []

    for line in purchase_data.get("Line", []):
        detail = line.get("AccountBasedExpenseLineDetail", {}) or line.get("ItemBasedExpenseLineDetail", {})
        line_model = QBOExpenseLine(
            amount=line.get("Amount"),
            account_name=detail.get("AccountRef", {}).get("name", ""),
            description=line.get("Description"),
            billable_status=detail.get("BillableStatus"),
            item_name=detail.get("ItemRef", {}).get("name") if "ItemRef" in detail else None
        )
        lines.append(line_model)

    return QBOExpense(
        id=purchase_data.get("Id"),
        txn_date=purchase_data.get("TxnDate"),
        total_amount=purchase_data.get("TotalAmt"),
        vendor_name=purchase_data.get("EntityRef", {}).get("name"),
        payment_type=purchase_data.get("PaymentType"),
        memo=purchase_data.get("PrivateNote"),
        account_name=purchase_data.get("AccountRef", {}).get("name", ""),
        lines=lines,
        clio_matter_id=extract_clio_matter_id(purchase_data)
    )



# Function to extract Clio Matter ID from QBO Purchase object
def extract_clio_matter_id(purchase_data: dict) -> str:
    return extract_clio_matter_id_from_qbo(purchase_data)
