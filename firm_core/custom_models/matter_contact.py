from pydantic import BaseModel
from clio_sdk.models import ContactModel
from typing import Optional

class MatterContactModel(ContactModel):
    matter_id: Optional[int]
    relationship_name: Optional[str]
    client_connect_user_id: Optional[int]
