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
from typing import Optional, Set
from typing_extensions import Self

class CalendarVisibility(BaseModel):
    """
    CalendarVisibility
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier for the *CalendarVisibility*")
    etag: Optional[StrictStr] = Field(default=None, description="ETag for the *CalendarVisibility*")
    color: Optional[StrictStr] = Field(default=None, description="Calendar color")
    light_color: Optional[StrictStr] = Field(default=None, description="Accent color to complement the main calendar color.")
    visible: Optional[StrictBool] = Field(default=None, description="Whether the *CalendarVisibility* will be shown by default in the Clio Web UI.")
    name: Optional[StrictStr] = Field(default=None, description="Calendar name")
    created_at: Optional[datetime] = Field(default=None, description="The time the *CalendarVisibility* was created (as a ISO-8601 timestamp)")
    updated_at: Optional[datetime] = Field(default=None, description="The time the *CalendarVisibility* was last updated (as a ISO-8601 timestamp)")
    __properties: ClassVar[List[str]] = ["id", "etag", "color", "light_color", "visible", "name", "created_at", "updated_at"]

    @field_validator('color')
    def color_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['#658CDA', '#DA6666', '#49B050', '#E7804C', '#8C66DA', '#C4A882', '#64AD88', '#84AAA5', '#56BFB3', '#E77399', '#BFBF4B', '#8BBF3C', '#B473B4', '#A7A77D', '#F2A53D', '#658CB3', '#BE9494', '#A992A9', '#8897A5', '#93A2BE']):
            raise ValueError("must be one of enum values ('#658CDA', '#DA6666', '#49B050', '#E7804C', '#8C66DA', '#C4A882', '#64AD88', '#84AAA5', '#56BFB3', '#E77399', '#BFBF4B', '#8BBF3C', '#B473B4', '#A7A77D', '#F2A53D', '#658CB3', '#BE9494', '#A992A9', '#8897A5', '#93A2BE')")
        return value

    @field_validator('light_color')
    def light_color_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['#5DA5C7', '#F95957', '#209412', '#FF7715', '#DE649D', '#FF6B02', '#56C4FC', '#00B177', '#50D19B', '#F14A8C', '#A3A2A2', '#84AB3B', '#B091EE', '#BD9E69', '#F2A000', '#00A5CA', '#CB5A3D', '#959CD0', '#B0B0B0', '#7BA6CD']):
            raise ValueError("must be one of enum values ('#5DA5C7', '#F95957', '#209412', '#FF7715', '#DE649D', '#FF6B02', '#56C4FC', '#00B177', '#50D19B', '#F14A8C', '#A3A2A2', '#84AB3B', '#B091EE', '#BD9E69', '#F2A000', '#00A5CA', '#CB5A3D', '#959CD0', '#B0B0B0', '#7BA6CD')")
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
        """Create an instance of CalendarVisibility from a JSON string"""
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
        """Create an instance of CalendarVisibility from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "etag": obj.get("etag"),
            "color": obj.get("color"),
            "light_color": obj.get("light_color"),
            "visible": obj.get("visible"),
            "name": obj.get("name"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


