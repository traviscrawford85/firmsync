from pydantic import BaseModel
from clio_sdk.models import ContactModel
from typing import Optional
from datetime import datetime, date
from typing import Dict, Union

class ClientModel(ContactModel):
    is_matter_client: Optional[bool] = True
    company: Optional[ContactModel] = None
    addresses: Optional[List[Dict[str, Any]]] = None  # You can refactor with AddressModel
