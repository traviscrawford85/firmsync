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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from clio_sdk.models.address_base import AddressBase
from clio_sdk.models.avatar_base import AvatarBase
from clio_sdk.models.contact_base import ContactBase
from clio_sdk.models.custom_field_value_base import CustomFieldValueBase
from clio_sdk.models.email_address_base import EmailAddressBase
from clio_sdk.models.phone_number_base import PhoneNumberBase
from clio_sdk.models.relationship_base import RelationshipBase
from clio_sdk.models.web_site_base import WebSiteBase
from typing import Optional, Set
from typing_extensions import Self

class RelatedContacts(BaseModel):
    """
    RelatedContacts
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier for the *RelatedContacts*")
    contact_id: Optional[StrictInt] = Field(default=None, description="The id of the *RelatedContacts*")
    name: Optional[StrictStr] = Field(default=None, description="The full name of the *RelatedContacts*")
    first_name: Optional[StrictStr] = Field(default=None, description="First name of the Person")
    middle_name: Optional[StrictStr] = Field(default=None, description="Middle name of the Person")
    last_name: Optional[StrictStr] = Field(default=None, description="Last name of the Person")
    type: Optional[StrictStr] = Field(default=None, description="The type of the *RelatedContacts*")
    created_at: Optional[datetime] = Field(default=None, description="The time the *RelatedContacts* was created (as a ISO-8601 timestamp)")
    updated_at: Optional[datetime] = Field(default=None, description="The time the *RelatedContacts* was last updated (as a ISO-8601 timestamp)")
    prefix: Optional[StrictStr] = Field(default=None, description="The prefix of the *RelatedContacts* (Mr, Mrs, etc)")
    title: Optional[StrictStr] = Field(default=None, description="The designated title of the *RelatedContacts*")
    initials: Optional[StrictStr] = Field(default=None, description="The initials of the *RelatedContacts*")
    is_matter_client: Optional[StrictBool] = Field(default=None, description="Whether or not the RelatedContacts is also the client of the matter")
    primary_email_address: Optional[StrictStr] = Field(default=None, description="The primary email address of related contact")
    primary_phone_number: Optional[StrictStr] = Field(default=None, description="The primary phone number of related contact")
    client_connect_user_id: Optional[StrictInt] = Field(default=None, description="The client connect ID of the contacts associated user")
    avatar: Optional[AvatarBase] = None
    company: Optional[ContactBase] = None
    primary_address: Optional[AddressBase] = None
    primary_web_site: Optional[WebSiteBase] = None
    secondary_address: Optional[AddressBase] = None
    secondary_web_site: Optional[WebSiteBase] = None
    addresses: Optional[List[AddressBase]] = Field(default=None, description="Address")
    custom_field_values: Optional[List[CustomFieldValueBase]] = Field(default=None, description="CustomFieldValue")
    email_addresses: Optional[List[EmailAddressBase]] = Field(default=None, description="EmailAddress")
    phone_numbers: Optional[List[PhoneNumberBase]] = Field(default=None, description="PhoneNumber")
    web_sites: Optional[List[WebSiteBase]] = Field(default=None, description="WebSite")
    relationship: Optional[RelationshipBase] = None
    __properties: ClassVar[List[str]] = ["id", "contact_id", "name", "first_name", "middle_name", "last_name", "type", "created_at", "updated_at", "prefix", "title", "initials", "is_matter_client", "primary_email_address", "primary_phone_number", "client_connect_user_id", "avatar", "company", "primary_address", "primary_web_site", "secondary_address", "secondary_web_site", "addresses", "custom_field_values", "email_addresses", "phone_numbers", "web_sites", "relationship"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Company', 'Person']):
            raise ValueError("must be one of enum values ('Company', 'Person')")
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
        """Create an instance of RelatedContacts from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of avatar
        if self.avatar:
            _dict['avatar'] = self.avatar.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company
        if self.company:
            _dict['company'] = self.company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of primary_address
        if self.primary_address:
            _dict['primary_address'] = self.primary_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of primary_web_site
        if self.primary_web_site:
            _dict['primary_web_site'] = self.primary_web_site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secondary_address
        if self.secondary_address:
            _dict['secondary_address'] = self.secondary_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secondary_web_site
        if self.secondary_web_site:
            _dict['secondary_web_site'] = self.secondary_web_site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in addresses (list)
        _items = []
        if self.addresses:
            for _item_addresses in self.addresses:
                if _item_addresses:
                    _items.append(_item_addresses.to_dict())
            _dict['addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_field_values (list)
        _items = []
        if self.custom_field_values:
            for _item_custom_field_values in self.custom_field_values:
                if _item_custom_field_values:
                    _items.append(_item_custom_field_values.to_dict())
            _dict['custom_field_values'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in email_addresses (list)
        _items = []
        if self.email_addresses:
            for _item_email_addresses in self.email_addresses:
                if _item_email_addresses:
                    _items.append(_item_email_addresses.to_dict())
            _dict['email_addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in phone_numbers (list)
        _items = []
        if self.phone_numbers:
            for _item_phone_numbers in self.phone_numbers:
                if _item_phone_numbers:
                    _items.append(_item_phone_numbers.to_dict())
            _dict['phone_numbers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in web_sites (list)
        _items = []
        if self.web_sites:
            for _item_web_sites in self.web_sites:
                if _item_web_sites:
                    _items.append(_item_web_sites.to_dict())
            _dict['web_sites'] = _items
        # override the default output from pydantic by calling `to_dict()` of relationship
        if self.relationship:
            _dict['relationship'] = self.relationship.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RelatedContacts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "contact_id": obj.get("contact_id"),
            "name": obj.get("name"),
            "first_name": obj.get("first_name"),
            "middle_name": obj.get("middle_name"),
            "last_name": obj.get("last_name"),
            "type": obj.get("type"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "prefix": obj.get("prefix"),
            "title": obj.get("title"),
            "initials": obj.get("initials"),
            "is_matter_client": obj.get("is_matter_client"),
            "primary_email_address": obj.get("primary_email_address"),
            "primary_phone_number": obj.get("primary_phone_number"),
            "client_connect_user_id": obj.get("client_connect_user_id"),
            "avatar": AvatarBase.from_dict(obj["avatar"]) if obj.get("avatar") is not None else None,
            "company": ContactBase.from_dict(obj["company"]) if obj.get("company") is not None else None,
            "primary_address": AddressBase.from_dict(obj["primary_address"]) if obj.get("primary_address") is not None else None,
            "primary_web_site": WebSiteBase.from_dict(obj["primary_web_site"]) if obj.get("primary_web_site") is not None else None,
            "secondary_address": AddressBase.from_dict(obj["secondary_address"]) if obj.get("secondary_address") is not None else None,
            "secondary_web_site": WebSiteBase.from_dict(obj["secondary_web_site"]) if obj.get("secondary_web_site") is not None else None,
            "addresses": [AddressBase.from_dict(_item) for _item in obj["addresses"]] if obj.get("addresses") is not None else None,
            "custom_field_values": [CustomFieldValueBase.from_dict(_item) for _item in obj["custom_field_values"]] if obj.get("custom_field_values") is not None else None,
            "email_addresses": [EmailAddressBase.from_dict(_item) for _item in obj["email_addresses"]] if obj.get("email_addresses") is not None else None,
            "phone_numbers": [PhoneNumberBase.from_dict(_item) for _item in obj["phone_numbers"]] if obj.get("phone_numbers") is not None else None,
            "web_sites": [WebSiteBase.from_dict(_item) for _item in obj["web_sites"]] if obj.get("web_sites") is not None else None,
            "relationship": RelationshipBase.from_dict(obj["relationship"]) if obj.get("relationship") is not None else None
        })
        return _obj


