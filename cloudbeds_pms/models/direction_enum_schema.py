# coding: utf-8

"""
    Cloudbeds API

    <p>Welcome to the documentation for <strong>Cloudbeds API Version v2</strong>! If you are looking to learn how to use the Cloudbeds API to access guest information, reservations, or similar data for your Cloudbeds customers, then you've come to the right place.</p><p>In this document you will find all the API methods we provide along with explanations for parameters and response examples.</p><p>If you have questions about different implementation steps (e.g. how to implement OAuth 2.0), please refer to our <a href='https://integrations.cloudbeds.com/hc/en-us'>Integrations Portal</a>.</p><p>Be sure to <a href='https://go.pardot.com/l/308041/2018-07-24/qb2lg'>subscribe</a> to the monthly Cloudbeds API announcement mailing list to receive information on new additions and improvements to the Cloudbeds API and related developer tools.</p><p><strong>Endpoint:</strong> https://api.cloudbeds.com/{method}</p><p><strong>HTTPS:</strong> Our API requires HTTPS. We'll respond with an appropriate error if you're not using it.</p><p><strong>Request Format:</strong> HTTP GET, POST and PUT (Content-Type: application/x-www-form-urlencoded)</p><p><strong>Response Format:</strong> JSON</p><p><strong>Response Header:</strong> X-Request-ID is added to response headers in all calls to help accelerate support and troubleshooting.</p><p><strong><a href='https://integrations.cloudbeds.com/hc/en-us/articles/14104678058267-API-Documentation#postman-collection'><img src='https://run.pstmn.io/button.svg' alt='Run in Postman'></a></strong> use this link to access our Public collection in Postman.</p>

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DirectionEnumSchema(str, Enum):
    """
    The operator to use for the filter
    """

    """
    allowed enum values
    """
    ASC = 'asc'
    DESC = 'desc'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DirectionEnumSchema from a JSON string"""
        return cls(json.loads(json_str))


