# cloudbeds_pms_v1_2.TaxesAndFeesApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_taxes_and_fees_get**](TaxesAndFeesApi.md#get_taxes_and_fees_get) | **GET** /getTaxesAndFees | getTaxesAndFees


# **get_taxes_and_fees_get**
> GetTaxesAndFeesResponse get_taxes_and_fees_get(property_id=property_id, include_deleted=include_deleted, include_expired=include_expired)

getTaxesAndFees

Returns the taxes and fees set for the property. Read the [Rate-Based tax (Dynamic Tax) guide](https://myfrontdesk.cloudbeds.com/hc/en-us/articles/360014103514-rate-based-tax-dynamic-tax) to understand its usage.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.get_taxes_and_fees_response import GetTaxesAndFeesResponse
from cloudbeds_pms_v1_2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.2
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_2.Configuration(
    host = "https://api.cloudbeds.com/api/v1.2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudbeds_pms_v1_2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_2.TaxesAndFeesApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    include_deleted = False # bool | If the response should include deleted taxes and fees (optional) (default to False)
    include_expired = False # bool | If the response should include expired taxes and fees (optional) (default to False)

    try:
        # getTaxesAndFees
        api_response = api_instance.get_taxes_and_fees_get(property_id=property_id, include_deleted=include_deleted, include_expired=include_expired)
        print("The response of TaxesAndFeesApi->get_taxes_and_fees_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxesAndFeesApi->get_taxes_and_fees_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **include_deleted** | **bool**| If the response should include deleted taxes and fees | [optional] [default to False]
 **include_expired** | **bool**| If the response should include expired taxes and fees | [optional] [default to False]

### Return type

[**GetTaxesAndFeesResponse**](GetTaxesAndFeesResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

