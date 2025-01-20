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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class GetTransactionsResponseDataInner(BaseModel):
    """
    GetTransactionsResponseDataInner
    """ # noqa: E501
    property_id: Optional[StrictStr] = Field(default=None, description="Property ID", alias="propertyID")
    reservation_id: Optional[StrictStr] = Field(default=None, description="Reservation ID", alias="reservationID")
    sub_reservation_id: Optional[StrictStr] = Field(default=None, description="Sub Reservation ID", alias="subReservationID")
    house_account_id: Optional[StrictStr] = Field(default=None, description="House Account ID", alias="houseAccountID")
    house_account_name: Optional[StrictStr] = Field(default=None, description="House Account Name", alias="houseAccountName")
    guest_id: Optional[StrictStr] = Field(default=None, description="Guest ID", alias="guestID")
    property_name: Optional[StrictStr] = Field(default=None, description="Property Name", alias="propertyName")
    transaction_date_time: Optional[datetime] = Field(default=None, description="DateTime that the transaction was stored", alias="transactionDateTime")
    transaction_date_time_utc: Optional[datetime] = Field(default=None, description="DateTime that the transaction was stored, in UTC timezone", alias="transactionDateTimeUTC")
    transaction_modified_date_time: Optional[datetime] = Field(default=None, description="DateTime that the transaction was last modified", alias="transactionModifiedDateTime")
    transaction_modified_date_time_utc: Optional[datetime] = Field(default=None, description="DateTime that the transaction was last modified, in UTC timezone", alias="transactionModifiedDateTimeUTC")
    guest_check_in: Optional[date] = Field(default=None, description="Reservation Check-in date", alias="guestCheckIn")
    guest_check_out: Optional[date] = Field(default=None, description="Reservation Check-out date", alias="guestCheckOut")
    room_type_id: Optional[StrictStr] = Field(default=None, description="ID of the room type", alias="roomTypeID")
    room_type_name: Optional[StrictStr] = Field(default=None, description="Name of the room type", alias="roomTypeName")
    room_name: Optional[StrictStr] = Field(default=None, description="Name of the specific room. N/A means not applicable, and it is used if the transaction is not linked to a room.", alias="roomName")
    guest_name: Optional[StrictStr] = Field(default=None, description="Name of the first guest of the reservation", alias="guestName")
    description: Optional[StrictStr] = Field(default=None, description="Description of the transaction")
    category: Optional[StrictStr] = Field(default=None, description="Category of the transaction")
    transaction_code: Optional[StrictStr] = Field(default=None, description="Transaction identifier that can be used, or left blank", alias="transactionCode")
    notes: Optional[StrictStr] = Field(default=None, description="If any special information needs to be added to the transaction, it will be in this field")
    quantity: Optional[StrictInt] = None
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Consolidated amount on the transaction (Credit - Debit)")
    currency: Optional[StrictStr] = Field(default=None, description="Currency of the transaction")
    user_name: Optional[StrictStr] = Field(default=None, description="User responsible for creating the transaction", alias="userName")
    transaction_type: Optional[StrictStr] = Field(default=None, description="Consolidated transaction type", alias="transactionType")
    transaction_category: Optional[StrictStr] = Field(default=None, description="Transaction category", alias="transactionCategory")
    item_category_name: Optional[StrictStr] = Field(default=None, description="Item category name", alias="itemCategoryName")
    transaction_id: Optional[StrictStr] = Field(default=None, description="Transaction identifier", alias="transactionID")
    parent_transaction_id: Optional[StrictStr] = Field(default=None, description="Parent transaction identifier. Parent transaction is a transaction to which this current transaction is strongly related to or derived from.<br/> Example: Parent transaction to a room rate tax is a room rate.<br/> This parent transaction ID will mostly be present on transactions that are taxes, fees and voids. It will not be present on room rates, items, payments and refunds.", alias="parentTransactionID")
    card_type: Optional[StrictStr] = Field(default=None, description="Abbreviated name of credit card type", alias="cardType")
    is_deleted: Optional[StrictBool] = Field(default=None, alias="isDeleted")
    __properties: ClassVar[List[str]] = ["propertyID", "reservationID", "subReservationID", "houseAccountID", "houseAccountName", "guestID", "propertyName", "transactionDateTime", "transactionDateTimeUTC", "transactionModifiedDateTime", "transactionModifiedDateTimeUTC", "guestCheckIn", "guestCheckOut", "roomTypeID", "roomTypeName", "roomName", "guestName", "description", "category", "transactionCode", "notes", "quantity", "amount", "currency", "userName", "transactionType", "transactionCategory", "itemCategoryName", "transactionID", "parentTransactionID", "cardType", "isDeleted"]

    @field_validator('transaction_type')
    def transaction_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['debit', 'credit']):
            raise ValueError("must be one of enum values ('debit', 'credit')")
        return value

    @field_validator('transaction_category')
    def transaction_category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['adjustment', 'addon', 'custom_item', 'fee', 'payment', 'product', 'rate', 'room_revenue', 'refund', 'tax', 'void']):
            raise ValueError("must be one of enum values ('adjustment', 'addon', 'custom_item', 'fee', 'payment', 'product', 'rate', 'room_revenue', 'refund', 'tax', 'void')")
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
        """Create an instance of GetTransactionsResponseDataInner from a JSON string"""
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
        # set to None if house_account_id (nullable) is None
        # and model_fields_set contains the field
        if self.house_account_id is None and "house_account_id" in self.model_fields_set:
            _dict['houseAccountID'] = None

        # set to None if house_account_name (nullable) is None
        # and model_fields_set contains the field
        if self.house_account_name is None and "house_account_name" in self.model_fields_set:
            _dict['houseAccountName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetTransactionsResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "propertyID": obj.get("propertyID"),
            "reservationID": obj.get("reservationID"),
            "subReservationID": obj.get("subReservationID"),
            "houseAccountID": obj.get("houseAccountID"),
            "houseAccountName": obj.get("houseAccountName"),
            "guestID": obj.get("guestID"),
            "propertyName": obj.get("propertyName"),
            "transactionDateTime": obj.get("transactionDateTime"),
            "transactionDateTimeUTC": obj.get("transactionDateTimeUTC"),
            "transactionModifiedDateTime": obj.get("transactionModifiedDateTime"),
            "transactionModifiedDateTimeUTC": obj.get("transactionModifiedDateTimeUTC"),
            "guestCheckIn": obj.get("guestCheckIn"),
            "guestCheckOut": obj.get("guestCheckOut"),
            "roomTypeID": obj.get("roomTypeID"),
            "roomTypeName": obj.get("roomTypeName"),
            "roomName": obj.get("roomName"),
            "guestName": obj.get("guestName"),
            "description": obj.get("description"),
            "category": obj.get("category"),
            "transactionCode": obj.get("transactionCode"),
            "notes": obj.get("notes"),
            "quantity": obj.get("quantity"),
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "userName": obj.get("userName"),
            "transactionType": obj.get("transactionType"),
            "transactionCategory": obj.get("transactionCategory"),
            "itemCategoryName": obj.get("itemCategoryName"),
            "transactionID": obj.get("transactionID"),
            "parentTransactionID": obj.get("parentTransactionID"),
            "cardType": obj.get("cardType"),
            "isDeleted": obj.get("isDeleted")
        })
        return _obj


