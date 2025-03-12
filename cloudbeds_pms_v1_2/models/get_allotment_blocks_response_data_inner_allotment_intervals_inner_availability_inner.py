# coding: utf-8

"""
    Cloudbeds API

    <p>     Welcome to the documentation for <strong>Cloudbeds API Version v1.2</strong>!     If you are looking to learn how to use the Cloudbeds API to access guest information, reservations, or similar data     for your Cloudbeds customers, then you've come to the right place. </p>  <p>     In this document you will find all the API methods we provide along with explanations for parameters and response     examples. </p>  <p>     If you have questions about different implementation steps (e.g. how to implement OAuth 2.0), please refer to our     <a href=\"https://integrations.cloudbeds.com/hc/en-us\">Integrations Portal</a>. </p>  <p>     Be sure to <a href=\"https://go.pardot.com/l/308041/2018-07-24/qb2lg\">subscribe</a> to the monthly     Cloudbeds API announcement mailing list to receive information on new additions and improvements to the     Cloudbeds API and related developer tools. </p>  <p>     <strong>Endpoint:</strong> https://api.cloudbeds.com/api/v1.2/{method} </p>  <p>     <strong>HTTPS:</strong> Our API requires HTTPS. We'll respond with an appropriate error if you're not using it. </p>  <p>     <strong>Request Format:</strong> HTTP GET, POST and PUT (Content-Type: application/x-www-form-urlencoded) </p>  <p>     <strong>Response Format:</strong> JSON </p>  <p>     <strong>Response Header:</strong> X-Request-ID is added to response headers in all calls to help accelerate support     and troubleshooting. </p>  <p>     <strong>         <a href=\"https://integrations.cloudbeds.com/hc/en-us/articles/14104678058267-API-Documentation#postman-collection\">             <img src=\"https://run.pstmn.io/button.svg\" alt=\"Run in Postman\">         </a>     </strong> use this link to access our Public collection in Postman. </p>

    The version of the OpenAPI document: v1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cloudbeds_pms_v1_2.models.post_create_allotment_block_response_data_inner_allotment_intervals_inner_availability_guest_pricing import PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailabilityGuestPricing
from typing import Optional, Set
from typing_extensions import Self

class GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner(BaseModel):
    """
    GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner
    """ # noqa: E501
    var_date: Optional[date] = Field(default=None, description="Day within interval", alias="date")
    block_remaining: Optional[StrictInt] = Field(default=None, description="Number of units remaining for the room type for this day", alias="blockRemaining")
    block_allotted: Optional[StrictInt] = Field(default=None, description="Total number of units available for the room type for this day", alias="blockAllotted")
    block_confirmed: Optional[StrictInt] = Field(default=None, description="Number of units booked for the room type for this day", alias="blockConfirmed")
    rate: Optional[StrictStr] = Field(default=None, description="the price")
    guest_pricing: Optional[PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailabilityGuestPricing] = Field(default=None, alias="guestPricing")
    split_block_allotted: Optional[StrictInt] = Field(default=None, description="Number of split units available for the room type this day", alias="splitBlockAllotted")
    split_block_confirmed: Optional[StrictInt] = Field(default=None, description="Number of split units blocked for the room type this day", alias="splitBlockConfirmed")
    __properties: ClassVar[List[str]] = ["date", "blockRemaining", "blockAllotted", "blockConfirmed", "rate", "guestPricing", "splitBlockAllotted", "splitBlockConfirmed"]

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
        """Create an instance of GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of guest_pricing
        if self.guest_pricing:
            _dict['guestPricing'] = self.guest_pricing.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "blockRemaining": obj.get("blockRemaining"),
            "blockAllotted": obj.get("blockAllotted"),
            "blockConfirmed": obj.get("blockConfirmed"),
            "rate": obj.get("rate"),
            "guestPricing": PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailabilityGuestPricing.from_dict(obj["guestPricing"]) if obj.get("guestPricing") is not None else None,
            "splitBlockAllotted": obj.get("splitBlockAllotted"),
            "splitBlockConfirmed": obj.get("splitBlockConfirmed")
        })
        return _obj


