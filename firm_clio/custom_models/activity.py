from pydantic import BaseModel, Field
from typing import Optional, Union, Dict
from datetime import datetime, date

class ActivityModel(BaseModel):
    id: Optional[int]
    etag: Optional[str]
    type: Optional[str]  # TimeEntry, ExpenseEntry, etc.
    date: Optional[date]
    quantity_in_hours: Optional[float]
    rounded_quantity_in_hours: Optional[float]
    quantity: Optional[float]  # in seconds (as of v4.0.4+)
    rounded_quantity: Optional[float]
    quantity_redacted: Optional[bool]
    price: Optional[float]
    note: Optional[str]
    flat_rate: Optional[bool]
    billed: Optional[bool]
    on_bill: Optional[bool]
    total: Optional[float]
    contingency_fee: Optional[bool]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    reference: Optional[str]
    non_billable: Optional[bool]
    non_billable_total: Optional[float]
    no_charge: Optional[bool]
    tax_setting: Optional[str]  # no_tax, tax_1_only, etc.
    currency: Optional[Dict[str, Union[str, float]]]

    def is_billable(self) -> bool:
        return not self.non_billable if self.non_billable is not None else False

    def is_redacted(self) -> bool:
        return self.quantity_redacted is True
