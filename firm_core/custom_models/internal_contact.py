import pydantic
from pydantic import BaseModel
from typing import Optional, Literal

class InternalContact(BaseModel):
    id: str
    type: Literal["client", "vendor", "witness", "company"]
    name: str
    email: Optional[str]
    phone: Optional[str]
    clio_id: Optional[int]
    qbo_id: Optional[str]
