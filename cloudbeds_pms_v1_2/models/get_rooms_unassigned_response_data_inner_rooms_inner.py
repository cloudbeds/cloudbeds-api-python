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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetRoomsUnassignedResponseDataInnerRoomsInner(BaseModel):
    """
    GetRoomsUnassignedResponseDataInnerRoomsInner
    """ # noqa: E501
    room_id: Optional[StrictStr] = Field(default=None, description="Room ID", alias="roomID")
    room_name: Optional[StrictStr] = Field(default=None, description="Room Name", alias="roomName")
    dorm_room_name: Optional[StrictStr] = Field(default=None, description="Name of the dorm room. Used for the shared dorm beds that are organized into rooms within the same room type", alias="dormRoomName")
    room_description: Optional[StrictStr] = Field(default=None, description="Room Description", alias="roomDescription")
    max_guests: Optional[StrictInt] = Field(default=None, description="Number of guests that room allows", alias="maxGuests")
    is_private: Optional[StrictBool] = Field(default=None, description="If room is private (true) or shared (false)", alias="isPrivate")
    is_virtual: Optional[StrictBool] = Field(default=None, description="If room is virtual (true) or physical (false)", alias="isVirtual")
    room_blocked: Optional[StrictBool] = Field(default=None, description="If room is blocked on calendar during the period selected. If no check-in/out dates are sent, it returns the status for the current day.", alias="roomBlocked")
    room_type_id: Optional[StrictStr] = Field(default=None, description="Room type ID", alias="roomTypeID")
    room_type_name: Optional[StrictStr] = Field(default=None, description="Room type Name", alias="roomTypeName")
    room_type_name_short: Optional[StrictStr] = Field(default=None, description="Room type Short Name", alias="roomTypeNameShort")
    __properties: ClassVar[List[str]] = ["roomID", "roomName", "dormRoomName", "roomDescription", "maxGuests", "isPrivate", "isVirtual", "roomBlocked", "roomTypeID", "roomTypeName", "roomTypeNameShort"]

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
        """Create an instance of GetRoomsUnassignedResponseDataInnerRoomsInner from a JSON string"""
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
        """Create an instance of GetRoomsUnassignedResponseDataInnerRoomsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "roomID": obj.get("roomID"),
            "roomName": obj.get("roomName"),
            "dormRoomName": obj.get("dormRoomName"),
            "roomDescription": obj.get("roomDescription"),
            "maxGuests": obj.get("maxGuests"),
            "isPrivate": obj.get("isPrivate"),
            "isVirtual": obj.get("isVirtual"),
            "roomBlocked": obj.get("roomBlocked"),
            "roomTypeID": obj.get("roomTypeID"),
            "roomTypeName": obj.get("roomTypeName"),
            "roomTypeNameShort": obj.get("roomTypeNameShort")
        })
        return _obj


