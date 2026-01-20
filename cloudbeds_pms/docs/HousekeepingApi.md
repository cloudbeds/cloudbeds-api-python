# cloudbeds_pms.HousekeepingApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_27abd48cb30106ec3251cf3baf34174c**](HousekeepingApi.md#call_27abd48cb30106ec3251cf3baf34174c) | **GET** /housekeeping/v1/inspections/{propertyId} | Housekeeping inspection list


# **call_27abd48cb30106ec3251cf3baf34174c**
> InspectionListResponseSchema call_27abd48cb30106ec3251cf3baf34174c(property_id, limit=limit, offset=offset, filters=filters)

Housekeeping inspection list

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.inspection_list_response_schema import InspectionListResponseSchema
from cloudbeds_pms.models.query_parameter_dynamic_filter_schema import QueryParameterDynamicFilterSchema
from cloudbeds_pms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_pms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms.HousekeepingApi(api_client)
    property_id = 1 # int | The property ID
    limit = 100 # int | The maximum number of items to return in the response. Default is 100. (optional) (default to 100)
    offset = 0 # int | The number of items to skip before starting to collect the result set. Used for pagination. (optional) (default to 0)
    filters = cloudbeds_pms.QueryParameterDynamicFilterSchema() # QueryParameterDynamicFilterSchema | This parameter should be formatted as a list of strings separated by ; (optional)

    try:
        # Housekeeping inspection list
        api_response = api_instance.call_27abd48cb30106ec3251cf3baf34174c(property_id, limit=limit, offset=offset, filters=filters)
        print("The response of HousekeepingApi->call_27abd48cb30106ec3251cf3baf34174c:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HousekeepingApi->call_27abd48cb30106ec3251cf3baf34174c: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**| The property ID | 
 **limit** | **int**| The maximum number of items to return in the response. Default is 100. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. Used for pagination. | [optional] [default to 0]
 **filters** | [**QueryParameterDynamicFilterSchema**](.md)| This parameter should be formatted as a list of strings separated by ; | [optional] 

### Return type

[**InspectionListResponseSchema**](InspectionListResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paged array of inspections |  -  |
**400** | Bad Request response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

