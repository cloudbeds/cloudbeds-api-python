# coding: utf-8

"""
    Cloudbeds API

    <p>     Welcome to the documentation for <strong>Cloudbeds API Version v1.2</strong>!     If you are looking to learn how to use the Cloudbeds API to access guest information, reservations, or similar data     for your Cloudbeds customers, then you've come to the right place. </p>  <p>     In this document you will find all the API methods we provide along with explanations for parameters and response     examples. </p>  <p>     If you have questions about different implementation steps (e.g. how to implement OAuth 2.0), please refer to our     <a href=\"https://integrations.cloudbeds.com/hc/en-us\">Integrations Portal</a>. </p>  <p>     Be sure to <a href=\"https://go.pardot.com/l/308041/2018-07-24/qb2lg\">subscribe</a> to the monthly     Cloudbeds API announcement mailing list to receive information on new additions and improvements to the     Cloudbeds API and related developer tools. </p>  <p>     <strong>Endpoint:</strong> https://api.cloudbeds.com/api/v1.2/{method} </p>  <p>     <strong>HTTPS:</strong> Our API requires HTTPS. We'll respond with an appropriate error if you're not using it. </p>  <p>     <strong>Request Format:</strong> HTTP GET, POST and PUT (Content-Type: application/x-www-form-urlencoded) </p>  <p>     <strong>Response Format:</strong> JSON </p>  <p>     <strong>Response Header:</strong> X-Request-ID is added to response headers in all calls to help accelerate support     and troubleshooting. </p>  <p>     <strong>         <a href=\"https://integrations.cloudbeds.com/hc/en-us/articles/14104678058267-API-Documentation#postman-collection\">             <img src=\"https://run.pstmn.io/button.svg\" alt=\"Run in Postman\">         </a>     </strong> use this link to access our Public collection in Postman. </p>

    The version of the OpenAPI document: v1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cloudbeds_pms_v1_2.models.get_hotel_details_response_data import GetHotelDetailsResponseData

class TestGetHotelDetailsResponseData(unittest.TestCase):
    """GetHotelDetailsResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetHotelDetailsResponseData:
        """Test GetHotelDetailsResponseData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetHotelDetailsResponseData`
        """
        model = GetHotelDetailsResponseData()
        if include_optional:
            return GetHotelDetailsResponseData(
                property_id = '',
                organization_id = '',
                property_name = '',
                property_type = '',
                property_image = [
                    cloudbeds_pms_v1_2.models.get_hotel_details_response_data_property_image_inner.GetHotelDetailsResponse_data_propertyImage_inner(
                        thumb = '', 
                        image = '', )
                    ],
                property_description = '',
                property_currency = cloudbeds_pms_v1_2.models.get_hotel_details_response_data_property_currency.GetHotelDetailsResponse_data_propertyCurrency(
                    currency_code = '', 
                    currency_symbol = '', 
                    currency_position = 'before', ),
                property_primary_language = '',
                property_additional_photos = [
                    cloudbeds_pms_v1_2.models.get_hotel_details_response_data_property_image_inner.GetHotelDetailsResponse_data_propertyImage_inner(
                        thumb = '', 
                        image = '', )
                    ],
                property_phone = '',
                property_email = '',
                property_address = cloudbeds_pms_v1_2.models.get_hotel_details_response_data_property_address.GetHotelDetailsResponse_data_propertyAddress(
                    property_address1 = '', 
                    property_address2 = '', 
                    property_city = '', 
                    property_state = '', 
                    property_zip = '', 
                    property_country = '', 
                    property_latitude = '', 
                    property_longitude = '', ),
                property_policy = cloudbeds_pms_v1_2.models.get_hotel_details_response_data_property_policy.GetHotelDetailsResponse_data_propertyPolicy(
                    property_check_in_time = '', 
                    property_check_out_time = '', 
                    property_late_check_out_allowed = True, 
                    property_late_check_out_type = 'value', 
                    property_late_check_out_value = '', 
                    property_terms_and_conditions = '', 
                    property_full_payment_before_checkin = True, ),
                property_amenities = [
                    ''
                    ],
                tax_id = '',
                tax_id2 = '',
                company_legal_name = ''
            )
        else:
            return GetHotelDetailsResponseData(
        )
        """

    def testGetHotelDetailsResponseData(self):
        """Test GetHotelDetailsResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
