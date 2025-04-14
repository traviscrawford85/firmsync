# firm_qbo/custom_models/qbo_expense_model.py

from pydantic import BaseModel
from typing import Optional, List


class QBOExpenseLine(BaseModel):
    amount: float
    account_name: str
    description: Optional[str]
    billable_status: Optional[str]
    item_name: Optional[str] = None
    clio_matter_id: Optional[str] = None


class QBOExpense(BaseModel):
    id: str
    txn_date: str
    total_amount: float
    vendor_name: Optional[str]
    payment_type: Optional[str]
    memo: Optional[str]
    account_name: str
    lines: List[QBOExpenseLine]
    clio_matter_id: Optional[str] = None
