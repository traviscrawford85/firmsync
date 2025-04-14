from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class MatterModel(BaseModel):
    id: Optional[int]
    display_number: Optional[str]
    custom_number: Optional[str]
    description: Optional[str]
    status: Optional[str]
    location: Optional[str]
    client_reference: Optional[str]
    client_id: Optional[int]
    billable: Optional[bool]
    open_date: Optional[date]
    close_date: Optional[date]
    pending_date: Optional[date]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    shared: Optional[bool]
    has_tasks: Optional[bool]
    last_activity_date: Optional[date]
    matter_stage_updated_at: Optional[datetime]
    currency: Optional[dict]
    matter_stage_id: Optional[int]
    matter_stage_name: Optional[str]
    maildrop_address: Optional[str]
    billing_method: Optional[str]
    

    def __str__(self):
        return f"Matter({self.display_number} - {self.status})"

    def is_open(self) -> bool:
        return self.status == "open"

    def is_closed(self) -> bool:
        return self.status == "closed"