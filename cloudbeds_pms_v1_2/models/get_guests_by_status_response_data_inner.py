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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cloudbeds_pms_v1_2.models.get_guests_modified_response_data_inner_custom_fields_inner import GetGuestsModifiedResponseDataInnerCustomFieldsInner
from typing import Optional, Set
from typing_extensions import Self

class GetGuestsByStatusResponseDataInner(BaseModel):
    """
    GetGuestsByStatusResponseDataInner
    """ # noqa: E501
    guest_id: Optional[StrictStr] = Field(default=None, description="Guest ID", alias="guestID")
    reservation_id: Optional[StrictStr] = Field(default=None, description="Reservation's unique identifier", alias="reservationID")
    sub_reservation_id: Optional[StrictStr] = Field(default=None, alias="subReservationID")
    reservation_created_date_time: Optional[datetime] = Field(default=None, description="Reservation creation datetime", alias="reservationCreatedDateTime")
    room_type_id: Optional[StrictStr] = Field(default=None, description="Room Type ID that the guest is assigned", alias="roomTypeID")
    room_id: Optional[StrictStr] = Field(default=None, description="Room ID that the guest is assigned", alias="roomID")
    room_name: Optional[StrictStr] = Field(default=None, description="Name of the room where guest is assigned", alias="roomName")
    guest_first_name: Optional[StrictStr] = Field(default=None, description="First Name", alias="guestFirstName")
    guest_last_name: Optional[StrictStr] = Field(default=None, description="Last Name", alias="guestLastName")
    guest_gender: Optional[StrictStr] = Field(default=None, description="Gender", alias="guestGender")
    guest_email: Optional[StrictStr] = Field(default=None, description="Email Address", alias="guestEmail")
    guest_phone: Optional[StrictStr] = Field(default=None, description="Phone Number", alias="guestPhone")
    guest_cell_phone: Optional[StrictStr] = Field(default=None, description="Cell Phone Number", alias="guestCellPhone")
    guest_address1: Optional[StrictStr] = Field(default=None, description="Address", alias="guestAddress1")
    guest_address2: Optional[StrictStr] = Field(default=None, description="Address line 2", alias="guestAddress2")
    guest_city: Optional[StrictStr] = Field(default=None, description="Address city", alias="guestCity")
    guest_state: Optional[StrictStr] = Field(default=None, description="Address state", alias="guestState")
    guest_country: Optional[StrictStr] = Field(default=None, description="Address country", alias="guestCountry")
    guest_zip: Optional[StrictStr] = Field(default=None, description="Address zip code", alias="guestZip")
    guest_birth_date: Optional[date] = Field(default=None, description="Guests Date of Birth", alias="guestBirthDate")
    guest_document_type: Optional[StrictStr] = Field(default=None, description="Document Type", alias="guestDocumentType")
    guest_document_number: Optional[StrictStr] = Field(default=None, description="Document Number", alias="guestDocumentNumber")
    guest_document_issue_date: Optional[date] = Field(default=None, description="Document Issue Date", alias="guestDocumentIssueDate")
    guest_document_issuing_country: Optional[StrictStr] = Field(default=None, description="Document Issuing Country", alias="guestDocumentIssuingCountry")
    guest_document_expiration_date: Optional[date] = Field(default=None, description="Document Expiration Date", alias="guestDocumentExpirationDate")
    start_date: Optional[datetime] = Field(default=None, description="Check-in date", alias="startDate")
    end_date: Optional[datetime] = Field(default=None, description="Check-out date", alias="endDate")
    custom_fields: Optional[List[GetGuestsModifiedResponseDataInnerCustomFieldsInner]] = Field(default=None, description="List of custom fields", alias="customFields")
    date_modified: Optional[datetime] = Field(default=None, description="Guest modification date", alias="dateModified")
    current_status: Optional[StrictStr] = Field(default=None, description="Current Status of the guest. Does not need to be equal to the status looked for (it may have had a status change outside of the filtered date range).", alias="currentStatus")
    status_date: Optional[datetime] = Field(default=None, description="DateTime when the last status modification occurred.", alias="statusDate")
    tax_id: Optional[StrictStr] = Field(default=None, description="Tax ID", alias="taxID")
    company_tax_id: Optional[StrictStr] = Field(default=None, description="Company tax ID", alias="companyTaxID")
    company_name: Optional[StrictStr] = Field(default=None, description="Company name", alias="companyName")
    is_anonymized: Optional[StrictBool] = Field(default=None, description="Flag indicating the guest data was removed upon request", alias="isAnonymized")
    is_deleted: Optional[StrictBool] = Field(default=None, description="Flag indicating the guest's reservation was removed", alias="isDeleted")
    guest_opt_in: Optional[StrictBool] = Field(default=None, description="If guest has opted-in to marketing communication or not", alias="guestOptIn")
    is_merged: Optional[StrictBool] = Field(default=None, description="Flag indicating that guest was merged", alias="isMerged")
    new_guest_id: Optional[StrictStr] = Field(default=None, description="Merged guest ID", alias="newGuestID")
    __properties: ClassVar[List[str]] = ["guestID", "reservationID", "subReservationID", "reservationCreatedDateTime", "roomTypeID", "roomID", "roomName", "guestFirstName", "guestLastName", "guestGender", "guestEmail", "guestPhone", "guestCellPhone", "guestAddress1", "guestAddress2", "guestCity", "guestState", "guestCountry", "guestZip", "guestBirthDate", "guestDocumentType", "guestDocumentNumber", "guestDocumentIssueDate", "guestDocumentIssuingCountry", "guestDocumentExpirationDate", "startDate", "endDate", "customFields", "dateModified", "currentStatus", "statusDate", "taxID", "companyTaxID", "companyName", "isAnonymized", "isDeleted", "guestOptIn", "isMerged", "newGuestID"]

    @field_validator('guest_gender')
    def guest_gender_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['M', 'F', 'N/A']):
            raise ValueError("must be one of enum values ('M', 'F', 'N/A')")
        return value

    @field_validator('current_status')
    def current_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['canceled', 'checked_out', 'in_house', 'not_checked_in']):
            raise ValueError("must be one of enum values ('canceled', 'checked_out', 'in_house', 'not_checked_in')")
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
        """Create an instance of GetGuestsByStatusResponseDataInner from a JSON string"""
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
        # set to None if tax_id (nullable) is None
        # and model_fields_set contains the field
        if self.tax_id is None and "tax_id" in self.model_fields_set:
            _dict['taxID'] = None

        # set to None if company_tax_id (nullable) is None
        # and model_fields_set contains the field
        if self.company_tax_id is None and "company_tax_id" in self.model_fields_set:
            _dict['companyTaxID'] = None

        # set to None if company_name (nullable) is None
        # and model_fields_set contains the field
        if self.company_name is None and "company_name" in self.model_fields_set:
            _dict['companyName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetGuestsByStatusResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "guestID": obj.get("guestID"),
            "reservationID": obj.get("reservationID"),
            "subReservationID": obj.get("subReservationID"),
            "reservationCreatedDateTime": obj.get("reservationCreatedDateTime"),
            "roomTypeID": obj.get("roomTypeID"),
            "roomID": obj.get("roomID"),
            "roomName": obj.get("roomName"),
            "guestFirstName": obj.get("guestFirstName"),
            "guestLastName": obj.get("guestLastName"),
            "guestGender": obj.get("guestGender"),
            "guestEmail": obj.get("guestEmail"),
            "guestPhone": obj.get("guestPhone"),
            "guestCellPhone": obj.get("guestCellPhone"),
            "guestAddress1": obj.get("guestAddress1"),
            "guestAddress2": obj.get("guestAddress2"),
            "guestCity": obj.get("guestCity"),
            "guestState": obj.get("guestState"),
            "guestCountry": obj.get("guestCountry"),
            "guestZip": obj.get("guestZip"),
            "guestBirthDate": obj.get("guestBirthDate"),
            "guestDocumentType": obj.get("guestDocumentType"),
            "guestDocumentNumber": obj.get("guestDocumentNumber"),
            "guestDocumentIssueDate": obj.get("guestDocumentIssueDate"),
            "guestDocumentIssuingCountry": obj.get("guestDocumentIssuingCountry"),
            "guestDocumentExpirationDate": obj.get("guestDocumentExpirationDate"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "customFields": [GetGuestsModifiedResponseDataInnerCustomFieldsInner.from_dict(_item) for _item in obj["customFields"]] if obj.get("customFields") is not None else None,
            "dateModified": obj.get("dateModified"),
            "currentStatus": obj.get("currentStatus"),
            "statusDate": obj.get("statusDate"),
            "taxID": obj.get("taxID"),
            "companyTaxID": obj.get("companyTaxID"),
            "companyName": obj.get("companyName"),
            "isAnonymized": obj.get("isAnonymized"),
            "isDeleted": obj.get("isDeleted"),
            "guestOptIn": obj.get("guestOptIn"),
            "isMerged": obj.get("isMerged"),
            "newGuestID": obj.get("newGuestID")
        })
        return _obj


