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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from clio_sdk.models.user_base import UserBase
from typing import Optional, Set
from typing_extensions import Self

class BankAccount(BaseModel):
    """
    BankAccount
    """ # noqa: E501
    account_number: Optional[StrictStr] = Field(default=None, description="The account number for *BankAccount*")
    balance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The current balance of the *BankAccount*")
    bank_transactions_count: Optional[StrictInt] = Field(default=None, description="The number of bank transactions associated with the account.")
    clio_payment_page_link: Optional[StrictStr] = Field(default=None, description="Link to Single Payment Page which allows to transfer funds without logging in.")
    clio_payment_page_qr_code: Optional[StrictStr] = Field(default=None, description="A QR code that links to a Single Payment Page which allows to transfer funds without logging in.")
    clio_payments_enabled: Optional[StrictBool] = Field(default=None, description="Whether the bank account is connected to Clio Payments")
    controlled_account: Optional[StrictBool] = Field(default=None, description="Whether is a controlled account")
    created_at: Optional[datetime] = Field(default=None, description="The time the *BankAccount* was created (as a ISO-8601 timestamp)")
    currency: Optional[StrictStr] = Field(default=None, description="The currency type of the *BankAccount*")
    currency_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The currency ID of the *BankAccount*")
    default_account: Optional[StrictBool] = Field(default=None, description="Whether it is the default account")
    domicile_branch: Optional[StrictStr] = Field(default=None, description="The name of the branch where the account was opened")
    etag: Optional[StrictStr] = Field(default=None, description="ETag for the *BankAccount*")
    general_ledger_number: Optional[StrictStr] = Field(default=None, description="General ledger number")
    holder: Optional[StrictStr] = Field(default=None, description="The name of the person or business that owns the *BankAccount*")
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier for the *BankAccount*")
    institution: Optional[StrictStr] = Field(default=None, description="The financial institution where the *BankAccount* is registered")
    name: Optional[StrictStr] = Field(default=None, description="The name of the *BankAccount*")
    swift: Optional[StrictStr] = Field(default=None, description="A unique identification code for the financial institution")
    transit_number: Optional[StrictStr] = Field(default=None, description="Transit number for the bank account branch")
    type: Optional[StrictStr] = Field(default=None, description="The type of the *BankAccount*")
    updated_at: Optional[datetime] = Field(default=None, description="The time the *BankAccount* was last updated (as a ISO-8601 timestamp)")
    user: Optional[UserBase] = None
    __properties: ClassVar[List[str]] = ["account_number", "balance", "bank_transactions_count", "clio_payment_page_link", "clio_payment_page_qr_code", "clio_payments_enabled", "controlled_account", "created_at", "currency", "currency_id", "default_account", "domicile_branch", "etag", "general_ledger_number", "holder", "id", "institution", "name", "swift", "transit_number", "type", "updated_at", "user"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Operating', 'Trust']):
            raise ValueError("must be one of enum values ('Operating', 'Trust')")
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
        """Create an instance of BankAccount from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account_number": obj.get("account_number"),
            "balance": obj.get("balance"),
            "bank_transactions_count": obj.get("bank_transactions_count"),
            "clio_payment_page_link": obj.get("clio_payment_page_link"),
            "clio_payment_page_qr_code": obj.get("clio_payment_page_qr_code"),
            "clio_payments_enabled": obj.get("clio_payments_enabled"),
            "controlled_account": obj.get("controlled_account"),
            "created_at": obj.get("created_at"),
            "currency": obj.get("currency"),
            "currency_id": obj.get("currency_id"),
            "default_account": obj.get("default_account"),
            "domicile_branch": obj.get("domicile_branch"),
            "etag": obj.get("etag"),
            "general_ledger_number": obj.get("general_ledger_number"),
            "holder": obj.get("holder"),
            "id": obj.get("id"),
            "institution": obj.get("institution"),
            "name": obj.get("name"),
            "swift": obj.get("swift"),
            "transit_number": obj.get("transit_number"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "user": UserBase.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj


