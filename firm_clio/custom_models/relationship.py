from pydantic import BaseModel
from clio_sdk.models import ContactModel
from typing import Optional


class RelationshipModel(BaseModel):
    id: Optional[int]
    description: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
