from pydantic import BaseModel
from firm_core.custom_models.contact import ContactModel
from typing import List, Any
from typing import Optional
from datetime import datetime, date
from typing import Dict, Union

class ClientModel(ContactModel):
    is_matter_client: Optional[bool] = True
    company: Optional[ContactModel] = None
    addresses: Optional[List[Dict[str, Any]]] = None  # You can refactor with AddressModel
