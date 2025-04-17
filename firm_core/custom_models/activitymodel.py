from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

class ActivityModel(BaseModel):
    
    id: Optional[str] = None  # Internal DB ID (if used)
    
    source: Literal["clio", "qbo"]  # Source system
    
    external_id: str  # ID from Clio or QBO
    
    date: datetime  # Timestamp of activity
    
    description: Optional[str] = None  # 
    
    amount: float  # Total cost or charge
    
    quantity: Optional[float] = 1.0  # 
    
    rate: Optional[float] = None  # 
    
    matter_id: Optional[str] = None  # Clio-only field
    
    contact_id: Optional[str] = None  # 
    
    contact_name: Optional[str] = None  # 
    
    type: Optional[Literal["time", "expense", "flat_fee", "purchase"]] = None  # 
    