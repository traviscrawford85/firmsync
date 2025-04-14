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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from clio_sdk.models.activity_create_request_data_activity_description import ActivityCreateRequestDataActivityDescription
from clio_sdk.models.activity_create_request_data_calendar_entry import ActivityCreateRequestDataCalendarEntry
from clio_sdk.models.activity_create_request_data_client_portal import ActivityCreateRequestDataClientPortal
from clio_sdk.models.activity_create_request_data_communication import ActivityCreateRequestDataCommunication
from clio_sdk.models.activity_create_request_data_contact_note import ActivityCreateRequestDataContactNote
from clio_sdk.models.activity_create_request_data_expense_category import ActivityCreateRequestDataExpenseCategory
from clio_sdk.models.activity_create_request_data_matter import ActivityCreateRequestDataMatter
from clio_sdk.models.activity_create_request_data_task import ActivityCreateRequestDataTask
from clio_sdk.models.activity_create_request_data_text_message_conversation import ActivityCreateRequestDataTextMessageConversation
from clio_sdk.models.activity_create_request_data_user import ActivityCreateRequestDataUser
from clio_sdk.models.activity_create_request_data_utbms_expense import ActivityCreateRequestDataUtbmsExpense
from clio_sdk.models.activity_create_request_data_vendor import ActivityCreateRequestDataVendor
from typing import Optional, Set
from typing_extensions import Self

class ActivityUpdateRequestData(BaseModel):
    """
    ActivityUpdateRequestData
    """ # noqa: E501
    activity_description: Optional[ActivityCreateRequestDataActivityDescription] = None
    calendar_entry: Optional[ActivityCreateRequestDataCalendarEntry] = None
    client_portal: Optional[ActivityCreateRequestDataClientPortal] = None
    communication: Optional[ActivityCreateRequestDataCommunication] = None
    contact_note: Optional[ActivityCreateRequestDataContactNote] = None
    var_date: Optional[date] = Field(default=None, description="The date the Activity was performed. (Expects an ISO-8601 date).", alias="date")
    expense_category: Optional[ActivityCreateRequestDataExpenseCategory] = None
    matter: Optional[ActivityCreateRequestDataMatter] = None
    matter_note: Optional[ActivityCreateRequestDataContactNote] = None
    no_charge: Optional[StrictBool] = Field(default=None, description="Whether the non-billable *Activity* will be shown on the bill.")
    non_billable: Optional[StrictBool] = Field(default=None, description="Whether or not this Activity is prevented from appearing as a line item in a bill. Only valid for non-billed TimeEntries, and with the exception of the Activity having no_charge set to true. ")
    note: Optional[StrictStr] = Field(default=None, description="A custom note to describe what the Activity is for.")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="For an ExpenseEntry, HardCostEntry, and SoftCostEntry, it is the expense amount.  [Support Link for ExpenseEntry](https://help.clio.com/hc/en-us/articles/9289745356571-Expenses)  [Support Link for HardCostEntry and SoftCostEntry](https://help.clio.com/hc/en-us/articles/9289745356571-Expenses#enable-hard-and-soft-cost-expenses-0-0)  For a TimeEntry, it is the hourly or flat amount. When updating a TimeEntry, if the price is not given or the user does not have the permission to view the rate, and its activity description, matter and/or user is changed, the price is reset according to the rate defined for the activity description, matter, client or user.  [Support Link for Rates Hierarchy](https://help.clio.com/hc/en-us/articles/9289801180187-Rates-and-Rate-Hierarchies-)  [Support Link for Billing Rate Visibility](https://help.clio.com/hc/en-us/articles/9285360193819-Permissions-and-Billing-Rates#billing-rate-visibility-0-3) ")
    quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The field is applicable to TimeEntry, ExpenseEntry, and SoftCostEntry.  **Version <= 4.0.3:** The number of hours the TimeEntry took.  **Latest version:** The number of seconds the TimeEntry took. ")
    reference: Optional[StrictStr] = Field(default=None, description="A check reference for a HardCostEntry.")
    start_timer: Optional[StrictBool] = Field(default=None, description="Whether or not a timer should be started for this Activity. Only valid for non-FlatRate, non-billed TimeEntries.")
    task: Optional[ActivityCreateRequestDataTask] = None
    tax_setting: Optional[StrictStr] = Field(default=None, description="The option denoting whether primary tax, secondary tax, or both is applied to an expense entry.")
    text_message_conversation: Optional[ActivityCreateRequestDataTextMessageConversation] = None
    type: Optional[StrictStr] = Field(default=None, description="The type of the Activity.")
    user: Optional[ActivityCreateRequestDataUser] = None
    utbms_expense: Optional[ActivityCreateRequestDataUtbmsExpense] = None
    vendor: Optional[ActivityCreateRequestDataVendor] = None
    __properties: ClassVar[List[str]] = ["activity_description", "calendar_entry", "client_portal", "communication", "contact_note", "date", "expense_category", "matter", "matter_note", "no_charge", "non_billable", "note", "price", "quantity", "reference", "start_timer", "task", "tax_setting", "text_message_conversation", "type", "user", "utbms_expense", "vendor"]

    @field_validator('tax_setting')
    def tax_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['no_tax', 'tax_1_only', 'tax_2_only', 'tax_1_and_tax_2']):
            raise ValueError("must be one of enum values ('no_tax', 'tax_1_only', 'tax_2_only', 'tax_1_and_tax_2')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['TimeEntry', 'ExpenseEntry', 'HardCostEntry', 'SoftCostEntry']):
            raise ValueError("must be one of enum values ('TimeEntry', 'ExpenseEntry', 'HardCostEntry', 'SoftCostEntry')")
        return value

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
        """Create an instance of ActivityUpdateRequestData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of activity_description
        if self.activity_description:
            _dict['activity_description'] = self.activity_description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of calendar_entry
        if self.calendar_entry:
            _dict['calendar_entry'] = self.calendar_entry.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client_portal
        if self.client_portal:
            _dict['client_portal'] = self.client_portal.to_dict()
        # override the default output from pydantic by calling `to_dict()` of communication
        if self.communication:
            _dict['communication'] = self.communication.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contact_note
        if self.contact_note:
            _dict['contact_note'] = self.contact_note.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expense_category
        if self.expense_category:
            _dict['expense_category'] = self.expense_category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of matter
        if self.matter:
            _dict['matter'] = self.matter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of matter_note
        if self.matter_note:
            _dict['matter_note'] = self.matter_note.to_dict()
        # override the default output from pydantic by calling `to_dict()` of task
        if self.task:
            _dict['task'] = self.task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of text_message_conversation
        if self.text_message_conversation:
            _dict['text_message_conversation'] = self.text_message_conversation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of utbms_expense
        if self.utbms_expense:
            _dict['utbms_expense'] = self.utbms_expense.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vendor
        if self.vendor:
            _dict['vendor'] = self.vendor.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ActivityUpdateRequestData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activity_description": ActivityCreateRequestDataActivityDescription.from_dict(obj["activity_description"]) if obj.get("activity_description") is not None else None,
            "calendar_entry": ActivityCreateRequestDataCalendarEntry.from_dict(obj["calendar_entry"]) if obj.get("calendar_entry") is not None else None,
            "client_portal": ActivityCreateRequestDataClientPortal.from_dict(obj["client_portal"]) if obj.get("client_portal") is not None else None,
            "communication": ActivityCreateRequestDataCommunication.from_dict(obj["communication"]) if obj.get("communication") is not None else None,
            "contact_note": ActivityCreateRequestDataContactNote.from_dict(obj["contact_note"]) if obj.get("contact_note") is not None else None,
            "date": obj.get("date"),
            "expense_category": ActivityCreateRequestDataExpenseCategory.from_dict(obj["expense_category"]) if obj.get("expense_category") is not None else None,
            "matter": ActivityCreateRequestDataMatter.from_dict(obj["matter"]) if obj.get("matter") is not None else None,
            "matter_note": ActivityCreateRequestDataContactNote.from_dict(obj["matter_note"]) if obj.get("matter_note") is not None else None,
            "no_charge": obj.get("no_charge"),
            "non_billable": obj.get("non_billable"),
            "note": obj.get("note"),
            "price": obj.get("price"),
            "quantity": obj.get("quantity"),
            "reference": obj.get("reference"),
            "start_timer": obj.get("start_timer"),
            "task": ActivityCreateRequestDataTask.from_dict(obj["task"]) if obj.get("task") is not None else None,
            "tax_setting": obj.get("tax_setting"),
            "text_message_conversation": ActivityCreateRequestDataTextMessageConversation.from_dict(obj["text_message_conversation"]) if obj.get("text_message_conversation") is not None else None,
            "type": obj.get("type"),
            "user": ActivityCreateRequestDataUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "utbms_expense": ActivityCreateRequestDataUtbmsExpense.from_dict(obj["utbms_expense"]) if obj.get("utbms_expense") is not None else None,
            "vendor": ActivityCreateRequestDataVendor.from_dict(obj["vendor"]) if obj.get("vendor") is not None else None
        })
        return _obj


