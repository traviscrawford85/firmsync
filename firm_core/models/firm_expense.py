# firm_core/models/firm_expense.py
# this is the canonical model for firm expenses
from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel


class FirmExpenseLineItem(BaseModel):
    description: Optional[str]
    amount: float
    account: Optional[str]
    billable: bool = True


class FirmExpense(BaseModel):
    external_id: str
    system: str  # e.g., "qbo" or "clio"
    date: date
    amount: float
    vendor: Optional[str]
    account_name: Optional[str]
    note: Optional[str]
    reference: Optional[str]
    currency: str = "USD"
    line_items: List[FirmExpenseLineItem]
    created_at: datetime
    updated_at: datetime
