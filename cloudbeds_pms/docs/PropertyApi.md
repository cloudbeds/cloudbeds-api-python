# cloudbeds_pms.PropertyApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_controller_get_system**](PropertyApi.md#system_controller_get_system) | **GET** /property/v1/system | Retrieves the property&#39;s system component versions


# **system_controller_get_system**
> SystemResponseSchema system_controller_get_system(x_property_id)

Retrieves the property's system component versions

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.system_response_schema import SystemResponseSchema
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
    api_instance = cloudbeds_pms.PropertyApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.

    try:
        # Retrieves the property's system component versions
        api_response = api_instance.system_controller_get_system(x_property_id)
        print("The response of PropertyApi->system_controller_get_system:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->system_controller_get_system: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 

### Return type

[**SystemResponseSchema**](SystemResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved property features |  -  |
**400** | Bad Request - Invalid input parameters or business rule violation |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**403** | Forbidden - Insufficient permissions |  -  |
**404** | Not Found - Property not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

