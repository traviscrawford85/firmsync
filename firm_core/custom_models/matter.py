from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class MatterModel(BaseModel):
    id: Optional[int]
    display_number: Optional[str]
    custom_number: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    location: Optional[str] = None
    client_reference: Optional[str] = None
    client_id: Optional[int] = None
    client_name: Optional[str] = None  # 👈 New field
    practice_area_name: Optional[str] = None  # 👈 New field
    billable: Optional[bool] = None
    open_date: Optional[date] = None
    close_date: Optional[date] = None
    pending_date: Optional[date] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    shared: Optional[bool] = None
    has_tasks: Optional[bool] = None
    last_activity_date: Optional[date] = None
    matter_stage_updated_at: Optional[datetime] = None
    currency: Optional[dict] = None
    matter_stage_id: Optional[int] = None
    matter_stage_name: Optional[str] = None
    maildrop_address: Optional[str] = None
    billing_method: Optional[str] = None


    def __str__(self):
        return (
            f"🗂️ Matter ID: {self.id}\n"
            f"📎 Display #: {self.display_number}\n"
            f"📝 Description: {self.description or 'N/A'}\n"
            f"📌 Status: {self.status or 'N/A'}\n"
            f"🏷️  Custom #: {self.custom_number or 'N/A'}\n"
            f"📍 Location: {self.location or 'N/A'}\n"
            f"👤 Client ID: {self.client_id or 'N/A'} | {self.client_name or 'N/A'}\n"
            f"💬 Client Ref: {self.client_reference or 'N/A'}\n"
            f"⚖️ Practice Area: {self.practice_area_name or 'N/A'}\n"
            f"💰 Billable: {self.billable if self.billable is not None else 'N/A'}\n"
            f"📅 Open: {self.open_date or 'N/A'} | Close: {self.close_date or 'N/A'} | Pending: {self.pending_date or 'N/A'}\n"
            f"🧾 Billing Method: {self.billing_method or 'N/A'}\n"
            f"🕓 Last Activity: {self.last_activity_date or 'N/A'}\n"
            f"{'-'*40}"
        )

    def is_open(self) -> bool:
        return self.status == "open"

    def is_closed(self) -> bool:
        return self.status == "closed"
