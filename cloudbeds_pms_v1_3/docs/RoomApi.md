# cloudbeds_pms_v1_3.RoomApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_room_block_delete**](RoomApi.md#delete_room_block_delete) | **DELETE** /deleteRoomBlock | deleteRoomBlock
[**get_available_room_types_get**](RoomApi.md#get_available_room_types_get) | **GET** /getAvailableRoomTypes | getAvailableRoomTypes
[**get_reservation_room_details_get**](RoomApi.md#get_reservation_room_details_get) | **GET** /getReservationRoomDetails | getReservationRoomDetails
[**get_room_blocks_get**](RoomApi.md#get_room_blocks_get) | **GET** /getRoomBlocks | getRoomBlocks
[**get_room_types_get**](RoomApi.md#get_room_types_get) | **GET** /getRoomTypes | getRoomTypes
[**get_rooms_fees_and_taxes_get**](RoomApi.md#get_rooms_fees_and_taxes_get) | **GET** /getRoomsFeesAndTaxes | getRoomsFeesAndTaxes
[**get_rooms_get**](RoomApi.md#get_rooms_get) | **GET** /getRooms | getRooms
[**get_rooms_unassigned_get**](RoomApi.md#get_rooms_unassigned_get) | **GET** /getRoomsUnassigned | getRoomsUnassigned
[**post_room_assign_post**](RoomApi.md#post_room_assign_post) | **POST** /postRoomAssign | postRoomAssign
[**post_room_block_post**](RoomApi.md#post_room_block_post) | **POST** /postRoomBlock | postRoomBlock
[**post_room_check_in_post**](RoomApi.md#post_room_check_in_post) | **POST** /postRoomCheckIn | postRoomCheckIn
[**post_room_check_out_post**](RoomApi.md#post_room_check_out_post) | **POST** /postRoomCheckOut | postRoomCheckOut
[**put_room_block_put**](RoomApi.md#put_room_block_put) | **PUT** /putRoomBlock | putRoomBlock


# **delete_room_block_delete**
> DeleteRoomBlockResponse delete_room_block_delete(room_block_id, property_id=property_id)

deleteRoomBlock

Deletes a room block

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.delete_room_block_response import DeleteRoomBlockResponse
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
    api_instance = cloudbeds_pms_v1_3.RoomApi(api_client)
    room_block_id = 'room_block_id_example' # str | Room block ID
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # deleteRoomBlock
        api_response = api_instance.delete_room_block_delete(room_block_id, property_id=property_id)
        print("The response of RoomApi->delete_room_block_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->delete_room_block_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_block_id** | **str**| Room block ID | 
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**DeleteRoomBlockResponse**](DeleteRoomBlockResponse.md)

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

# **get_available_room_types_get**
> GetAvailableRoomTypesResponse get_available_room_types_get(start_date, end_date, rooms, adults, children, property_ids=property_ids, promo_code=promo_code, detailed_rates=detailed_rates, sort=sort, order=order, min_rate=min_rate, max_rate=max_rate, page_number=page_number, page_size=page_size)

getAvailableRoomTypes

Returns a list of room types with availability considering the informed parameters ### Group account support

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_available_room_types_response import GetAvailableRoomTypesResponse
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
    api_instance = cloudbeds_pms_v1_3.RoomApi(api_client)
    start_date = '2013-10-20' # date | Check-In date.
    end_date = '2013-10-20' # date | Check-Out date.
    rooms = 1 # int | Number of rooms. (default to 1)
    adults = 1 # int | Number of adults. (default to 1)
    children = 56 # int | Number of children.
    property_ids = 'property_ids_example' # str | Property ID list, comma-separated, i.e. 37,345,89 (optional)
    promo_code = 'promo_code_example' # str | Promotional code (optional)
    detailed_rates = False # bool | If detailed rates are expected (optional) (default to False)
    sort = 'sort_example' # str | Sort parameter (optional)
    order = asc # str |  (optional) (default to asc)
    min_rate = 3.4 # float | Minimum daily rate. Used to filter results (optional)
    max_rate = 3.4 # float | Maximum daily rate. Used to filter results (optional)
    page_number = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Page size (optional) (default to 20)

    try:
        # getAvailableRoomTypes
        api_response = api_instance.get_available_room_types_get(start_date, end_date, rooms, adults, children, property_ids=property_ids, promo_code=promo_code, detailed_rates=detailed_rates, sort=sort, order=order, min_rate=min_rate, max_rate=max_rate, page_number=page_number, page_size=page_size)
        print("The response of RoomApi->get_available_room_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->get_available_room_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Check-In date. | 
 **end_date** | **date**| Check-Out date. | 
 **rooms** | **int**| Number of rooms. | [default to 1]
 **adults** | **int**| Number of adults. | [default to 1]
 **children** | **int**| Number of children. | 
 **property_ids** | **str**| Property ID list, comma-separated, i.e. 37,345,89 | [optional] 
 **promo_code** | **str**| Promotional code | [optional] 
 **detailed_rates** | **bool**| If detailed rates are expected | [optional] [default to False]
 **sort** | **str**| Sort parameter | [optional] 
 **order** | **str**|  | [optional] [default to asc]
 **min_rate** | **float**| Minimum daily rate. Used to filter results | [optional] 
 **max_rate** | **float**| Maximum daily rate. Used to filter results | [optional] 
 **page_number** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Page size | [optional] [default to 20]

### Return type

[**GetAvailableRoomTypesResponse**](GetAvailableRoomTypesResponse.md)

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

# **get_reservation_room_details_get**
> GetReservationRoomDetailsResponse get_reservation_room_details_get(sub_reservation_id, property_id=property_id)

getReservationRoomDetails

Returns information about particular room in reservation by its subReservationID

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_reservation_room_details_response import GetReservationRoomDetailsResponse
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
    api_instance = cloudbeds_pms_v1_3.RoomApi(api_client)
    sub_reservation_id = 'sub_reservation_id_example' # str | Sub Reservation ID of the specific assigned room
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # getReservationRoomDetails
        api_response = api_instance.get_reservation_room_details_get(sub_reservation_id, property_id=property_id)
        print("The response of RoomApi->get_reservation_room_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->get_reservation_room_details_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_reservation_id** | **str**| Sub Reservation ID of the specific assigned room | 
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**GetReservationRoomDetailsResponse**](GetReservationRoomDetailsResponse.md)

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

# **get_room_blocks_get**
> GetRoomBlocksResponse get_room_blocks_get(property_id=property_id, room_block_id=room_block_id, room_type_id=room_type_id, room_id=room_id, start_date=start_date, end_date=end_date, page_number=page_number, page_size=page_size)

getRoomBlocks

Returns a list of all room blocks considering the informed parameters.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_room_blocks_response import GetRoomBlocksResponse
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
    api_instance = cloudbeds_pms_v1_3.RoomApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    room_block_id = 'room_block_id_example' # str | Room block ID (optional)
    room_type_id = 'room_type_id_example' # str | Room type ID (optional)
    room_id = 'room_id_example' # str | Room ID (optional)
    start_date = '2013-10-20' # date | date\"] Start date - will filter for any room blocks that include this date (Date range must be one month or less) (optional)
    end_date = '2013-10-20' # date | date\"] End date - will filter for any room blocks that include this date (Date range must be one month or less) (optional)
    page_number = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Page size (optional) (default to 20)

    try:
        # getRoomBlocks
        api_response = api_instance.get_room_blocks_get(property_id=property_id, room_block_id=room_block_id, room_type_id=room_type_id, room_id=room_id, start_date=start_date, end_date=end_date, page_number=page_number, page_size=page_size)
        print("The response of RoomApi->get_room_blocks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->get_room_blocks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **room_block_id** | **str**| Room block ID | [optional] 
 **room_type_id** | **str**| Room type ID | [optional] 
 **room_id** | **str**| Room ID | [optional] 
 **start_date** | **date**| date\&quot;] Start date - will filter for any room blocks that include this date (Date range must be one month or less) | [optional] 
 **end_date** | **date**| date\&quot;] End date - will filter for any room blocks that include this date (Date range must be one month or less) | [optional] 
 **page_number** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Page size | [optional] [default to 20]

### Return type

[**GetRoomBlocksResponse**](GetRoomBlocksResponse.md)

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

# **get_room_types_get**
> GetRoomTypesResponse get_room_types_get(property_ids=property_ids, room_type_ids=room_type_ids, start_date=start_date, end_date=end_date, adults=adults, children=children, detailed_rates=detailed_rates, room_type_name=room_type_name, property_city=property_city, property_name=property_name, max_guests=max_guests, page_number=page_number, page_size=page_size, sort=sort)

getRoomTypes

Returns a list of room types filtered by the selected parameters ### Group account support

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_room_types_response import GetRoomTypesResponse
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
    api_instance = cloudbeds_pms_v1_3.RoomApi(api_client)
    property_ids = 'property_ids_example' # str | Property ID list, comma-separated, i.e. 37,345,89 (optional)
    room_type_ids = 'room_type_ids_example' # str | Room Type ID list, If more than one, send as comma-separated, i.e. 37,345,89 (optional)
    start_date = '2013-10-20' # date | Check-in date. Required for the rates to be returned. (optional)
    end_date = '2013-10-20' # date | Check-out date. Required for the rates to be returned. (optional)
    adults = 56 # int | Number of adults. Required for the rates to be returned. (optional)
    children = 56 # int | Number of children. Required for the rates to be returned. (optional)
    detailed_rates = False # bool | If detailed rates are expected (optional) (default to False)
    room_type_name = 'room_type_name_example' # str | Room type name, used to filter (optional)
    property_city = 'property_city_example' # str | Hotel city, used to filter (optional)
    property_name = 'property_name_example' # str | Hotel name, used to filter (optional)
    max_guests = 'max_guests_example' # str | Max number of guests, used to filter (optional)
    page_number = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Page size (optional) (default to 20)
    sort = 'sort_example' # str | Sorting rules, semicolon-separated. Format: `field[:direction]`, where `direction` is `asc` or `desc`, defaults to `asc` if not provided. Valid fields: `sorting_position`. Examples: - `sort=sorting_position` - `sort=sorting_position:desc` (optional)

    try:
        # getRoomTypes
        api_response = api_instance.get_room_types_get(property_ids=property_ids, room_type_ids=room_type_ids, start_date=start_date, end_date=end_date, adults=adults, children=children, detailed_rates=detailed_rates, room_type_name=room_type_name, property_city=property_city, property_name=property_name, max_guests=max_guests, page_number=page_number, page_size=page_size, sort=sort)
        print("The response of RoomApi->get_room_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->get_room_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_ids** | **str**| Property ID list, comma-separated, i.e. 37,345,89 | [optional] 
 **room_type_ids** | **str**| Room Type ID list, If more than one, send as comma-separated, i.e. 37,345,89 | [optional] 
 **start_date** | **date**| Check-in date. Required for the rates to be returned. | [optional] 
 **end_date** | **date**| Check-out date. Required for the rates to be returned. | [optional] 
 **adults** | **int**| Number of adults. Required for the rates to be returned. | [optional] 
 **children** | **int**| Number of children. Required for the rates to be returned. | [optional] 
 **detailed_rates** | **bool**| If detailed rates are expected | [optional] [default to False]
 **room_type_name** | **str**| Room type name, used to filter | [optional] 
 **property_city** | **str**| Hotel city, used to filter | [optional] 
 **property_name** | **str**| Hotel name, used to filter | [optional] 
 **max_guests** | **str**| Max number of guests, used to filter | [optional] 
 **page_number** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Page size | [optional] [default to 20]
 **sort** | **str**| Sorting rules, semicolon-separated. Format: &#x60;field[:direction]&#x60;, where &#x60;direction&#x60; is &#x60;asc&#x60; or &#x60;desc&#x60;, defaults to &#x60;asc&#x60; if not provided. Valid fields: &#x60;sorting_position&#x60;. Examples: - &#x60;sort&#x3D;sorting_position&#x60; - &#x60;sort&#x3D;sorting_position:desc&#x60; | [optional] 

### Return type

[**GetRoomTypesResponse**](GetRoomTypesResponse.md)

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

# **get_rooms_fees_and_taxes_get**
> GetRoomsFeesAndTaxesResponse get_rooms_fees_and_taxes_get(start_date, end_date, rooms_total, rooms_count, property_id=property_id)

getRoomsFeesAndTaxes

Get applicable fees and tax to a booking. This is meant to be used on checkout to display to the guest.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_rooms_fees_and_taxes_response import GetRoomsFeesAndTaxesResponse
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
    api_instance = cloudbeds_pms_v1_3.RoomApi(api_client)
    start_date = '2013-10-20' # date | Check-in date
    end_date = '2013-10-20' # date | Check-out date
    rooms_total = 3.4 # float | Total value of the rooms to be booked, with included taxes
    rooms_count = 56 # int | Number of rooms to be booked
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # getRoomsFeesAndTaxes
        api_response = api_instance.get_rooms_fees_and_taxes_get(start_date, end_date, rooms_total, rooms_count, property_id=property_id)
        print("The response of RoomApi->get_rooms_fees_and_taxes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->get_rooms_fees_and_taxes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Check-in date | 
 **end_date** | **date**| Check-out date | 
 **rooms_total** | **float**| Total value of the rooms to be booked, with included taxes | 
 **rooms_count** | **int**| Number of rooms to be booked | 
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**GetRoomsFeesAndTaxesResponse**](GetRoomsFeesAndTaxesResponse.md)

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

# **get_rooms_get**
> GetRoomsResponse get_rooms_get(property_ids=property_ids, room_type_id=room_type_id, room_type_name_short=room_type_name_short, start_date=start_date, end_date=end_date, include_room_relations=include_room_relations, page_number=page_number, page_size=page_size, sort=sort)

getRooms

Returns a list of all rooms considering the informed parameters. If Check-in/out dates are sent, only unassigned rooms are returned. ### Group account support

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_rooms_response import GetRoomsResponse
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
    api_instance = cloudbeds_pms_v1_3.RoomApi(api_client)
    property_ids = 'property_ids_example' # str | Property ID list, comma-separated, i.e. 37,345,89 (optional)
    room_type_id = 'room_type_id_example' # str | Room type ID, comma-separated, i.e. 37,345,89 (optional)
    room_type_name_short = 'room_type_name_short_example' # str | Room Type (short-version) (optional)
    start_date = '2013-10-20' # date | Initial stay date. If sent, only returns unassigned rooms in this period. If not sent, will return all rooms available in property. Necessary if endDate is sent. (optional)
    end_date = '2013-10-20' # date | Final stay date. Necessary if startDate is sent. (optional)
    include_room_relations = 0 # int | Determines whether room relations info should be included in the response (optional) (default to 0)
    page_number = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Page size (optional) (default to 20)
    sort = 'sort_example' # str | Sorting rules, semicolon-separated. Format: `field[:direction]`, where `direction` is `asc` or `desc`, defaults to `asc` if not provided. Valid fields: `room_position`, `sorting_position`. Examples: - `sort=room_position;sorting_position` - `sort=room_position:asc;sorting_position:desc` (optional)

    try:
        # getRooms
        api_response = api_instance.get_rooms_get(property_ids=property_ids, room_type_id=room_type_id, room_type_name_short=room_type_name_short, start_date=start_date, end_date=end_date, include_room_relations=include_room_relations, page_number=page_number, page_size=page_size, sort=sort)
        print("The response of RoomApi->get_rooms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->get_rooms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_ids** | **str**| Property ID list, comma-separated, i.e. 37,345,89 | [optional] 
 **room_type_id** | **str**| Room type ID, comma-separated, i.e. 37,345,89 | [optional] 
 **room_type_name_short** | **str**| Room Type (short-version) | [optional] 
 **start_date** | **date**| Initial stay date. If sent, only returns unassigned rooms in this period. If not sent, will return all rooms available in property. Necessary if endDate is sent. | [optional] 
 **end_date** | **date**| Final stay date. Necessary if startDate is sent. | [optional] 
 **include_room_relations** | **int**| Determines whether room relations info should be included in the response | [optional] [default to 0]
 **page_number** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Page size | [optional] [default to 20]
 **sort** | **str**| Sorting rules, semicolon-separated. Format: &#x60;field[:direction]&#x60;, where &#x60;direction&#x60; is &#x60;asc&#x60; or &#x60;desc&#x60;, defaults to &#x60;asc&#x60; if not provided. Valid fields: &#x60;room_position&#x60;, &#x60;sorting_position&#x60;. Examples: - &#x60;sort&#x3D;room_position;sorting_position&#x60; - &#x60;sort&#x3D;room_position:asc;sorting_position:desc&#x60; | [optional] 

### Return type

[**GetRoomsResponse**](GetRoomsResponse.md)

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

# **get_rooms_unassigned_get**
> GetRoomsUnassignedResponse get_rooms_unassigned_get(property_ids=property_ids)

getRoomsUnassigned

Returns a list of unassigned rooms in the property. Call is alias of [getRooms](#api-Room-getRooms). Please check its documentation for parameters, response and example. ### Group account support

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_rooms_unassigned_response import GetRoomsUnassignedResponse
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
    api_instance = cloudbeds_pms_v1_3.RoomApi(api_client)
    property_ids = 'property_ids_example' # str | List of property IDs, comma-separated, i.e. 37,345,89 (optional)

    try:
        # getRoomsUnassigned
        api_response = api_instance.get_rooms_unassigned_get(property_ids=property_ids)
        print("The response of RoomApi->get_rooms_unassigned_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->get_rooms_unassigned_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_ids** | **str**| List of property IDs, comma-separated, i.e. 37,345,89 | [optional] 

### Return type

[**GetRoomsUnassignedResponse**](GetRoomsUnassignedResponse.md)

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

# **post_room_assign_post**
> PostRoomAssignResponse post_room_assign_post(property_id=property_id, reservation_id=reservation_id, sub_reservation_id=sub_reservation_id, reservation_room_id=reservation_room_id, new_room_id=new_room_id, room_type_id=room_type_id, old_room_id=old_room_id, override_rates=override_rates, adjust_price=adjust_price)

postRoomAssign

Assign/Reassign a room on a guest reservation

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_room_assign_response import PostRoomAssignResponse
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
    api_instance = cloudbeds_pms_v1_3.RoomApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation identifier (optional)
    sub_reservation_id = 'sub_reservation_id_example' # str | Sub Reservation identifier (optional)
    reservation_room_id = 'reservation_room_id_example' # str | Reservation room ID. Must be set if you want to unassign a room. (optional)
    new_room_id = 'new_room_id_example' # str | Room ID of the room that will be assigned. Empty field must be sent if you want to unassign a room. (optional)
    room_type_id = 'room_type_id_example' # str | Room Type ID of the room that will be assigned. Need to be provided in case of assignment. (optional)
    old_room_id = 'old_room_id_example' # str | Room ID of the room that was assigned. Need to be provided in case of reassignment. (optional)
    override_rates = False # bool | Deprecated. Please use adjustPrice instead. Setting overrideRates=true will have the opposite of the effect that the name implies. It will cause the rates to NOT be overridden, but instead to be recalculated based on the new room assignment. (optional) (default to False)
    adjust_price = False # bool | If room assignment would result in an upcharge or discount, this parameter needs to be set to true to approve the charges. If not set, the rate will retain its original value. (optional) (default to False)

    try:
        # postRoomAssign
        api_response = api_instance.post_room_assign_post(property_id=property_id, reservation_id=reservation_id, sub_reservation_id=sub_reservation_id, reservation_room_id=reservation_room_id, new_room_id=new_room_id, room_type_id=room_type_id, old_room_id=old_room_id, override_rates=override_rates, adjust_price=adjust_price)
        print("The response of RoomApi->post_room_assign_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->post_room_assign_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation identifier | [optional] 
 **sub_reservation_id** | **str**| Sub Reservation identifier | [optional] 
 **reservation_room_id** | **str**| Reservation room ID. Must be set if you want to unassign a room. | [optional] 
 **new_room_id** | **str**| Room ID of the room that will be assigned. Empty field must be sent if you want to unassign a room. | [optional] 
 **room_type_id** | **str**| Room Type ID of the room that will be assigned. Need to be provided in case of assignment. | [optional] 
 **old_room_id** | **str**| Room ID of the room that was assigned. Need to be provided in case of reassignment. | [optional] 
 **override_rates** | **bool**| Deprecated. Please use adjustPrice instead. Setting overrideRates&#x3D;true will have the opposite of the effect that the name implies. It will cause the rates to NOT be overridden, but instead to be recalculated based on the new room assignment. | [optional] [default to False]
 **adjust_price** | **bool**| If room assignment would result in an upcharge or discount, this parameter needs to be set to true to approve the charges. If not set, the rate will retain its original value. | [optional] [default to False]

### Return type

[**PostRoomAssignResponse**](PostRoomAssignResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_room_block_post**
> PostRoomBlockResponse post_room_block_post(property_id=property_id, room_block_type=room_block_type, room_block_reason=room_block_reason, start_date=start_date, end_date=end_date, rooms=rooms, first_name=first_name, last_name=last_name, length_of_hold_in_hours=length_of_hold_in_hours, email=email, phone=phone)

postRoomBlock

Adds a room block to the selected property.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_room_block_request_rooms_inner import PostRoomBlockRequestRoomsInner
from cloudbeds_pms_v1_3.models.post_room_block_response import PostRoomBlockResponse
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
    api_instance = cloudbeds_pms_v1_3.RoomApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    room_block_type = 'room_block_type_example' # str | Room block type. ‘blocked’ - Room block. ‘out_of_service’ - Out of service block. 'courtesy_hold' - Courtesy hold block. (optional)
    room_block_reason = 'room_block_reason_example' # str | Room block reason (optional)
    start_date = '2013-10-20' # date | Room block start date (optional)
    end_date = '2013-10-20' # date | Room block end date (optional)
    rooms = [cloudbeds_pms_v1_3.PostRoomBlockRequestRoomsInner()] # List[PostRoomBlockRequestRoomsInner] | All rooms for room block. When multiple rooms are submitted they will be created under the same roomBlockID. (optional)
    first_name = 'first_name_example' # str | First name - for courtesy hold updates (optional)
    last_name = 'last_name_example' # str | Last name - for courtesy hold updates (optional)
    length_of_hold_in_hours = 56 # int | Length of hold in hours - for courtesy hold updates (optional)
    email = 'email_example' # str | Email address - for courtesy hold updates (optional)
    phone = 'phone_example' # str | Phone number - for courtesy hold updates (optional)

    try:
        # postRoomBlock
        api_response = api_instance.post_room_block_post(property_id=property_id, room_block_type=room_block_type, room_block_reason=room_block_reason, start_date=start_date, end_date=end_date, rooms=rooms, first_name=first_name, last_name=last_name, length_of_hold_in_hours=length_of_hold_in_hours, email=email, phone=phone)
        print("The response of RoomApi->post_room_block_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->post_room_block_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **room_block_type** | **str**| Room block type. ‘blocked’ - Room block. ‘out_of_service’ - Out of service block. &#39;courtesy_hold&#39; - Courtesy hold block. | [optional] 
 **room_block_reason** | **str**| Room block reason | [optional] 
 **start_date** | **date**| Room block start date | [optional] 
 **end_date** | **date**| Room block end date | [optional] 
 **rooms** | [**List[PostRoomBlockRequestRoomsInner]**](PostRoomBlockRequestRoomsInner.md)| All rooms for room block. When multiple rooms are submitted they will be created under the same roomBlockID. | [optional] 
 **first_name** | **str**| First name - for courtesy hold updates | [optional] 
 **last_name** | **str**| Last name - for courtesy hold updates | [optional] 
 **length_of_hold_in_hours** | **int**| Length of hold in hours - for courtesy hold updates | [optional] 
 **email** | **str**| Email address - for courtesy hold updates | [optional] 
 **phone** | **str**| Phone number - for courtesy hold updates | [optional] 

### Return type

[**PostRoomBlockResponse**](PostRoomBlockResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_room_check_in_post**
> PostRoomCheckInResponse post_room_check_in_post(property_id=property_id, reservation_id=reservation_id, sub_reservation_id=sub_reservation_id, room_id=room_id)

postRoomCheckIn

Check-in a room already assigned for a guest

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_room_check_in_response import PostRoomCheckInResponse
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
    api_instance = cloudbeds_pms_v1_3.RoomApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation identifier (optional)
    sub_reservation_id = 'sub_reservation_id_example' # str | Sub Reservation identifier, allows for granular control over what room is being checked-in. If sent, roomID is ignored. (optional)
    room_id = 'room_id_example' # str | Room ID of the room that will be checked-in. (optional)

    try:
        # postRoomCheckIn
        api_response = api_instance.post_room_check_in_post(property_id=property_id, reservation_id=reservation_id, sub_reservation_id=sub_reservation_id, room_id=room_id)
        print("The response of RoomApi->post_room_check_in_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->post_room_check_in_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation identifier | [optional] 
 **sub_reservation_id** | **str**| Sub Reservation identifier, allows for granular control over what room is being checked-in. If sent, roomID is ignored. | [optional] 
 **room_id** | **str**| Room ID of the room that will be checked-in. | [optional] 

### Return type

[**PostRoomCheckInResponse**](PostRoomCheckInResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_room_check_out_post**
> PostRoomCheckOutResponse post_room_check_out_post(property_id=property_id, reservation_id=reservation_id, sub_reservation_id=sub_reservation_id, room_id=room_id)

postRoomCheckOut

Check-out a room already assigned for a guest. If all rooms are checked out, the reservation status will update accordingly to "Checked Out" as well.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_room_check_out_response import PostRoomCheckOutResponse
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
    api_instance = cloudbeds_pms_v1_3.RoomApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation identifier (optional)
    sub_reservation_id = 'sub_reservation_id_example' # str | Sub Reservation identifier, allows for granular control over what room is being checked out. If sent, roomID is ignored. (optional)
    room_id = 'room_id_example' # str | Room ID of the room that will be checked out. (optional)

    try:
        # postRoomCheckOut
        api_response = api_instance.post_room_check_out_post(property_id=property_id, reservation_id=reservation_id, sub_reservation_id=sub_reservation_id, room_id=room_id)
        print("The response of RoomApi->post_room_check_out_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->post_room_check_out_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation identifier | [optional] 
 **sub_reservation_id** | **str**| Sub Reservation identifier, allows for granular control over what room is being checked out. If sent, roomID is ignored. | [optional] 
 **room_id** | **str**| Room ID of the room that will be checked out. | [optional] 

### Return type

[**PostRoomCheckOutResponse**](PostRoomCheckOutResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_room_block_put**
> PutRoomBlockResponse put_room_block_put(property_id=property_id, room_block_id=room_block_id, room_block_reason=room_block_reason, start_date=start_date, end_date=end_date, rooms=rooms, first_name=first_name, last_name=last_name, length_of_hold_in_hours=length_of_hold_in_hours, email=email, phone=phone)

putRoomBlock

Updates a room block.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.put_room_block_request_rooms_inner import PutRoomBlockRequestRoomsInner
from cloudbeds_pms_v1_3.models.put_room_block_response import PutRoomBlockResponse
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
    api_instance = cloudbeds_pms_v1_3.RoomApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    room_block_id = 'room_block_id_example' # str | Room block ID (optional)
    room_block_reason = 'room_block_reason_example' # str | Room block reason (optional)
    start_date = '2013-10-20' # date | Room block start date (optional)
    end_date = '2013-10-20' # date | Room block end date (optional)
    rooms = [cloudbeds_pms_v1_3.PutRoomBlockRequestRoomsInner()] # List[PutRoomBlockRequestRoomsInner] | All rooms for room block. When multiple rooms are submitted they will be created under the same roomBlockID. (optional)
    first_name = 'first_name_example' # str | First name - for courtesy hold updates (optional)
    last_name = 'last_name_example' # str | Last name - for courtesy hold updates (optional)
    length_of_hold_in_hours = 56 # int | Length of hold in hours - for courtesy hold updates (optional)
    email = 'email_example' # str | Email address - for courtesy hold updates (optional)
    phone = 'phone_example' # str | Phone number - for courtesy hold updates (optional)

    try:
        # putRoomBlock
        api_response = api_instance.put_room_block_put(property_id=property_id, room_block_id=room_block_id, room_block_reason=room_block_reason, start_date=start_date, end_date=end_date, rooms=rooms, first_name=first_name, last_name=last_name, length_of_hold_in_hours=length_of_hold_in_hours, email=email, phone=phone)
        print("The response of RoomApi->put_room_block_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->put_room_block_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **room_block_id** | **str**| Room block ID | [optional] 
 **room_block_reason** | **str**| Room block reason | [optional] 
 **start_date** | **date**| Room block start date | [optional] 
 **end_date** | **date**| Room block end date | [optional] 
 **rooms** | [**List[PutRoomBlockRequestRoomsInner]**](PutRoomBlockRequestRoomsInner.md)| All rooms for room block. When multiple rooms are submitted they will be created under the same roomBlockID. | [optional] 
 **first_name** | **str**| First name - for courtesy hold updates | [optional] 
 **last_name** | **str**| Last name - for courtesy hold updates | [optional] 
 **length_of_hold_in_hours** | **int**| Length of hold in hours - for courtesy hold updates | [optional] 
 **email** | **str**| Email address - for courtesy hold updates | [optional] 
 **phone** | **str**| Phone number - for courtesy hold updates | [optional] 

### Return type

[**PutRoomBlockResponse**](PutRoomBlockResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

