# coding: utf-8

"""
    Cloudbeds API

    <p>     Welcome to the documentation for <strong>Cloudbeds API Version v1.2</strong>!     If you are looking to learn how to use the Cloudbeds API to access guest information, reservations, or similar data     for your Cloudbeds customers, then you've come to the right place. </p>  <p>     In this document you will find all the API methods we provide along with explanations for parameters and response     examples. </p>  <p>     If you have questions about different implementation steps (e.g. how to implement OAuth 2.0), please refer to our     <a href=\"https://integrations.cloudbeds.com/hc/en-us\">Integrations Portal</a>. </p>  <p>     Be sure to <a href=\"https://go.pardot.com/l/308041/2018-07-24/qb2lg\">subscribe</a> to the monthly     Cloudbeds API announcement mailing list to receive information on new additions and improvements to the     Cloudbeds API and related developer tools. </p>  <p>     <strong>Endpoint:</strong> https://api.cloudbeds.com/api/v1.2/{method} </p>  <p>     <strong>HTTPS:</strong> Our API requires HTTPS. We'll respond with an appropriate error if you're not using it. </p>  <p>     <strong>Request Format:</strong> HTTP GET, POST and PUT (Content-Type: application/x-www-form-urlencoded) </p>  <p>     <strong>Response Format:</strong> JSON </p>  <p>     <strong>Response Header:</strong> X-Request-ID is added to response headers in all calls to help accelerate support     and troubleshooting. </p>  <p>     <strong>         <a href=\"https://integrations.cloudbeds.com/hc/en-us/articles/14104678058267-API-Documentation#postman-collection\">             <img src=\"https://run.pstmn.io/button.svg\" alt=\"Run in Postman\">         </a>     </strong> use this link to access our Public collection in Postman. </p>

    The version of the OpenAPI document: v1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cloudbeds_pms_v1_2.models.get_allotment_blocks_response_data_inner_allotment_intervals_inner import GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner

class TestGetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner(unittest.TestCase):
    """GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner:
        """Test GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner`
        """
        model = GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner()
        if include_optional:
            return GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner(
                room_type_id = '',
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                availability = [
                    cloudbeds_pms_v1_2.models.get_allotment_blocks_response_data_inner_allotment_intervals_inner_availability_inner.GetAllotmentBlocksResponse_data_inner_allotmentIntervals_inner_availability_inner(
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        block_remaining = 56, 
                        block_allotted = 56, 
                        block_confirmed = 56, 
                        rate = '', 
                        guest_pricing = cloudbeds_pms_v1_2.models.post_create_allotment_block_response_data_inner_allotment_intervals_inner_availability_guest_pricing.PostCreateAllotmentBlockResponse_data_inner_allotmentIntervals_inner_availability_guestPricing(
                            adult1 = '', 
                            adult2 = '', 
                            adult3 = '', 
                            child1 = '', 
                            child2 = '', 
                            child3 = '', ), )
                    ],
                restrictions = cloudbeds_pms_v1_2.models.get_allotment_blocks_response_data_inner_allotment_intervals_inner_restrictions.GetAllotmentBlocksResponse_data_inner_allotmentIntervals_inner_restrictions(
                    min_los = 56, 
                    max_los = 56, 
                    cut_off_days = 56, 
                    last_minute_booking_days = 56, 
                    closed_to_arrival = 56, 
                    closed_to_departure = 56, )
            )
        else:
            return GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner(
        )
        """

    def testGetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner(self):
        """Test GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
