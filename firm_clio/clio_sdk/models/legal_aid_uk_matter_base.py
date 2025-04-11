# coding: utf-8

"""
    Clio API Documentation

    # Developer Support and Feedback * Clio takes the availability and stability of our API seriously; please report any **degradations** or **breakages** to Clio's API Support team at [api@clio.com](mailto:api@clio.com). * For business and partnership inquiries, contact our API Partnerships team at [api.partnerships@clio.com](mailto:api.partnerships@clio.com). * For best practices and tips from the Clio development community, join the conversation in the [Clio Developer Slack Channel](https://join.slack.com/t/clio-public/shared_invite/zt-1bd5nfbiv-WloZR3ZjepoUTv28SI1ezw).  A community-driven [Clio Developers Stack Overflow Group](https://stackoverflow.com/questions/tagged/clio-api) also exists where you can connect and ask questions from other Clio API users. # Getting Started > **Note:** The API is available in four distinct data regions: Australia (au.app.clio.com), Canada (ca.app.clio.com), EU (eu.app.clio.com) and US (app.clio.com). > > Likewise, the developer portal is available at region-specific links for the [Australia](https://au.developers.clio.com), [Canada](https://ca.developers.clio.com), [EU](https://eu.developers.clio.com), and [US](https://developers.clio.com) regions. > > This document assumes the US region is being used (app.clio.com). If you're building in one of the other regions, you should adapt the links and examples as necessary.  To start building on the Clio API, you’ll need a Clio account – you can review our [Developer Handbook](https://docs.developers.clio.com/) and follow the steps to sign up for an account.  Once you have an account, you can [create a developer application](https://docs.developers.clio.com/api-docs/applications) from the [Developer Portal](https://developers.clio.com) and start building! # Authorization with OAuth 2.0 See our [Authorization documentation →](https://docs.developers.clio.com/api-docs/authorization) # Permissions See our [Permissions documentation →](https://docs.developers.clio.com/api-docs/permissions) # Fields See our [Fields documentation →](https://docs.developers.clio.com/api-docs/fields) # Rate Limiting See our [Rate Limits documentation →](https://docs.developers.clio.com/api-docs/rate-limits) # Paging See our [Pagination documentation →](https://docs.developers.clio.com/api-docs/paging) # ETags See our [ETags documentation →](https://docs.developers.clio.com/api-docs/etags) # Minor Versions API v4 supports multiple minor versions. Versions are of the form '4.X.Y'. To request a specific version, you can use an `X-API-VERSION` header in your request, with the header value set to the API version you're requesting. If this header is omitted, it will be treated as a request for the default API version. If the header is present but invalid, it will return a `410 Gone` response. If the header is present and valid, but it is no longer supported, it will return a `410 Gone` response.  An `X-API-VERSION` will be included in all successful responses, with the value being set to the API version used.  You can find our [API Versioning Policy and Guidelines](https://docs.developers.clio.com/api-docs/api-versioning-policy) in our documentation hub.  The [API Changelog](https://docs.developers.clio.com/api-docs/api-changelog) explains each version's changes in further detail. - 4.0.4    Update `quantity` field to return values in seconds rather than hours for Activities  - 4.0.5    * Remove `matter_balances` field from Bills   * Standardize status/state enum values   * Add a Document association to completed DocumentAutomations   * Add rate visibility handling for Activity's price and total  - 4.0.6    Remove `document_versions` collection field from Documents  - 4.0.7    Change secure link format  - 4.0.8    * `Activity` hours are redacted in the response based on the activity hours visibility setting for the user   * Add `quantity_redacted` field to activities  - 4.0.9    **This is the default version**    Contacts are filtered and redacted in the response based on the new 'Contacts Visibility' user permission setting.  - 4.0.10    Fixed validation of `type` query parameter when querying Notes   

    The version of the OpenAPI document: v4
    Contact: api@clio.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class LegalAidUkMatterBase(BaseModel):
    """
    LegalAidUkMatterBase
    """ # noqa: E501
    access_point: Optional[StrictStr] = Field(default=None, description="Access point")
    laa_office_number: Optional[StrictStr] = Field(default=None, description="LAA office number")
    ait_hearing_centre: Optional[StrictInt] = Field(default=None, description="AIT hearing centre")
    attended_several_hearings_acting_for_multiple_clients: Optional[StrictBool] = Field(default=None, description="Attended several hearings acting for multiple clients")
    bill_ho_ucn: Optional[StrictStr] = Field(default=None, description="Bill HO UCN")
    bill_number_of_attendances: Optional[StrictInt] = Field(default=None, description="Bill number of attendances")
    bill_outcome_for_the_client_code: Optional[StrictInt] = Field(default=None, description="Bill outcome for the client code")
    bill_stage_reached_code: Optional[StrictInt] = Field(default=None, description="Bill stage reached code")
    case_reference: Optional[StrictStr] = Field(default=None, description="Case reference")
    case_start_date: Optional[date] = Field(default=None, description="Case start date")
    category: Optional[StrictInt] = Field(default=None, description="Category")
    category_as_string: Optional[StrictStr] = Field(default=None, description="Category as string")
    certificate_effective_date: Optional[date] = Field(default=None, description="Certificate effective date")
    certificate_expiration_date: Optional[date] = Field(default=None, description="Certificate expiration date")
    certificate_number: Optional[StrictStr] = Field(default=None, description="Certificate number")
    certificate_scope: Optional[StrictStr] = Field(default=None, description="Certificate scope")
    certification_type: Optional[StrictInt] = Field(default=None, description="Certification type")
    change_of_solicitor: Optional[StrictBool] = Field(default=None, description="Change of solicitor")
    client_equal_opportunity_monitoring: Optional[StrictStr] = Field(default=None, description="Client equal opportunity monitoring")
    client_type: Optional[StrictInt] = Field(default=None, description="Client type")
    clr_start_date: Optional[date] = Field(default=None, description="CLR start date")
    clr_total_profit_costs: Optional[StrictStr] = Field(default=None, description="CLR total profit costs")
    cost_limit: Optional[StrictStr] = Field(default=None, description="Cost limit")
    counsel: Optional[StrictInt] = Field(default=None, description="Counsel")
    court: Optional[StrictInt] = Field(default=None, description="Court")
    court_id: Optional[StrictInt] = Field(default=None, description="Court ID")
    court_id_code: Optional[StrictStr] = Field(default=None, description="Court ID code")
    created_at: Optional[datetime] = Field(default=None, description="The time the *LegalAidUkMatter* was created (as a ISO-8601 timestamp)")
    delivery_location: Optional[StrictStr] = Field(default=None, description="Delivery location")
    dscc_number: Optional[StrictStr] = Field(default=None, description="DSCC number")
    duty_solicitor: Optional[StrictBool] = Field(default=None, description="Duty solicitor")
    etag: Optional[StrictStr] = Field(default=None, description="ETag for the *LegalAidUkMatter*")
    exceptional_case_funding_reference: Optional[StrictStr] = Field(default=None, description="Exceptional case funding reference")
    expense_limit: Optional[StrictStr] = Field(default=None, description="Expense limit")
    fee_scheme: Optional[StrictInt] = Field(default=None, description="Fee scheme")
    first_conducting_solicitor: Optional[StrictBool] = Field(default=None, description="First conducting solicitor")
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier for the *LegalAidUkMatter*")
    irc_surgery: Optional[StrictStr] = Field(default=None, description="Irc surgery")
    legacy_case: Optional[StrictStr] = Field(default=None, description="Legacy case")
    legal_representation_number: Optional[StrictStr] = Field(default=None, description="Legal representation number")
    lh_total_disbursements: Optional[StrictStr] = Field(default=None, description="LH total disbursements")
    lh_start_date: Optional[StrictStr] = Field(default=None, description="LH start date")
    lh_total_profit_costs: Optional[StrictStr] = Field(default=None, description="LH total profit costs")
    linked_matter_id: Optional[StrictInt] = Field(default=None, description="Linked matter ID")
    local_authority_number: Optional[StrictStr] = Field(default=None, description="Local authority number")
    maat_id: Optional[StrictStr] = Field(default=None, description="MAAT ID")
    matter_type: Optional[StrictInt] = Field(default=None, description="Matter type")
    matter_type_code: Optional[StrictStr] = Field(default=None, description="Matter type code")
    matter_type_1: Optional[StrictInt] = Field(default=None, description="Matter type 1")
    matter_type_1_code: Optional[StrictStr] = Field(default=None, description="Matter type 1 code")
    matter_type_1_title: Optional[StrictStr] = Field(default=None, description="Matter type 1 title")
    matter_type_2: Optional[StrictInt] = Field(default=None, description="Matter type 2")
    matter_type_2_code: Optional[StrictStr] = Field(default=None, description="Matter type 2 code")
    matter_type_2_title: Optional[StrictStr] = Field(default=None, description="Matter type 2 title")
    matter_types_combined: Optional[StrictStr] = Field(default=None, description="Matter types combined")
    number_of_clients_seen_at_surgery: Optional[StrictInt] = Field(default=None, description="Number of clients seen at surgery")
    number_of_clients: Optional[StrictInt] = Field(default=None, description="Number of clients")
    party: Optional[StrictInt] = Field(default=None, description="Party")
    police_station: Optional[StrictStr] = Field(default=None, description="Police station")
    post_transfer_clients_represented: Optional[StrictInt] = Field(default=None, description="Post transfer clients represented")
    postal_application_accepted: Optional[StrictStr] = Field(default=None, description="Postal application accepted")
    prior_authority_reference: Optional[StrictStr] = Field(default=None, description="Priory authority reference")
    prison_id: Optional[StrictInt] = Field(default=None, description="Prison ID")
    prison_law_prior_approval_number: Optional[StrictStr] = Field(default=None, description="Prison law prior approval number")
    procurement_area: Optional[StrictStr] = Field(default=None, description="Procurement area")
    region: Optional[StrictInt] = Field(default=None, description="Region")
    related_claims_number: Optional[StrictStr] = Field(default=None, description="Related claims number")
    representation_order_date: Optional[date] = Field(default=None, description="Representation order date")
    schedule_reference_number: Optional[StrictStr] = Field(default=None, description="Schedule reference number")
    scheme_id: Optional[StrictStr] = Field(default=None, description="Scheme ID")
    session_type: Optional[StrictInt] = Field(default=None, description="Session type")
    solicitor_type: Optional[StrictInt] = Field(default=None, description="Solicitor type")
    standard_fee_category: Optional[StrictInt] = Field(default=None, description="Standard fee category")
    surgery_clients_resulting_in_a_legal_help_matter_opened: Optional[StrictInt] = Field(default=None, description="Surgery clients resulting in a legal help matter opened")
    surgery_clients: Optional[StrictInt] = Field(default=None, description="Surgery clients")
    surgery_date: Optional[date] = Field(default=None, description="Surgery date")
    transfer_date: Optional[date] = Field(default=None, description="Transfer date")
    type_of_advice: Optional[StrictInt] = Field(default=None, description="Type of advice")
    type_of_service: Optional[StrictStr] = Field(default=None, description="Type of service")
    ucn: Optional[StrictStr] = Field(default=None, description="UCN")
    ufn: Optional[StrictStr] = Field(default=None, description="UFN")
    undesignated_area_court: Optional[StrictBool] = Field(default=None, description="Undesignated area court")
    updated_at: Optional[datetime] = Field(default=None, description="The time the *LegalAidUkMatter* was last updated (as a ISO-8601 timestamp)")
    user_type: Optional[StrictInt] = Field(default=None, description="User type")
    youth_court: Optional[StrictBool] = Field(default=None, description="Youth court")
    __properties: ClassVar[List[str]] = ["access_point", "laa_office_number", "ait_hearing_centre", "attended_several_hearings_acting_for_multiple_clients", "bill_ho_ucn", "bill_number_of_attendances", "bill_outcome_for_the_client_code", "bill_stage_reached_code", "case_reference", "case_start_date", "category", "category_as_string", "certificate_effective_date", "certificate_expiration_date", "certificate_number", "certificate_scope", "certification_type", "change_of_solicitor", "client_equal_opportunity_monitoring", "client_type", "clr_start_date", "clr_total_profit_costs", "cost_limit", "counsel", "court", "court_id", "court_id_code", "created_at", "delivery_location", "dscc_number", "duty_solicitor", "etag", "exceptional_case_funding_reference", "expense_limit", "fee_scheme", "first_conducting_solicitor", "id", "irc_surgery", "legacy_case", "legal_representation_number", "lh_total_disbursements", "lh_start_date", "lh_total_profit_costs", "linked_matter_id", "local_authority_number", "maat_id", "matter_type", "matter_type_code", "matter_type_1", "matter_type_1_code", "matter_type_1_title", "matter_type_2", "matter_type_2_code", "matter_type_2_title", "matter_types_combined", "number_of_clients_seen_at_surgery", "number_of_clients", "party", "police_station", "post_transfer_clients_represented", "postal_application_accepted", "prior_authority_reference", "prison_id", "prison_law_prior_approval_number", "procurement_area", "region", "related_claims_number", "representation_order_date", "schedule_reference_number", "scheme_id", "session_type", "solicitor_type", "standard_fee_category", "surgery_clients_resulting_in_a_legal_help_matter_opened", "surgery_clients", "surgery_date", "transfer_date", "type_of_advice", "type_of_service", "ucn", "ufn", "undesignated_area_court", "updated_at", "user_type", "youth_court"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of LegalAidUkMatterBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LegalAidUkMatterBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access_point": obj.get("access_point"),
            "laa_office_number": obj.get("laa_office_number"),
            "ait_hearing_centre": obj.get("ait_hearing_centre"),
            "attended_several_hearings_acting_for_multiple_clients": obj.get("attended_several_hearings_acting_for_multiple_clients"),
            "bill_ho_ucn": obj.get("bill_ho_ucn"),
            "bill_number_of_attendances": obj.get("bill_number_of_attendances"),
            "bill_outcome_for_the_client_code": obj.get("bill_outcome_for_the_client_code"),
            "bill_stage_reached_code": obj.get("bill_stage_reached_code"),
            "case_reference": obj.get("case_reference"),
            "case_start_date": obj.get("case_start_date"),
            "category": obj.get("category"),
            "category_as_string": obj.get("category_as_string"),
            "certificate_effective_date": obj.get("certificate_effective_date"),
            "certificate_expiration_date": obj.get("certificate_expiration_date"),
            "certificate_number": obj.get("certificate_number"),
            "certificate_scope": obj.get("certificate_scope"),
            "certification_type": obj.get("certification_type"),
            "change_of_solicitor": obj.get("change_of_solicitor"),
            "client_equal_opportunity_monitoring": obj.get("client_equal_opportunity_monitoring"),
            "client_type": obj.get("client_type"),
            "clr_start_date": obj.get("clr_start_date"),
            "clr_total_profit_costs": obj.get("clr_total_profit_costs"),
            "cost_limit": obj.get("cost_limit"),
            "counsel": obj.get("counsel"),
            "court": obj.get("court"),
            "court_id": obj.get("court_id"),
            "court_id_code": obj.get("court_id_code"),
            "created_at": obj.get("created_at"),
            "delivery_location": obj.get("delivery_location"),
            "dscc_number": obj.get("dscc_number"),
            "duty_solicitor": obj.get("duty_solicitor"),
            "etag": obj.get("etag"),
            "exceptional_case_funding_reference": obj.get("exceptional_case_funding_reference"),
            "expense_limit": obj.get("expense_limit"),
            "fee_scheme": obj.get("fee_scheme"),
            "first_conducting_solicitor": obj.get("first_conducting_solicitor"),
            "id": obj.get("id"),
            "irc_surgery": obj.get("irc_surgery"),
            "legacy_case": obj.get("legacy_case"),
            "legal_representation_number": obj.get("legal_representation_number"),
            "lh_total_disbursements": obj.get("lh_total_disbursements"),
            "lh_start_date": obj.get("lh_start_date"),
            "lh_total_profit_costs": obj.get("lh_total_profit_costs"),
            "linked_matter_id": obj.get("linked_matter_id"),
            "local_authority_number": obj.get("local_authority_number"),
            "maat_id": obj.get("maat_id"),
            "matter_type": obj.get("matter_type"),
            "matter_type_code": obj.get("matter_type_code"),
            "matter_type_1": obj.get("matter_type_1"),
            "matter_type_1_code": obj.get("matter_type_1_code"),
            "matter_type_1_title": obj.get("matter_type_1_title"),
            "matter_type_2": obj.get("matter_type_2"),
            "matter_type_2_code": obj.get("matter_type_2_code"),
            "matter_type_2_title": obj.get("matter_type_2_title"),
            "matter_types_combined": obj.get("matter_types_combined"),
            "number_of_clients_seen_at_surgery": obj.get("number_of_clients_seen_at_surgery"),
            "number_of_clients": obj.get("number_of_clients"),
            "party": obj.get("party"),
            "police_station": obj.get("police_station"),
            "post_transfer_clients_represented": obj.get("post_transfer_clients_represented"),
            "postal_application_accepted": obj.get("postal_application_accepted"),
            "prior_authority_reference": obj.get("prior_authority_reference"),
            "prison_id": obj.get("prison_id"),
            "prison_law_prior_approval_number": obj.get("prison_law_prior_approval_number"),
            "procurement_area": obj.get("procurement_area"),
            "region": obj.get("region"),
            "related_claims_number": obj.get("related_claims_number"),
            "representation_order_date": obj.get("representation_order_date"),
            "schedule_reference_number": obj.get("schedule_reference_number"),
            "scheme_id": obj.get("scheme_id"),
            "session_type": obj.get("session_type"),
            "solicitor_type": obj.get("solicitor_type"),
            "standard_fee_category": obj.get("standard_fee_category"),
            "surgery_clients_resulting_in_a_legal_help_matter_opened": obj.get("surgery_clients_resulting_in_a_legal_help_matter_opened"),
            "surgery_clients": obj.get("surgery_clients"),
            "surgery_date": obj.get("surgery_date"),
            "transfer_date": obj.get("transfer_date"),
            "type_of_advice": obj.get("type_of_advice"),
            "type_of_service": obj.get("type_of_service"),
            "ucn": obj.get("ucn"),
            "ufn": obj.get("ufn"),
            "undesignated_area_court": obj.get("undesignated_area_court"),
            "updated_at": obj.get("updated_at"),
            "user_type": obj.get("user_type"),
            "youth_court": obj.get("youth_court")
        })
        return _obj


