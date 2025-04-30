# cloudbeds_pms_v1_3.RoomsApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hotel_room_types_get**](RoomsApi.md#get_hotel_room_types_get) | **GET** /getHotelRoomTypes | getHotelRoomTypes


# **get_hotel_room_types_get**
> GetHotelRoomTypesResponse get_hotel_room_types_get(property_ids, start_date=start_date, end_date=end_date, adults=adults, children=children, detailed_rates=detailed_rates, page_number=page_number, page_size=page_size)

getHotelRoomTypes

Returns a list of room types of a specific property, or a list of properties

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_hotel_room_types_response import GetHotelRoomTypesResponse
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
    api_instance = cloudbeds_pms_v1_3.RoomsApi(api_client)
    property_ids = 'property_ids_example' # str | Property ID list, comma-separated, i.e. 37,345,89
    start_date = '2013-10-20' # date | Check-In date. Required for rates to be returned. (optional)
    end_date = '2013-10-20' # date | Check-Out date. Required for rates to be returned. (optional)
    adults = 56 # int | Number of adults. Required for rates to be returned. (optional)
    children = 56 # int | Number of children. Required for rates to be returned. (optional)
    detailed_rates = False # bool | If detailed rates are expected (optional) (default to False)
    page_number = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Page size (optional) (default to 20)

    try:
        # getHotelRoomTypes
        api_response = api_instance.get_hotel_room_types_get(property_ids, start_date=start_date, end_date=end_date, adults=adults, children=children, detailed_rates=detailed_rates, page_number=page_number, page_size=page_size)
        print("The response of RoomsApi->get_hotel_room_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->get_hotel_room_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_ids** | **str**| Property ID list, comma-separated, i.e. 37,345,89 | 
 **start_date** | **date**| Check-In date. Required for rates to be returned. | [optional] 
 **end_date** | **date**| Check-Out date. Required for rates to be returned. | [optional] 
 **adults** | **int**| Number of adults. Required for rates to be returned. | [optional] 
 **children** | **int**| Number of children. Required for rates to be returned. | [optional] 
 **detailed_rates** | **bool**| If detailed rates are expected | [optional] [default to False]
 **page_number** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Page size | [optional] [default to 20]

### Return type

[**GetHotelRoomTypesResponse**](GetHotelRoomTypesResponse.md)

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

