import pydantic
from pydantic import BaseModel
from typing import Optional, Literal

class InternalExpense(BaseModel):
    id: str
    source: Literal["clio", "qbo"]
    amount: float
    vendor_name: Optional[str]
    vendor_id: Optional[str]
    clio_matter_id: Optional[int]
    qbo_account_ref: Optional[str]
    description: str
    date: datetime
    synced: bool = False
