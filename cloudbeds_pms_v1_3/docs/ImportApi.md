# cloudbeds_pms_v1_3.ImportApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_dummy_reservations_get**](ImportApi.md#import_dummy_reservations_get) | **GET** /import/dummyReservations | GetImportDummyReservations
[**import_tours_get**](ImportApi.md#import_tours_get) | **GET** /import/tours | GetImportTours


# **import_dummy_reservations_get**
> GetImportDummyReservationsResponse import_dummy_reservations_get()

GetImportDummyReservations



### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_import_dummy_reservations_response import GetImportDummyReservationsResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
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
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.ImportApi(api_client)

    try:
        # GetImportDummyReservations
        api_response = api_instance.import_dummy_reservations_get()
        print("The response of ImportApi->import_dummy_reservations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_dummy_reservations_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetImportDummyReservationsResponse**](GetImportDummyReservationsResponse.md)

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

# **import_tours_get**
> GetImportToursResponse import_tours_get()

GetImportTours



### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_import_tours_response import GetImportToursResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
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
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.ImportApi(api_client)

    try:
        # GetImportTours
        api_response = api_instance.import_tours_get()
        print("The response of ImportApi->import_tours_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_tours_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetImportToursResponse**](GetImportToursResponse.md)

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

