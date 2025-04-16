from pydantic import BaseModel
from typing import Optional

from datetime import datetime, date
from typing import Dict, Union

class ContactModel(BaseModel):
    id: Optional[int]
    etag: Optional[str]
    name: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    date_of_birth: Optional[date]
    type: Optional[str]  # Company or Person
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    prefix: Optional[str]
    title: Optional[str]
    initials: Optional[str]
    clio_connect_email: Optional[str]
    locked_clio_connect_email: Optional[bool]
    client_connect_user_id: Optional[int]
    primary_email_address: Optional[str]
    secondary_email_address: Optional[str]
    primary_phone_number: Optional[str]
    secondary_phone_number: Optional[str]
    ledes_client_id: Optional[str]
    has_clio_for_clients_permission: Optional[bool]
    is_client: Optional[bool]
    is_clio_for_client_user: Optional[bool]
    is_co_counsel: Optional[bool]
    is_bill_recipient: Optional[bool]
    sales_tax_number: Optional[str]
    currency: Optional[Dict[str, Union[str, float]]]

    def is_individual(self) -> bool:
        return self.type == "Person"

    def is_company(self) -> bool:
        return self.type == "Company"

    @property
    def full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}".strip()