# firm_core/custom_models/activity.py

from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

class ActivityModel(BaseModel):
    id: Optional[str]                               # Internal DB ID (if used)
    source: Literal["clio", "qbo"]                  # Source system
    external_id: str                                # ID from Clio or QBO
    date: datetime                                  # Timestamp of activity
    description: Optional[str]
    amount: float                                    # Total cost/charge
    quantity: Optional[float] = 1.0                  # Optional for time/qty
    rate: Optional[float] = None                     # Useful for Clio time entries
    matter_id: Optional[str]                         # Clio only
    contact_id: Optional[str]                        # Shared if mapped
    contact_name: Optional[str]  # Add this to ActivityModel
    type: Optional[Literal["time", "expense", "flat_fee", "purchase"]] = None
