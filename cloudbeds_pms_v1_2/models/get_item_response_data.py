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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from cloudbeds_pms_v1_2.models.get_item_response_data_fees_inner import GetItemResponseDataFeesInner
from cloudbeds_pms_v1_2.models.get_item_response_data_taxes_inner import GetItemResponseDataTaxesInner
from typing import Optional, Set
from typing_extensions import Self

class GetItemResponseData(BaseModel):
    """
    Item details
    """ # noqa: E501
    item_id: Optional[StrictStr] = Field(default=None, description="Item unique identifier", alias="itemID")
    item_type: Optional[StrictStr] = Field(default=None, description="Item type", alias="itemType")
    sku: Optional[StrictStr] = Field(default=None, description="Item SKU")
    item_code: Optional[StrictStr] = Field(default=None, description="Item code", alias="itemCode")
    name: Optional[StrictStr] = Field(default=None, description="Item name")
    category_id: Optional[StrictStr] = Field(default=None, description="Item category identifier. Null if unset", alias="categoryID")
    category_name: Optional[StrictStr] = Field(default=None, description="Item category name. Empty if unset", alias="categoryName")
    description: Optional[StrictStr] = Field(default=None, description="Item description")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Item price")
    stock_inventory: Optional[StrictBool] = Field(default=None, description="Track stock inventory for this item", alias="stockInventory")
    item_quantity: Optional[StrictInt] = Field(default=None, description="<sup>1</sup> Current amount of item available", alias="itemQuantity")
    reorder_threshold: Optional[StrictInt] = Field(default=None, description="<sup>1</sup> Quantity at which to reorder item", alias="reorderThreshold")
    reorder_needed: Optional[StrictBool] = Field(default=None, description="<sup>1</sup> true - Whether item is at or below value set for reorder threshold.", alias="reorderNeeded")
    stop_sell: Optional[StrictInt] = Field(default=None, description="<sup>1</sup> Quantity at which to stop selling product.", alias="stopSell")
    stop_sell_met: Optional[StrictBool] = Field(default=None, description="<sup>1</sup> true - Whether item is at or below value set for stop-sell threshold.", alias="stopSellMet")
    taxes: Optional[List[GetItemResponseDataTaxesInner]] = Field(default=None, description="<sup>2</sup> Details of the taxes applicable")
    total_taxes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="<sup>2</sup> Total value of the taxes", alias="totalTaxes")
    fees: Optional[List[GetItemResponseDataFeesInner]] = Field(default=None, description="<sup>2</sup> Details of the fees applicable")
    total_fees: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="<sup>2</sup> Total value of the fees", alias="totalFees")
    price_without_fees_and_taxes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="<sup>2</sup> item price subtracting the included taxes", alias="priceWithoutFeesAndTaxes")
    grand_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="<sup>2</sup> item price with fees and taxes", alias="grandTotal")
    __properties: ClassVar[List[str]] = ["itemID", "itemType", "sku", "itemCode", "name", "categoryID", "categoryName", "description", "price", "stockInventory", "itemQuantity", "reorderThreshold", "reorderNeeded", "stopSell", "stopSellMet", "taxes", "totalTaxes", "fees", "totalFees", "priceWithoutFeesAndTaxes", "grandTotal"]

    @field_validator('item_type')
    def item_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['product', 'service']):
            raise ValueError("must be one of enum values ('product', 'service')")
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
        """Create an instance of GetItemResponseData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in taxes (list)
        _items = []
        if self.taxes:
            for _item_taxes in self.taxes:
                if _item_taxes:
                    _items.append(_item_taxes.to_dict())
            _dict['taxes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fees (list)
        _items = []
        if self.fees:
            for _item_fees in self.fees:
                if _item_fees:
                    _items.append(_item_fees.to_dict())
            _dict['fees'] = _items
        # set to None if item_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.item_quantity is None and "item_quantity" in self.model_fields_set:
            _dict['itemQuantity'] = None

        # set to None if reorder_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.reorder_threshold is None and "reorder_threshold" in self.model_fields_set:
            _dict['reorderThreshold'] = None

        # set to None if reorder_needed (nullable) is None
        # and model_fields_set contains the field
        if self.reorder_needed is None and "reorder_needed" in self.model_fields_set:
            _dict['reorderNeeded'] = None

        # set to None if stop_sell (nullable) is None
        # and model_fields_set contains the field
        if self.stop_sell is None and "stop_sell" in self.model_fields_set:
            _dict['stopSell'] = None

        # set to None if stop_sell_met (nullable) is None
        # and model_fields_set contains the field
        if self.stop_sell_met is None and "stop_sell_met" in self.model_fields_set:
            _dict['stopSellMet'] = None

        # set to None if taxes (nullable) is None
        # and model_fields_set contains the field
        if self.taxes is None and "taxes" in self.model_fields_set:
            _dict['taxes'] = None

        # set to None if total_taxes (nullable) is None
        # and model_fields_set contains the field
        if self.total_taxes is None and "total_taxes" in self.model_fields_set:
            _dict['totalTaxes'] = None

        # set to None if fees (nullable) is None
        # and model_fields_set contains the field
        if self.fees is None and "fees" in self.model_fields_set:
            _dict['fees'] = None

        # set to None if total_fees (nullable) is None
        # and model_fields_set contains the field
        if self.total_fees is None and "total_fees" in self.model_fields_set:
            _dict['totalFees'] = None

        # set to None if price_without_fees_and_taxes (nullable) is None
        # and model_fields_set contains the field
        if self.price_without_fees_and_taxes is None and "price_without_fees_and_taxes" in self.model_fields_set:
            _dict['priceWithoutFeesAndTaxes'] = None

        # set to None if grand_total (nullable) is None
        # and model_fields_set contains the field
        if self.grand_total is None and "grand_total" in self.model_fields_set:
            _dict['grandTotal'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetItemResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "itemID": obj.get("itemID"),
            "itemType": obj.get("itemType"),
            "sku": obj.get("sku"),
            "itemCode": obj.get("itemCode"),
            "name": obj.get("name"),
            "categoryID": obj.get("categoryID"),
            "categoryName": obj.get("categoryName"),
            "description": obj.get("description"),
            "price": obj.get("price"),
            "stockInventory": obj.get("stockInventory"),
            "itemQuantity": obj.get("itemQuantity"),
            "reorderThreshold": obj.get("reorderThreshold"),
            "reorderNeeded": obj.get("reorderNeeded"),
            "stopSell": obj.get("stopSell"),
            "stopSellMet": obj.get("stopSellMet"),
            "taxes": [GetItemResponseDataTaxesInner.from_dict(_item) for _item in obj["taxes"]] if obj.get("taxes") is not None else None,
            "totalTaxes": obj.get("totalTaxes"),
            "fees": [GetItemResponseDataFeesInner.from_dict(_item) for _item in obj["fees"]] if obj.get("fees") is not None else None,
            "totalFees": obj.get("totalFees"),
            "priceWithoutFeesAndTaxes": obj.get("priceWithoutFeesAndTaxes"),
            "grandTotal": obj.get("grandTotal")
        })
        return _obj


