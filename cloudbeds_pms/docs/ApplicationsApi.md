# cloudbeds_pms.ApplicationsApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_client_controller_connected_api_clients**](ApplicationsApi.md#api_client_controller_connected_api_clients) | **GET** /integration/v1/connected-applications | Get all connected API clients for a property


# **api_client_controller_connected_api_clients**
> ApplicationListResponseSchema api_client_controller_connected_api_clients(x_property_id, scopes=scopes)

Get all connected API clients for a property

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.application_list_response_schema import ApplicationListResponseSchema
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
    api_instance = cloudbeds_pms.ApplicationsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    scopes = ['[\"read:reservation,write:appError\"]'] # List[str] | List of OAuth scopes to filter by. Only API clients that have all specified scopes will be returned. (optional)

    try:
        # Get all connected API clients for a property
        api_response = api_instance.api_client_controller_connected_api_clients(x_property_id, scopes=scopes)
        print("The response of ApplicationsApi->api_client_controller_connected_api_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->api_client_controller_connected_api_clients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **scopes** | [**List[str]**](str.md)| List of OAuth scopes to filter by. Only API clients that have all specified scopes will be returned. | [optional] 

### Return type

[**ApplicationListResponseSchema**](ApplicationListResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of connected API clients |  -  |
**400** | Bad request response |  -  |
**403** | Forbidden response |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

