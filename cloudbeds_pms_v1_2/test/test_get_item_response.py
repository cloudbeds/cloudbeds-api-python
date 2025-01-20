# coding: utf-8

"""
    Cloudbeds API

    <p>     Welcome to the documentation for <strong>Cloudbeds API Version v1.2</strong>!     If you are looking to learn how to use the Cloudbeds API to access guest information, reservations, or similar data     for your Cloudbeds customers, then you've come to the right place. </p>  <p>     In this document you will find all the API methods we provide along with explanations for parameters and response     examples. </p>  <p>     If you have questions about different implementation steps (e.g. how to implement OAuth 2.0), please refer to our     <a href=\"https://integrations.cloudbeds.com/hc/en-us\">Integrations Portal</a>. </p>  <p>     Be sure to <a href=\"https://go.pardot.com/l/308041/2018-07-24/qb2lg\">subscribe</a> to the monthly     Cloudbeds API announcement mailing list to receive information on new additions and improvements to the     Cloudbeds API and related developer tools. </p>  <p>     <strong>Endpoint:</strong> https://api.cloudbeds.com/api/v1.2/{method} </p>  <p>     <strong>HTTPS:</strong> Our API requires HTTPS. We'll respond with an appropriate error if you're not using it. </p>  <p>     <strong>Request Format:</strong> HTTP GET, POST and PUT (Content-Type: application/x-www-form-urlencoded) </p>  <p>     <strong>Response Format:</strong> JSON </p>  <p>     <strong>Response Header:</strong> X-Request-ID is added to response headers in all calls to help accelerate support     and troubleshooting. </p>  <p>     <strong>         <a href=\"https://integrations.cloudbeds.com/hc/en-us/articles/14104678058267-API-Documentation#postman-collection\">             <img src=\"https://run.pstmn.io/button.svg\" alt=\"Run in Postman\">         </a>     </strong> use this link to access our Public collection in Postman. </p>

    The version of the OpenAPI document: v1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cloudbeds_pms_v1_2.models.get_item_response import GetItemResponse

class TestGetItemResponse(unittest.TestCase):
    """GetItemResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetItemResponse:
        """Test GetItemResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetItemResponse`
        """
        model = GetItemResponse()
        if include_optional:
            return GetItemResponse(
                success = True,
                data = cloudbeds_pms_v1_2.models.get_item_response_data.GetItemResponse_data(
                    item_id = '', 
                    item_type = 'product', 
                    sku = '', 
                    item_code = '', 
                    name = '', 
                    category_id = '', 
                    category_name = '', 
                    description = '', 
                    price = 1.337, 
                    stock_inventory = True, 
                    item_quantity = 56, 
                    reorder_threshold = 56, 
                    reorder_needed = True, 
                    stop_sell = 56, 
                    stop_sell_met = True, 
                    taxes = [
                        cloudbeds_pms_v1_2.models.get_item_response_data_taxes_inner.GetItemResponse_data_taxes_inner(
                            tax_name = '', 
                            tax_value = 1.337, )
                        ], 
                    total_taxes = 1.337, 
                    fees = [
                        cloudbeds_pms_v1_2.models.get_item_response_data_fees_inner.GetItemResponse_data_fees_inner(
                            fee_name = '', 
                            fee_value = 1.337, )
                        ], 
                    total_fees = 1.337, 
                    price_without_fees_and_taxes = 1.337, 
                    grand_total = 1.337, ),
                message = ''
            )
        else:
            return GetItemResponse(
        )
        """

    def testGetItemResponse(self):
        """Test GetItemResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
