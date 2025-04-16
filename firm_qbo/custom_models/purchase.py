from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class ReferenceType(BaseModel):
    value: Optional[str]
    name: Optional[str]

class Line(BaseModel):
    Id: Optional[str]
    LineNum: Optional[int]
    Description: Optional[str]
    Amount: Optional[float]
    DetailType: Optional[str]
    AccountBasedExpenseLineDetail: Optional[dict]

class PurchaseModel(BaseModel):
    Id: Optional[str]
    DocNumber: Optional[str]
    TxnDate: Optional[datetime]
    PrivateNote: Optional[str]
    Line: Optional[List[Line]]
    VendorRef: Optional[ReferenceType]
    AccountRef: Optional[ReferenceType]
    PaymentType: Optional[str]
    TotalAmt: Optional[float]
    CurrencyRef: Optional[ReferenceType]
    ExchangeRate: Optional[float]
    EntityRef: Optional[ReferenceType]
    DepartmentRef: Optional[ReferenceType]
    MetaData: Optional[dict]
