from pydantic import BaseModel
from clio_sdk.models import ContactModel
from typing import Optional

class RelatedContactModel(BaseModel):
    contact_id: Optional[int]
    name: Optional[str]
    type: Optional[str]
    relationship_description: Optional[str]  # Optional custom descriptor
