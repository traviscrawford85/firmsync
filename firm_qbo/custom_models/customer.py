from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class Address(BaseModel):
    Id: Optional[str]
    Line1: Optional[str]
    Line2: Optional[str]
    Line3: Optional[str]
    Line4: Optional[str]
    Line5: Optional[str]
    City: Optional[str]
    Country: Optional[str]
    CountrySubDivisionCode: Optional[str]
    PostalCode: Optional[str]
    Lat: Optional[str]
    Long: Optional[str]

class EmailAddress(BaseModel):
    Address: Optional[str]

class PhoneNumber(BaseModel):
    FreeFormNumber: Optional[str]

class CustomerModel(BaseModel):
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
    BalanceWithJobs: Optional[float]
    BillAddr: Optional[Address]
    ShipAddr: Optional[Address]
    Taxable: Optional[bool]
    ResaleNum: Optional[str]
    PreferredDeliveryMethod: Optional[str]
    Notes: Optional[str]
    Job: Optional[bool]
    ParentRef: Optional[dict]
    Level: Optional[int]
    SalesTermRef: Optional[dict]
    PaymentMethodRef: Optional[dict]
    CurrencyRef: Optional[dict]
    OpenBalanceDate: Optional[datetime]
    CustomField: Optional[List[dict]]
    MetaData: Optional[dict]
