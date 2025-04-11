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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from clio_sdk.models.calendar_entry_create_request_data_attendees_inner import CalendarEntryCreateRequestDataAttendeesInner
from clio_sdk.models.calendar_entry_create_request_data_calendar_entry_event_type import CalendarEntryCreateRequestDataCalendarEntryEventType
from clio_sdk.models.calendar_entry_create_request_data_calendar_owner import CalendarEntryCreateRequestDataCalendarOwner
from clio_sdk.models.calendar_entry_create_request_data_conference_meeting import CalendarEntryCreateRequestDataConferenceMeeting
from clio_sdk.models.calendar_entry_create_request_data_external_properties_inner import CalendarEntryCreateRequestDataExternalPropertiesInner
from clio_sdk.models.calendar_entry_create_request_data_matter import CalendarEntryCreateRequestDataMatter
from typing import Optional, Set
from typing_extensions import Self

class CalendarEntryCreateRequestData(BaseModel):
    """
    CalendarEntryCreateRequestData
    """ # noqa: E501
    deleted: Optional[StrictStr] = Field(default=None, description="Flag to delete a specific instance of a recurring event.", alias="_deleted")
    all_day: Optional[StrictBool] = Field(default=None, description="Whether or not the CalendarEntry is for all day.")
    attendees: Optional[List[CalendarEntryCreateRequestDataAttendeesInner]] = None
    calendar_entry_event_type: Optional[CalendarEntryCreateRequestDataCalendarEntryEventType] = None
    calendar_owner: CalendarEntryCreateRequestDataCalendarOwner
    conference_meeting: Optional[CalendarEntryCreateRequestDataConferenceMeeting] = None
    description: Optional[StrictStr] = Field(default=None, description="A detailed description of the CalendarEntry.")
    end_at: datetime = Field(description="The time the CalendarEntry ends (Expects an ISO-8601 timestamp).")
    external_properties: Optional[List[CalendarEntryCreateRequestDataExternalPropertiesInner]] = None
    location: Optional[StrictStr] = Field(default=None, description="The geographic location of the CalendarEntry.")
    matter: Optional[CalendarEntryCreateRequestDataMatter] = None
    recurrence_rule: Optional[StrictStr] = Field(default=None, description="Recurrence rule for expanding recurring CalendarEntry. To convert an existing recurring event to a non-recurring event, `''` or `null` are valid values.")
    send_email_notification: Optional[StrictBool] = Field(default=None, description="Whether the calendar Entry should send email notifications to attendees")
    start_at: datetime = Field(description="The time the CalendarEntry starts (Expects an ISO-8601 timestamp).")
    summary: StrictStr = Field(description="A short summary of the CalendarEntry.")
    __properties: ClassVar[List[str]] = ["_deleted", "all_day", "attendees", "calendar_entry_event_type", "calendar_owner", "conference_meeting", "description", "end_at", "external_properties", "location", "matter", "recurrence_rule", "send_email_notification", "start_at", "summary"]

    @field_validator('deleted')
    def deleted_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['single', 'future']):
            raise ValueError("must be one of enum values ('single', 'future')")
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
        """Create an instance of CalendarEntryCreateRequestData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attendees (list)
        _items = []
        if self.attendees:
            for _item_attendees in self.attendees:
                if _item_attendees:
                    _items.append(_item_attendees.to_dict())
            _dict['attendees'] = _items
        # override the default output from pydantic by calling `to_dict()` of calendar_entry_event_type
        if self.calendar_entry_event_type:
            _dict['calendar_entry_event_type'] = self.calendar_entry_event_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of calendar_owner
        if self.calendar_owner:
            _dict['calendar_owner'] = self.calendar_owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conference_meeting
        if self.conference_meeting:
            _dict['conference_meeting'] = self.conference_meeting.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in external_properties (list)
        _items = []
        if self.external_properties:
            for _item_external_properties in self.external_properties:
                if _item_external_properties:
                    _items.append(_item_external_properties.to_dict())
            _dict['external_properties'] = _items
        # override the default output from pydantic by calling `to_dict()` of matter
        if self.matter:
            _dict['matter'] = self.matter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CalendarEntryCreateRequestData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_deleted": obj.get("_deleted"),
            "all_day": obj.get("all_day"),
            "attendees": [CalendarEntryCreateRequestDataAttendeesInner.from_dict(_item) for _item in obj["attendees"]] if obj.get("attendees") is not None else None,
            "calendar_entry_event_type": CalendarEntryCreateRequestDataCalendarEntryEventType.from_dict(obj["calendar_entry_event_type"]) if obj.get("calendar_entry_event_type") is not None else None,
            "calendar_owner": CalendarEntryCreateRequestDataCalendarOwner.from_dict(obj["calendar_owner"]) if obj.get("calendar_owner") is not None else None,
            "conference_meeting": CalendarEntryCreateRequestDataConferenceMeeting.from_dict(obj["conference_meeting"]) if obj.get("conference_meeting") is not None else None,
            "description": obj.get("description"),
            "end_at": obj.get("end_at"),
            "external_properties": [CalendarEntryCreateRequestDataExternalPropertiesInner.from_dict(_item) for _item in obj["external_properties"]] if obj.get("external_properties") is not None else None,
            "location": obj.get("location"),
            "matter": CalendarEntryCreateRequestDataMatter.from_dict(obj["matter"]) if obj.get("matter") is not None else None,
            "recurrence_rule": obj.get("recurrence_rule"),
            "send_email_notification": obj.get("send_email_notification"),
            "start_at": obj.get("start_at"),
            "summary": obj.get("summary")
        })
        return _obj


