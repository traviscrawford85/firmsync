from pydantic import BaseModel
from typing import Optional

class ContactModel(BaseModel):
    id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]

    @property
    def full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}".strip()