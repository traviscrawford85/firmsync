from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class VendorModel(BaseModel):
    Id: Optional[str]
    DisplayName: Optional[str]
    CompanyName: Optional[str]
    GivenName: Optional[str]
    MiddleName: Optional[str]
    FamilyName: Optional[str]
    Suffix: Optional[str]
    Title: Optional[str]
    PrimaryEmailAddr: Optional[EmailAddress]
    PrimaryPhone: Optional[PhoneNumber]
    Mobile: Optional[PhoneNumber]
    Fax: Optional[PhoneNumber]
    AlternatePhone: Optional[PhoneNumber]
    Active: Optional[bool]
    Balance: Optional[float]
    BillAddr: Optional[Address]
    TaxIdentifier: Optional[str]
    TermRef: Optional[dict]
    AcctNum: Optional[str]
    CurrencyRef: Optional[dict]
    Vendor1099: Optional[bool]
    CustomField: Optional[List[dict]]
    MetaData: Optional[dict]
