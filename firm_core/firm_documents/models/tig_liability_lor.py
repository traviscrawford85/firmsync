from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class ClientInfo(BaseModel):
    name: str = Field(..., alias="Matter.Client.Name")
    address: str = Field(..., alias="Matter.Client.Address")


class DefendantInsuranceCompany(BaseModel):
    name: str = Field(..., alias="Matter.Relationships.Defendant'sInsuranceCompany.Name")
    address: str = Field(..., alias="Matter.Relationships.Defendant'sInsuranceCompany.Address")


class MatterCustomFields(BaseModel):
    coach_number: str = Field(..., alias="Matter.CustomField.CoachNo")
    cross_streets: str = Field(..., alias="Matter.CustomField.CrossStreets")
    date_of_incident: date = Field(..., alias="Matter.CustomField.DateOfIncident")
    defendants_insurance_claim_no: str = Field(..., alias="Matter.CustomField.DefendantsInsuranceClaimNo")
    description_of_incident: str = Field(..., alias="Matter.CustomField.DescriptionOfIncident")
    incident_location_city: str = Field(..., alias="Matter.CustomField.IncidentLocationCity")
    incident_location_state: str = Field(..., alias="Matter.CustomField.IncidentLocationState")
    line_number: str = Field(..., alias="Matter.CustomField.LineNo")
    transit_agency: str = Field(..., alias="Matter.CustomField.TransitAgency")
    user_initials: str = Field(..., alias="Matter.CustomField.UserInitials")


class MatterInfo(BaseModel):
    client: ClientInfo
    custom: MatterCustomFields
    relationships: DefendantInsuranceCompany


class TIGLiabilityLOR(BaseModel):
    matter: MatterInfo
    date_verbose: Optional[str] = Field(default_factory=lambda: date.today().strftime("%B %d, %Y"), alias="Date.Verbose")
