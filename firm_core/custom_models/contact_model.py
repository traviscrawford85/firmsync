from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

class Address(BaseModel):
    street: Optional[str]
    city: Optional[str]
    province: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]

class ContactModel(BaseModel):
    id: int
    name: str
    email: Optional[EmailStr]
    phone: Optional[str]
    type: str = "Person"
    company: Optional[str]
    addresses: List[Address] = []
