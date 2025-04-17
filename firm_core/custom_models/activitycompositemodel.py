from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

class (BaseModel):
    
    id: Optional[str] = None  # 
    
    external_id: Optional[str] = None  # 
    
    source: Optional[Literal['clio', 'qbo']] = None  # 
    
    date: Optional[datetime] = None  # 
    
    description: Optional[str] = None  # 
    
    amount: Optional[float] = None  # 
    
    quantity: Optional[float] = None  # 
    
    rate: Optional[float] = None  # 
    
    type: Optional[Literal['time', 'expense', 'flat_fee', 'purchase']] = None  # 
    
    matter_id: Optional[str] = None  # 
    
    contact_id: Optional[str] = None  # 
    
    contact_name: Optional[str] = None  # 
    
    qbo_vendor_id: Optional[str] = None  # 
    
    qbo_account_id: Optional[str] = None  # 
    
    qbo_item_id: Optional[str] = None  # 
    
    qbo_customer_id: Optional[str] = None  # 
    
    qbo_synced_at: Optional[datetime] = None  # 
    
    status: Optional[Literal['draft', 'synced', 'error']] = None  # 
    