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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from cloudbeds_pms_v1_2.models.get_guests_modified_response_data_inner_custom_fields_inner import GetGuestsModifiedResponseDataInnerCustomFieldsInner
from cloudbeds_pms_v1_2.models.get_reservations_response_data_inner_guest_list_value import GetReservationsResponseDataInnerGuestListValue
from cloudbeds_pms_v1_2.models.get_reservations_response_data_inner_rooms_inner import GetReservationsResponseDataInnerRoomsInner
from typing import Optional, Set
from typing_extensions import Self

class GetReservationsResponseDataInner(BaseModel):
    """
    GetReservationsResponseDataInner
    """ # noqa: E501
    property_id: Optional[StrictStr] = Field(default=None, description="Properties identifier", alias="propertyID")
    reservation_id: Optional[StrictStr] = Field(default=None, description="Reservation's unique identifier", alias="reservationID")
    date_created: Optional[datetime] = Field(default=None, alias="dateCreated")
    date_modified: Optional[datetime] = Field(default=None, alias="dateModified")
    status: Optional[StrictStr] = None
    guest_id: Optional[StrictStr] = Field(default=None, alias="guestID")
    profile_id: Optional[StrictStr] = Field(default=None, alias="profileID")
    guest_name: Optional[StrictStr] = Field(default=None, alias="guestName")
    start_date: Optional[date] = Field(default=None, alias="startDate")
    end_date: Optional[date] = Field(default=None, alias="endDate")
    allotment_block_code: Optional[StrictStr] = Field(default=None, description="Allotment block code", alias="allotmentBlockCode")
    adults: Optional[StrictInt] = None
    children: Optional[StrictInt] = None
    balance: Optional[Union[StrictFloat, StrictInt]] = None
    source_name: Optional[StrictStr] = Field(default=None, description="Source of reservation", alias="sourceName")
    source_id: Optional[StrictStr] = Field(default=None, description="Booking source unique id", alias="sourceID")
    third_party_identifier: Optional[StrictStr] = Field(default=None, alias="thirdPartyIdentifier")
    sub_reservation_id: Optional[StrictStr] = Field(default=None, description="If roomID or roomName are given, the respective subReservationID (to that room) is informed.", alias="subReservationID")
    custom_fields: Optional[List[GetGuestsModifiedResponseDataInnerCustomFieldsInner]] = Field(default=None, description="List of reservation custom fields. Only returned if \"includeCustomFields\" is true", alias="customFields")
    rooms: Optional[List[GetReservationsResponseDataInnerRoomsInner]] = Field(default=None, description="Array with rooms information. Only returned if \"includeAllRooms\" is true")
    guest_list: Optional[Dict[str, GetReservationsResponseDataInnerGuestListValue]] = Field(default=None, description="A map of guest IDs to guest objects (key is the Guest ID). It contains an entry for each guest included on the reservation. Only returned if \"includeGuestsDetails\" is true", alias="guestList")
    __properties: ClassVar[List[str]] = ["propertyID", "reservationID", "dateCreated", "dateModified", "status", "guestID", "profileID", "guestName", "startDate", "endDate", "allotmentBlockCode", "adults", "children", "balance", "sourceName", "sourceID", "thirdPartyIdentifier", "subReservationID", "customFields", "rooms", "guestList"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['not_confirmed', 'confirmed', 'canceled', 'checked_in', 'checked_out', 'no_show']):
            raise ValueError("must be one of enum values ('not_confirmed', 'confirmed', 'canceled', 'checked_in', 'checked_out', 'no_show')")
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
        """Create an instance of GetReservationsResponseDataInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item_custom_fields in self.custom_fields:
                if _item_custom_fields:
                    _items.append(_item_custom_fields.to_dict())
            _dict['customFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rooms (list)
        _items = []
        if self.rooms:
            for _item_rooms in self.rooms:
                if _item_rooms:
                    _items.append(_item_rooms.to_dict())
            _dict['rooms'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in guest_list (dict)
        _field_dict = {}
        if self.guest_list:
            for _key_guest_list in self.guest_list:
                if self.guest_list[_key_guest_list]:
                    _field_dict[_key_guest_list] = self.guest_list[_key_guest_list].to_dict()
            _dict['guestList'] = _field_dict
        # set to None if allotment_block_code (nullable) is None
        # and model_fields_set contains the field
        if self.allotment_block_code is None and "allotment_block_code" in self.model_fields_set:
            _dict['allotmentBlockCode'] = None

        # set to None if sub_reservation_id (nullable) is None
        # and model_fields_set contains the field
        if self.sub_reservation_id is None and "sub_reservation_id" in self.model_fields_set:
            _dict['subReservationID'] = None

        # set to None if custom_fields (nullable) is None
        # and model_fields_set contains the field
        if self.custom_fields is None and "custom_fields" in self.model_fields_set:
            _dict['customFields'] = None

        # set to None if guest_list (nullable) is None
        # and model_fields_set contains the field
        if self.guest_list is None and "guest_list" in self.model_fields_set:
            _dict['guestList'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetReservationsResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "propertyID": obj.get("propertyID"),
            "reservationID": obj.get("reservationID"),
            "dateCreated": obj.get("dateCreated"),
            "dateModified": obj.get("dateModified"),
            "status": obj.get("status"),
            "guestID": obj.get("guestID"),
            "profileID": obj.get("profileID"),
            "guestName": obj.get("guestName"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "allotmentBlockCode": obj.get("allotmentBlockCode"),
            "adults": obj.get("adults"),
            "children": obj.get("children"),
            "balance": obj.get("balance"),
            "sourceName": obj.get("sourceName"),
            "sourceID": obj.get("sourceID"),
            "thirdPartyIdentifier": obj.get("thirdPartyIdentifier"),
            "subReservationID": obj.get("subReservationID"),
            "customFields": [GetGuestsModifiedResponseDataInnerCustomFieldsInner.from_dict(_item) for _item in obj["customFields"]] if obj.get("customFields") is not None else None,
            "rooms": [GetReservationsResponseDataInnerRoomsInner.from_dict(_item) for _item in obj["rooms"]] if obj.get("rooms") is not None else None,
            "guestList": dict(
                (_k, GetReservationsResponseDataInnerGuestListValue.from_dict(_v))
                for _k, _v in obj["guestList"].items()
            )
            if obj.get("guestList") is not None
            else None
        })
        return _obj


