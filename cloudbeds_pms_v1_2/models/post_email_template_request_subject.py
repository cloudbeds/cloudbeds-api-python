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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PostEmailTemplateRequestSubject(BaseModel):
    """
    Email message subject. The subject key should be a language code (IETF). A few examples are listed below.
    """ # noqa: E501
    en: Optional[StrictStr] = Field(default=None, description="Email message subject in English")
    es: Optional[StrictStr] = Field(default=None, description="Email message subject in Spanish")
    ru: Optional[StrictStr] = Field(default=None, description="Email message subject in Russian")
    pt_br: Optional[StrictStr] = Field(default=None, description="Email message subject in Portuguese", alias="pt-br")
    __properties: ClassVar[List[str]] = ["en", "es", "ru", "pt-br"]

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
        """Create an instance of PostEmailTemplateRequestSubject from a JSON string"""
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
        # set to None if en (nullable) is None
        # and model_fields_set contains the field
        if self.en is None and "en" in self.model_fields_set:
            _dict['en'] = None

        # set to None if es (nullable) is None
        # and model_fields_set contains the field
        if self.es is None and "es" in self.model_fields_set:
            _dict['es'] = None

        # set to None if ru (nullable) is None
        # and model_fields_set contains the field
        if self.ru is None and "ru" in self.model_fields_set:
            _dict['ru'] = None

        # set to None if pt_br (nullable) is None
        # and model_fields_set contains the field
        if self.pt_br is None and "pt_br" in self.model_fields_set:
            _dict['pt-br'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostEmailTemplateRequestSubject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "en": obj.get("en"),
            "es": obj.get("es"),
            "ru": obj.get("ru"),
            "pt-br": obj.get("pt-br")
        })
        return _obj


