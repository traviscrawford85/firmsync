from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class PipAdjusterInfo(BaseModel):
    fax_number: str = Field(..., alias="Matter.Relationships.ClientsPipAdjuster.PrimaryFaxNumber")
    address: str = Field(..., alias="Matter.Relationships.ClientsPipAdjuster.Address")
    name: str = Field(..., alias="Matter.Relationships.ClientsPipAdjuster.Name")
    prefix: str = Field(..., alias="Matter.Relationships.ClientsPipAdjuster.Prefix")
    last_name: str = Field(..., alias="Matter.Relationships.ClientsPipAdjuster.LastName")


class CustomFields(BaseModel):
    insurance_name: str = Field(..., alias="Matter.CustomField.ClientAutoInsuranceName")
    claim_number: str = Field(..., alias="Matter.CustomField.ClientAutoInsuranceClaimNo")
    date_of_incident: date = Field(..., alias="Matter.CustomField.DateOfIncident")
    user_initials: str = Field(..., alias="Matter.CustomField.UserInitials")


class MatterInfo(BaseModel):
    client_name: str = Field(..., alias="Matter.Client.Name")
    adjuster: PipAdjusterInfo
    custom_fields: CustomFields


class PipLetterOfRepresentation(BaseModel):
    matter: MatterInfo
    date_verbose: Optional[str] = Field(default_factory=lambda: date.today().strftime("%B %d, %Y"), alias="Date.Verbose")
