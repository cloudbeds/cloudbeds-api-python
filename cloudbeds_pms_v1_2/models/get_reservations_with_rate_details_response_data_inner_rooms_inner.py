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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetReservationsWithRateDetailsResponseDataInnerRoomsInner(BaseModel):
    """
    GetReservationsWithRateDetailsResponseDataInnerRoomsInner
    """ # noqa: E501
    room_type_id: Optional[StrictStr] = Field(default=None, description="Room Type ID", alias="roomTypeID")
    room_type_is_virtual: Optional[StrictBool] = Field(default=None, description="If room is virtual (true) or physical (false)", alias="roomTypeIsVirtual")
    room_type_name: Optional[StrictStr] = Field(default=None, description="Room Type Name", alias="roomTypeName")
    sub_reservation_id: Optional[StrictStr] = Field(default=None, description="sub Reservation ID (specific to each room)", alias="subReservationID")
    guest_id: Optional[StrictStr] = Field(default=None, description="ID of the main guest assigned to the room", alias="guestID")
    guest_name: Optional[StrictStr] = Field(default=None, description="Name of the main guest assigned to the room", alias="guestName")
    rate_id: Optional[StrictStr] = Field(default=None, description="ID of the rate used for the booking room", alias="rateID")
    rate_name: Optional[StrictStr] = Field(default=None, description="Name of the rate used for the booking room", alias="rateName")
    adults: Optional[StrictStr] = Field(default=None, description="Number of adults in the room")
    children: Optional[StrictStr] = Field(default=None, description="Number of children in the room")
    room_id: Optional[StrictStr] = Field(default=None, description="Room ID (null if the reservation has not been assigned a specific room yet).", alias="roomID")
    room_name: Optional[StrictStr] = Field(default=None, description="Name of the room, if roomID=null it does not exist.", alias="roomName")
    room_check_in: Optional[StrictStr] = Field(default=None, description="Check-in date for the room", alias="roomCheckIn")
    room_check_out: Optional[StrictStr] = Field(default=None, description="Check-out date for the room", alias="roomCheckOut")
    room_status: Optional[StrictStr] = Field(default=None, alias="roomStatus")
    detailed_room_rates: Optional[List[Dict[str, Any]]] = Field(default=None, description="Associative object, with dates as indexes, and rates as values", alias="detailedRoomRates")
    __properties: ClassVar[List[str]] = ["roomTypeID", "roomTypeIsVirtual", "roomTypeName", "subReservationID", "guestID", "guestName", "rateID", "rateName", "adults", "children", "roomID", "roomName", "roomCheckIn", "roomCheckOut", "roomStatus", "detailedRoomRates"]

    @field_validator('room_status')
    def room_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['cancelled', 'in_house', 'checked_out', 'not_checked_in']):
            raise ValueError("must be one of enum values ('cancelled', 'in_house', 'checked_out', 'not_checked_in')")
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
        """Create an instance of GetReservationsWithRateDetailsResponseDataInnerRoomsInner from a JSON string"""
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
        # set to None if room_name (nullable) is None
        # and model_fields_set contains the field
        if self.room_name is None and "room_name" in self.model_fields_set:
            _dict['roomName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetReservationsWithRateDetailsResponseDataInnerRoomsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "roomTypeID": obj.get("roomTypeID"),
            "roomTypeIsVirtual": obj.get("roomTypeIsVirtual"),
            "roomTypeName": obj.get("roomTypeName"),
            "subReservationID": obj.get("subReservationID"),
            "guestID": obj.get("guestID"),
            "guestName": obj.get("guestName"),
            "rateID": obj.get("rateID"),
            "rateName": obj.get("rateName"),
            "adults": obj.get("adults"),
            "children": obj.get("children"),
            "roomID": obj.get("roomID"),
            "roomName": obj.get("roomName"),
            "roomCheckIn": obj.get("roomCheckIn"),
            "roomCheckOut": obj.get("roomCheckOut"),
            "roomStatus": obj.get("roomStatus"),
            "detailedRoomRates": obj.get("detailedRoomRates")
        })
        return _obj


