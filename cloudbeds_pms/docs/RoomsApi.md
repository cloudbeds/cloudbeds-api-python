# cloudbeds_pms.RoomsApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**out_of_service_controller_make**](RoomsApi.md#out_of_service_controller_make) | **POST** /rooms/v1/out-of-service | Room out of service


# **out_of_service_controller_make**
> OutOfServiceResponseSchema out_of_service_controller_make(place_rooms_out_of_service_request)

Room out of service

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.out_of_service_response_schema import OutOfServiceResponseSchema
from cloudbeds_pms.models.place_rooms_out_of_service_request import PlaceRoomsOutOfServiceRequest
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
    api_instance = cloudbeds_pms.RoomsApi(api_client)
    place_rooms_out_of_service_request = cloudbeds_pms.PlaceRoomsOutOfServiceRequest() # PlaceRoomsOutOfServiceRequest | Out of service request body.

    try:
        # Room out of service
        api_response = api_instance.out_of_service_controller_make(place_rooms_out_of_service_request)
        print("The response of RoomsApi->out_of_service_controller_make:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->out_of_service_controller_make: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_rooms_out_of_service_request** | [**PlaceRoomsOutOfServiceRequest**](PlaceRoomsOutOfServiceRequest.md)| Out of service request body. | 

### Return type

[**OutOfServiceResponseSchema**](OutOfServiceResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Rooms were placed out of service successfully |  -  |
**400** | At least one of the rooms could not be placed out of service |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

