# cloudbeds_pms_v1_3.GuestApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_guest_note_delete**](GuestApi.md#delete_guest_note_delete) | **DELETE** /deleteGuestNote | deleteGuestNote
[**get_guest_get**](GuestApi.md#get_guest_get) | **GET** /getGuest | getGuest
[**get_guest_list_get**](GuestApi.md#get_guest_list_get) | **GET** /getGuestList | getGuestList
[**get_guest_notes_get**](GuestApi.md#get_guest_notes_get) | **GET** /getGuestNotes | getGuestNotes
[**get_guests_by_filter_get**](GuestApi.md#get_guests_by_filter_get) | **GET** /getGuestsByFilter | getGuestsByFilter
[**get_guests_by_status_get**](GuestApi.md#get_guests_by_status_get) | **GET** /getGuestsByStatus | getGuestsByStatus
[**get_guests_modified_get**](GuestApi.md#get_guests_modified_get) | **GET** /getGuestsModified | getGuestsModified
[**post_guest_credit_card_post**](GuestApi.md#post_guest_credit_card_post) | **POST** /postGuestCreditCard | postGuestCreditCard
[**post_guest_document_post**](GuestApi.md#post_guest_document_post) | **POST** /postGuestDocument | postGuestDocument
[**post_guest_note_post**](GuestApi.md#post_guest_note_post) | **POST** /postGuestNote | postGuestNote
[**post_guest_photo_post**](GuestApi.md#post_guest_photo_post) | **POST** /postGuestPhoto | postGuestPhoto
[**post_guest_post**](GuestApi.md#post_guest_post) | **POST** /postGuest | postGuest
[**post_guests_to_room_post**](GuestApi.md#post_guests_to_room_post) | **POST** /postGuestsToRoom | postGuestsToRoom
[**put_guest_note_put**](GuestApi.md#put_guest_note_put) | **PUT** /putGuestNote | putGuestNote
[**put_guest_put**](GuestApi.md#put_guest_put) | **PUT** /putGuest | putGuest


# **delete_guest_note_delete**
> DeleteGuestNoteResponse delete_guest_note_delete(guest_id, note_id, property_id=property_id)

deleteGuestNote

Archives an existing guest note.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.delete_guest_note_response import DeleteGuestNoteResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    guest_id = 'guest_id_example' # str | Guest ID
    note_id = 'note_id_example' # str | Note ID
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # deleteGuestNote
        api_response = api_instance.delete_guest_note_delete(guest_id, note_id, property_id=property_id)
        print("The response of GuestApi->delete_guest_note_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->delete_guest_note_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guest_id** | **str**| Guest ID | 
 **note_id** | **str**| Note ID | 
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**DeleteGuestNoteResponse**](DeleteGuestNoteResponse.md)

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

# **get_guest_get**
> GetGuestResponse get_guest_get(property_id=property_id, reservation_id=reservation_id, guest_id=guest_id, include_guest_requirements=include_guest_requirements)

getGuest

Returns information on a guest specified by the Reservation ID parameter

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_guest_response import GetGuestResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation Unique Identifier. Required if no guestID is provided. (optional)
    guest_id = 'guest_id_example' # str | Guest ID. Required if no reservationID is provided. (optional)
    include_guest_requirements = False # bool | Includes guest requirements data in the response (optional) (default to False)

    try:
        # getGuest
        api_response = api_instance.get_guest_get(property_id=property_id, reservation_id=reservation_id, guest_id=guest_id, include_guest_requirements=include_guest_requirements)
        print("The response of GuestApi->get_guest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->get_guest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation Unique Identifier. Required if no guestID is provided. | [optional] 
 **guest_id** | **str**| Guest ID. Required if no reservationID is provided. | [optional] 
 **include_guest_requirements** | **bool**| Includes guest requirements data in the response | [optional] [default to False]

### Return type

[**GetGuestResponse**](GetGuestResponse.md)

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

# **get_guest_list_get**
> GetGuestListResponse get_guest_list_get(property_ids=property_ids, results_from=results_from, results_to=results_to, check_in_from=check_in_from, check_in_to=check_in_to, check_out_from=check_out_from, check_out_to=check_out_to, guest_first_name=guest_first_name, guest_last_name=guest_last_name, guest_email=guest_email, guest_phone=guest_phone, guest_cell_phone=guest_cell_phone, status=status, sort_by=sort_by, include_guest_info=include_guest_info, exclude_secondary_guests=exclude_secondary_guests, include_guest_requirements=include_guest_requirements, page_number=page_number, page_size=page_size)

getGuestList

Returns a list of guests, ordered by modification date ### Group account support

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_guest_list_response import GetGuestListResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    property_ids = 'property_ids_example' # str | List of property IDs, comma-separated, i.e. 37,345,89 (optional)
    results_from = '2013-10-20T19:20:30+01:00' # datetime | Inferior limit datetime, used to filter guests result, based on latest creation/modification date (optional)
    results_to = '2013-10-20T19:20:30+01:00' # datetime | Superior limit datetime, used to filter guests result, based on latest creation/modification date (optional)
    check_in_from = '2013-10-20' # date | Filters guests result to return only guests with check-in date range starting on this date (optional)
    check_in_to = '2013-10-20' # date | Filters guests result to return only guests with check-in date range ending on this date (optional)
    check_out_from = '2013-10-20' # date | Filters guests result to return only guests with check-out date range starting on this date (optional)
    check_out_to = '2013-10-20' # date | Filters guests result to return only guests with check-out date range ending on this date (optional)
    guest_first_name = 'guest_first_name_example' # str | Filters guests result based on Guest First Name (optional)
    guest_last_name = 'guest_last_name_example' # str | Filters guests result based on Guest Last Name (optional)
    guest_email = 'guest_email_example' # str | Filters guests result based on Guest Email (optional)
    guest_phone = 'guest_phone_example' # str | Filters guests result based on Guest Phone Number (optional)
    guest_cell_phone = 'guest_cell_phone_example' # str | Filters guests result based on Guest Cell Phone Number (optional)
    status = 'status_example' # str | Reservation status <br /> If more than one, send as comma-separated values. i.e. in_progress,confirmed (optional)
    sort_by = modification # str | Sort By parameter (optional) (default to modification)
    include_guest_info = False # bool | If API response should return with more of Guest's information (optional) (default to False)
    exclude_secondary_guests = False # bool | If true, response only returns main guest's (optional) (default to False)
    include_guest_requirements = False # bool | Includes guest requirements data in the response (optional) (default to False)
    page_number = 1 # int | Results page number (optional) (default to 1)
    page_size = 100 # int | Results page size. Max = 100 (optional) (default to 100)

    try:
        # getGuestList
        api_response = api_instance.get_guest_list_get(property_ids=property_ids, results_from=results_from, results_to=results_to, check_in_from=check_in_from, check_in_to=check_in_to, check_out_from=check_out_from, check_out_to=check_out_to, guest_first_name=guest_first_name, guest_last_name=guest_last_name, guest_email=guest_email, guest_phone=guest_phone, guest_cell_phone=guest_cell_phone, status=status, sort_by=sort_by, include_guest_info=include_guest_info, exclude_secondary_guests=exclude_secondary_guests, include_guest_requirements=include_guest_requirements, page_number=page_number, page_size=page_size)
        print("The response of GuestApi->get_guest_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->get_guest_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_ids** | **str**| List of property IDs, comma-separated, i.e. 37,345,89 | [optional] 
 **results_from** | **datetime**| Inferior limit datetime, used to filter guests result, based on latest creation/modification date | [optional] 
 **results_to** | **datetime**| Superior limit datetime, used to filter guests result, based on latest creation/modification date | [optional] 
 **check_in_from** | **date**| Filters guests result to return only guests with check-in date range starting on this date | [optional] 
 **check_in_to** | **date**| Filters guests result to return only guests with check-in date range ending on this date | [optional] 
 **check_out_from** | **date**| Filters guests result to return only guests with check-out date range starting on this date | [optional] 
 **check_out_to** | **date**| Filters guests result to return only guests with check-out date range ending on this date | [optional] 
 **guest_first_name** | **str**| Filters guests result based on Guest First Name | [optional] 
 **guest_last_name** | **str**| Filters guests result based on Guest Last Name | [optional] 
 **guest_email** | **str**| Filters guests result based on Guest Email | [optional] 
 **guest_phone** | **str**| Filters guests result based on Guest Phone Number | [optional] 
 **guest_cell_phone** | **str**| Filters guests result based on Guest Cell Phone Number | [optional] 
 **status** | **str**| Reservation status &lt;br /&gt; If more than one, send as comma-separated values. i.e. in_progress,confirmed | [optional] 
 **sort_by** | **str**| Sort By parameter | [optional] [default to modification]
 **include_guest_info** | **bool**| If API response should return with more of Guest&#39;s information | [optional] [default to False]
 **exclude_secondary_guests** | **bool**| If true, response only returns main guest&#39;s | [optional] [default to False]
 **include_guest_requirements** | **bool**| Includes guest requirements data in the response | [optional] [default to False]
 **page_number** | **int**| Results page number | [optional] [default to 1]
 **page_size** | **int**| Results page size. Max &#x3D; 100 | [optional] [default to 100]

### Return type

[**GetGuestListResponse**](GetGuestListResponse.md)

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

# **get_guest_notes_get**
> GetGuestNotesResponse get_guest_notes_get(guest_id, property_id=property_id)

getGuestNotes

Retrieves a guest notes

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_guest_notes_response import GetGuestNotesResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    guest_id = 'guest_id_example' # str | Guest ID
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # getGuestNotes
        api_response = api_instance.get_guest_notes_get(guest_id, property_id=property_id)
        print("The response of GuestApi->get_guest_notes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->get_guest_notes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guest_id** | **str**| Guest ID | 
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**GetGuestNotesResponse**](GetGuestNotesResponse.md)

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

# **get_guests_by_filter_get**
> GetGuestsByFilterResponse get_guests_by_filter_get(status, property_ids=property_ids, reservation_id=reservation_id, room_id=room_id, guest_name=guest_name, check_in_from=check_in_from, check_in_to=check_in_to, check_out_from=check_out_from, check_out_to=check_out_to)

getGuestsByFilter

Returns a list of guests matching the selected parameters ### Group account support

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_guests_by_filter_response import GetGuestsByFilterResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    status = 'status_example' # str | Current guest status
    property_ids = 'property_ids_example' # str | List of property IDs, comma-separated, i.e. 37,345,89 (optional)
    reservation_id = 'reservation_id_example' # str |  (optional)
    room_id = 'room_id_example' # str |  (optional)
    guest_name = 'guest_name_example' # str |  (optional)
    check_in_from = '2013-10-20' # date | Filters guests result to return only guests with check-in date range starting on this date (optional)
    check_in_to = '2013-10-20' # date | Filters guests result to return only guests with check-in date range ending on this date (optional)
    check_out_from = '2013-10-20' # date | Filters guests result to return only guests with check-out date range starting on this date (optional)
    check_out_to = '2013-10-20' # date | Filters guests result to return only guests with check-out date range ending on this date (optional)

    try:
        # getGuestsByFilter
        api_response = api_instance.get_guests_by_filter_get(status, property_ids=property_ids, reservation_id=reservation_id, room_id=room_id, guest_name=guest_name, check_in_from=check_in_from, check_in_to=check_in_to, check_out_from=check_out_from, check_out_to=check_out_to)
        print("The response of GuestApi->get_guests_by_filter_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->get_guests_by_filter_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Current guest status | 
 **property_ids** | **str**| List of property IDs, comma-separated, i.e. 37,345,89 | [optional] 
 **reservation_id** | **str**|  | [optional] 
 **room_id** | **str**|  | [optional] 
 **guest_name** | **str**|  | [optional] 
 **check_in_from** | **date**| Filters guests result to return only guests with check-in date range starting on this date | [optional] 
 **check_in_to** | **date**| Filters guests result to return only guests with check-in date range ending on this date | [optional] 
 **check_out_from** | **date**| Filters guests result to return only guests with check-out date range starting on this date | [optional] 
 **check_out_to** | **date**| Filters guests result to return only guests with check-out date range ending on this date | [optional] 

### Return type

[**GetGuestsByFilterResponse**](GetGuestsByFilterResponse.md)

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

# **get_guests_by_status_get**
> GetGuestsByStatusResponse get_guests_by_status_get(status, property_id=property_id, results_from=results_from, results_to=results_to, page_number=page_number, page_size=page_size)

getGuestsByStatus

Returns a list of guests in the current status (Not Checked In, In House, Checked Out or Cancelled), sorted by modification date. If no date range is passed, it returns all guests with the selected status. ### Group account support

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_guests_by_status_response import GetGuestsByStatusResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    status = 'status_example' # str | Guest status during the period
    property_id = 'property_id_example' # str | ID for the properties to be queried (comma-separated, i.e. 37,345,89).<br /> It can be omitted if the API key is single-property, or to get results from all properties on an association. (optional)
    results_from = '2013-10-20T19:20:30+01:00' # datetime | Used to filter guests result, and returns only the guests that were last modified starting on \"resultsFrom\" value (optional)
    results_to = '2013-10-20T19:20:30+01:00' # datetime | Used to filter guests result, and returns only the guests that were last modified ending on \"resultsTo\" value (optional)
    page_number = 1 # int | Results page number (optional) (default to 1)
    page_size = 20 # int | Results page size. Max = 100 (optional) (default to 20)

    try:
        # getGuestsByStatus
        api_response = api_instance.get_guests_by_status_get(status, property_id=property_id, results_from=results_from, results_to=results_to, page_number=page_number, page_size=page_size)
        print("The response of GuestApi->get_guests_by_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->get_guests_by_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Guest status during the period | 
 **property_id** | **str**| ID for the properties to be queried (comma-separated, i.e. 37,345,89).&lt;br /&gt; It can be omitted if the API key is single-property, or to get results from all properties on an association. | [optional] 
 **results_from** | **datetime**| Used to filter guests result, and returns only the guests that were last modified starting on \&quot;resultsFrom\&quot; value | [optional] 
 **results_to** | **datetime**| Used to filter guests result, and returns only the guests that were last modified ending on \&quot;resultsTo\&quot; value | [optional] 
 **page_number** | **int**| Results page number | [optional] [default to 1]
 **page_size** | **int**| Results page size. Max &#x3D; 100 | [optional] [default to 20]

### Return type

[**GetGuestsByStatusResponse**](GetGuestsByStatusResponse.md)

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

# **get_guests_modified_get**
> GetGuestsModifiedResponse get_guests_modified_get(property_ids=property_ids, in_house=in_house, results_from=results_from, results_to=results_to, check_in_from=check_in_from, check_in_to=check_in_to, check_out_from=check_out_from, check_out_to=check_out_to, include_guest_requirements=include_guest_requirements, page_number=page_number, page_size=page_size)

getGuestsModified

Returns a list of guests based on their modification date. Note that when a guest checks in or checks out of a room, their record is modified at that time. If no date range is passed, only the records for the current day are returned. Also note that if the guest is assigned to multiple rooms, it will result in multiple records. ### Group account support

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_guests_modified_response import GetGuestsModifiedResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    property_ids = 'property_ids_example' # str | List of property IDs, comma-separated, i.e. 37,345,89 (optional)
    in_house = False # bool | When used, and true, will return guests only currently in-house. If the guest checks-out, it will not appear on the results. (optional) (default to False)
    results_from = '2013-10-20T19:20:30+01:00' # datetime | Inferior limit datetime, used to filter guests result, based on latest creation/modification date (optional)
    results_to = '2013-10-20T19:20:30+01:00' # datetime | Superior limit datetime, used to filter guests result, based on latest creation/modification date (optional)
    check_in_from = '2013-10-20' # date | Filters guests result to return only guests with check-in date range starting on this date (optional)
    check_in_to = '2013-10-20' # date | Filters guests result to return only guests with check-in date range ending on this date (optional)
    check_out_from = '2013-10-20' # date | Filters guests result to return only guests with check-out date range starting on this date (optional)
    check_out_to = '2013-10-20' # date | Filters guests result to return only guests with check-out date range ending on this date (optional)
    include_guest_requirements = False # bool | Includes guest requirements data in the response (optional) (default to False)
    page_number = 1 # int | Results page number (optional) (default to 1)
    page_size = 100 # int | Results page size. Max = 100 (optional) (default to 100)

    try:
        # getGuestsModified
        api_response = api_instance.get_guests_modified_get(property_ids=property_ids, in_house=in_house, results_from=results_from, results_to=results_to, check_in_from=check_in_from, check_in_to=check_in_to, check_out_from=check_out_from, check_out_to=check_out_to, include_guest_requirements=include_guest_requirements, page_number=page_number, page_size=page_size)
        print("The response of GuestApi->get_guests_modified_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->get_guests_modified_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_ids** | **str**| List of property IDs, comma-separated, i.e. 37,345,89 | [optional] 
 **in_house** | **bool**| When used, and true, will return guests only currently in-house. If the guest checks-out, it will not appear on the results. | [optional] [default to False]
 **results_from** | **datetime**| Inferior limit datetime, used to filter guests result, based on latest creation/modification date | [optional] 
 **results_to** | **datetime**| Superior limit datetime, used to filter guests result, based on latest creation/modification date | [optional] 
 **check_in_from** | **date**| Filters guests result to return only guests with check-in date range starting on this date | [optional] 
 **check_in_to** | **date**| Filters guests result to return only guests with check-in date range ending on this date | [optional] 
 **check_out_from** | **date**| Filters guests result to return only guests with check-out date range starting on this date | [optional] 
 **check_out_to** | **date**| Filters guests result to return only guests with check-out date range ending on this date | [optional] 
 **include_guest_requirements** | **bool**| Includes guest requirements data in the response | [optional] [default to False]
 **page_number** | **int**| Results page number | [optional] [default to 1]
 **page_size** | **int**| Results page size. Max &#x3D; 100 | [optional] [default to 100]

### Return type

[**GetGuestsModifiedResponse**](GetGuestsModifiedResponse.md)

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

# **post_guest_credit_card_post**
> PostGuestCreditCardResponse post_guest_credit_card_post(reservation_id=reservation_id, card_name=card_name, card_number=card_number, card_expiry_month=card_expiry_month, card_expiry_year=card_expiry_year, card_cvv=card_cvv, validate=validate)

postGuestCreditCard

Add a new credit card to guest file

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_guest_credit_card_response import PostGuestCreditCardResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    reservation_id = 'reservation_id_example' # str | Reservation Unique Identifier (optional)
    card_name = 'card_name_example' # str | Cardholder Name, as written in card (optional)
    card_number = 'card_number_example' # str | Credit Card number (optional)
    card_expiry_month = 56 # int | Credit Card expiration month (optional)
    card_expiry_year = 56 # int | Credit Card expiration year (2 or 4 digits) (optional)
    card_cvv = 'card_cvv_example' # str | Credit Card CVV code (optional)
    validate = True # bool | should the card be validated? If true, the card will be validated against the payment gateway. (optional)

    try:
        # postGuestCreditCard
        api_response = api_instance.post_guest_credit_card_post(reservation_id=reservation_id, card_name=card_name, card_number=card_number, card_expiry_month=card_expiry_month, card_expiry_year=card_expiry_year, card_cvv=card_cvv, validate=validate)
        print("The response of GuestApi->post_guest_credit_card_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->post_guest_credit_card_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**| Reservation Unique Identifier | [optional] 
 **card_name** | **str**| Cardholder Name, as written in card | [optional] 
 **card_number** | **str**| Credit Card number | [optional] 
 **card_expiry_month** | **int**| Credit Card expiration month | [optional] 
 **card_expiry_year** | **int**| Credit Card expiration year (2 or 4 digits) | [optional] 
 **card_cvv** | **str**| Credit Card CVV code | [optional] 
 **validate** | **bool**| should the card be validated? If true, the card will be validated against the payment gateway. | [optional] 

### Return type

[**PostGuestCreditCardResponse**](PostGuestCreditCardResponse.md)

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

# **post_guest_document_post**
> PostGuestDocumentResponse post_guest_document_post(property_id=property_id, guest_id=guest_id, file=file)

postGuestDocument

Attaches a document to a guest

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_guest_document_response import PostGuestDocumentResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    guest_id = 'guest_id_example' # str | Guest Unique Identifier (optional)
    file = None # bytearray | Form-based File Upload<br/> Allowed file types: <code>*.pdf, *.rtf, *.doc, *.docx, *.txt, *.jpg, *.jpeg, *.png, *.gif, *.csv, *.xls, *.xlsx, *.xml</code><br/> Allowed max file size: 100MB (optional)

    try:
        # postGuestDocument
        api_response = api_instance.post_guest_document_post(property_id=property_id, guest_id=guest_id, file=file)
        print("The response of GuestApi->post_guest_document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->post_guest_document_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **guest_id** | **str**| Guest Unique Identifier | [optional] 
 **file** | **bytearray**| Form-based File Upload&lt;br/&gt; Allowed file types: &lt;code&gt;*.pdf, *.rtf, *.doc, *.docx, *.txt, *.jpg, *.jpeg, *.png, *.gif, *.csv, *.xls, *.xlsx, *.xml&lt;/code&gt;&lt;br/&gt; Allowed max file size: 100MB | [optional] 

### Return type

[**PostGuestDocumentResponse**](PostGuestDocumentResponse.md)

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

# **post_guest_note_post**
> PostGuestNoteResponse post_guest_note_post(property_id=property_id, guest_id=guest_id, guest_note=guest_note, user_id=user_id)

postGuestNote

Adds a guest note

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_guest_note_response import PostGuestNoteResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    guest_id = 'guest_id_example' # str | Guest ID (optional)
    guest_note = 'guest_note_example' # str | Note to be added to guest profile. It's strictly forbidden to send unencrypted payment data through the API. Numeric values longer than 12 characters and considered valid by Luhn's algorithm will be rejected. (optional)
    user_id = 'user_id_example' # str | User ID Identify the actual user that is posting the note (optional)

    try:
        # postGuestNote
        api_response = api_instance.post_guest_note_post(property_id=property_id, guest_id=guest_id, guest_note=guest_note, user_id=user_id)
        print("The response of GuestApi->post_guest_note_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->post_guest_note_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **guest_id** | **str**| Guest ID | [optional] 
 **guest_note** | **str**| Note to be added to guest profile. It&#39;s strictly forbidden to send unencrypted payment data through the API. Numeric values longer than 12 characters and considered valid by Luhn&#39;s algorithm will be rejected. | [optional] 
 **user_id** | **str**| User ID Identify the actual user that is posting the note | [optional] 

### Return type

[**PostGuestNoteResponse**](PostGuestNoteResponse.md)

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

# **post_guest_photo_post**
> PostGuestPhotoResponse post_guest_photo_post(guest_id=guest_id, file=file)

postGuestPhoto

Attaches a photo to a guest

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_guest_photo_response import PostGuestPhotoResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    guest_id = 'guest_id_example' # str | Guest Unique Identifier (optional)
    file = None # bytearray | Form-based File Upload<br/> Allowed file types: <code>*.jpg, *.jpeg, *.png, *.gif</code><br/> Allowed max file size: 15MB (optional)

    try:
        # postGuestPhoto
        api_response = api_instance.post_guest_photo_post(guest_id=guest_id, file=file)
        print("The response of GuestApi->post_guest_photo_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->post_guest_photo_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guest_id** | **str**| Guest Unique Identifier | [optional] 
 **file** | **bytearray**| Form-based File Upload&lt;br/&gt; Allowed file types: &lt;code&gt;*.jpg, *.jpeg, *.png, *.gif&lt;/code&gt;&lt;br/&gt; Allowed max file size: 15MB | [optional] 

### Return type

[**PostGuestPhotoResponse**](PostGuestPhotoResponse.md)

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

# **post_guest_post**
> PostGuestResponse post_guest_post(property_id=property_id, reservation_id=reservation_id, guest_first_name=guest_first_name, guest_last_name=guest_last_name, guest_gender=guest_gender, guest_email=guest_email, guest_phone=guest_phone, guest_cell_phone=guest_cell_phone, guest_address1=guest_address1, guest_address2=guest_address2, guest_city=guest_city, guest_country=guest_country, guest_state=guest_state, guest_zip=guest_zip, guest_birth_date=guest_birth_date, guest_document_type=guest_document_type, guest_document_number=guest_document_number, guest_document_issue_date=guest_document_issue_date, guest_document_issuing_country=guest_document_issuing_country, guest_document_expiration_date=guest_document_expiration_date, guest_requirements=guest_requirements, custom_fields=custom_fields, guest_note=guest_note, reservation_note=reservation_note, guest_company_name=guest_company_name, guest_company_tax_id=guest_company_tax_id, guest_tax_id=guest_tax_id)

postGuest

Adds a guest to reservation as an additional guest.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_guest_request_custom_fields_inner import PostGuestRequestCustomFieldsInner
from cloudbeds_pms_v1_3.models.post_guest_response import PostGuestResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation ID (optional)
    guest_first_name = 'guest_first_name_example' # str |  (optional)
    guest_last_name = 'guest_last_name_example' # str |  (optional)
    guest_gender = 'guest_gender_example' # str |  (optional)
    guest_email = 'guest_email_example' # str |  (optional)
    guest_phone = 'guest_phone_example' # str |  (optional)
    guest_cell_phone = 'guest_cell_phone_example' # str |  (optional)
    guest_address1 = 'guest_address1_example' # str |  (optional)
    guest_address2 = 'guest_address2_example' # str |  (optional)
    guest_city = 'guest_city_example' # str |  (optional)
    guest_country = 'guest_country_example' # str | ISO-Code for Country (2 characters) (optional)
    guest_state = 'guest_state_example' # str |  (optional)
    guest_zip = 'guest_zip_example' # str |  (optional)
    guest_birth_date = '2013-10-20' # date |  (optional)
    guest_document_type = 'guest_document_type_example' # str | Document Type<br /> dni - Identity card<br /> nie - Residence permit<br /> na - non selection<br /> (optional)
    guest_document_number = 'guest_document_number_example' # str | (mandatory when guestDocumentType is sent) (optional)
    guest_document_issue_date = '2013-10-20' # date | (mandatory when guestDocumentType is sent and is not DNI) (optional)
    guest_document_issuing_country = 'guest_document_issuing_country_example' # str | Valid ISO-Code for Country (2 characters) (mandatory when guestDocumentType is sent) (optional)
    guest_document_expiration_date = '2013-10-20' # date | (mandatory when guestDocumentType is sent and is not DNI or NIE) (optional)
    guest_requirements = None # List[object] | Object with guest requirements information. (optional)
    custom_fields = [cloudbeds_pms_v1_3.PostGuestRequestCustomFieldsInner()] # List[PostGuestRequestCustomFieldsInner] | Only guest custom fields are allowed. (optional)
    guest_note = 'guest_note_example' # str | Note to be added to the Guest (optional)
    reservation_note = 'reservation_note_example' # str | Note to be added only to the Reservation. (optional)
    guest_company_name = 'guest_company_name_example' # str | Guest company name (optional)
    guest_company_tax_id = 'guest_company_tax_id_example' # str | Guest company tax ID (optional)
    guest_tax_id = 'guest_tax_id_example' # str | Guest tax ID (optional)

    try:
        # postGuest
        api_response = api_instance.post_guest_post(property_id=property_id, reservation_id=reservation_id, guest_first_name=guest_first_name, guest_last_name=guest_last_name, guest_gender=guest_gender, guest_email=guest_email, guest_phone=guest_phone, guest_cell_phone=guest_cell_phone, guest_address1=guest_address1, guest_address2=guest_address2, guest_city=guest_city, guest_country=guest_country, guest_state=guest_state, guest_zip=guest_zip, guest_birth_date=guest_birth_date, guest_document_type=guest_document_type, guest_document_number=guest_document_number, guest_document_issue_date=guest_document_issue_date, guest_document_issuing_country=guest_document_issuing_country, guest_document_expiration_date=guest_document_expiration_date, guest_requirements=guest_requirements, custom_fields=custom_fields, guest_note=guest_note, reservation_note=reservation_note, guest_company_name=guest_company_name, guest_company_tax_id=guest_company_tax_id, guest_tax_id=guest_tax_id)
        print("The response of GuestApi->post_guest_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->post_guest_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation ID | [optional] 
 **guest_first_name** | **str**|  | [optional] 
 **guest_last_name** | **str**|  | [optional] 
 **guest_gender** | **str**|  | [optional] 
 **guest_email** | **str**|  | [optional] 
 **guest_phone** | **str**|  | [optional] 
 **guest_cell_phone** | **str**|  | [optional] 
 **guest_address1** | **str**|  | [optional] 
 **guest_address2** | **str**|  | [optional] 
 **guest_city** | **str**|  | [optional] 
 **guest_country** | **str**| ISO-Code for Country (2 characters) | [optional] 
 **guest_state** | **str**|  | [optional] 
 **guest_zip** | **str**|  | [optional] 
 **guest_birth_date** | **date**|  | [optional] 
 **guest_document_type** | **str**| Document Type&lt;br /&gt; dni - Identity card&lt;br /&gt; nie - Residence permit&lt;br /&gt; na - non selection&lt;br /&gt; | [optional] 
 **guest_document_number** | **str**| (mandatory when guestDocumentType is sent) | [optional] 
 **guest_document_issue_date** | **date**| (mandatory when guestDocumentType is sent and is not DNI) | [optional] 
 **guest_document_issuing_country** | **str**| Valid ISO-Code for Country (2 characters) (mandatory when guestDocumentType is sent) | [optional] 
 **guest_document_expiration_date** | **date**| (mandatory when guestDocumentType is sent and is not DNI or NIE) | [optional] 
 **guest_requirements** | [**List[object]**](object.md)| Object with guest requirements information. | [optional] 
 **custom_fields** | [**List[PostGuestRequestCustomFieldsInner]**](PostGuestRequestCustomFieldsInner.md)| Only guest custom fields are allowed. | [optional] 
 **guest_note** | **str**| Note to be added to the Guest | [optional] 
 **reservation_note** | **str**| Note to be added only to the Reservation. | [optional] 
 **guest_company_name** | **str**| Guest company name | [optional] 
 **guest_company_tax_id** | **str**| Guest company tax ID | [optional] 
 **guest_tax_id** | **str**| Guest tax ID | [optional] 

### Return type

[**PostGuestResponse**](PostGuestResponse.md)

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

# **post_guests_to_room_post**
> PostGuestsToRoomResponse post_guests_to_room_post(property_id=property_id, reservation_id=reservation_id, room_id=room_id, guest_ids=guest_ids, remove_guest_ids=remove_guest_ids, remove_guest_ids_from_room=remove_guest_ids_from_room, remove_all=remove_all)

postGuestsToRoom

Assigns guest(s) to a room in a reservation and adds these guests as additional guests.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_guests_to_room_response import PostGuestsToRoomResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation ID (optional)
    room_id = 56 # int | Room ID already assigned to Reservation (optional)
    guest_ids = 'guest_ids_example' # str | Guest ID(s) to be assigned to room. If more than one, send as comma-separated, i.e. 37,345,89 (optional)
    remove_guest_ids = 'remove_guest_ids_example' # str | If sent, will remove guest ID(s) before adding guests sent in guestIDs parameter. If more than one, send as comma-separated, i.e. 37,345,89. Main Guest is never removed. (optional)
    remove_guest_ids_from_room = 'remove_guest_ids_from_room_example' # str | If sent, will remove guest ID(s) only from the specified Room ID(s). If more than one, send as comma-separated, i.e. 37,345,89. Incompatible with removeAll parameter. (optional)
    remove_all = True # bool | If set true, will remove all guests assigned to roomID before assigning guests sent in guestIDs parameter. Main Guest is never removed. (optional)

    try:
        # postGuestsToRoom
        api_response = api_instance.post_guests_to_room_post(property_id=property_id, reservation_id=reservation_id, room_id=room_id, guest_ids=guest_ids, remove_guest_ids=remove_guest_ids, remove_guest_ids_from_room=remove_guest_ids_from_room, remove_all=remove_all)
        print("The response of GuestApi->post_guests_to_room_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->post_guests_to_room_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation ID | [optional] 
 **room_id** | **int**| Room ID already assigned to Reservation | [optional] 
 **guest_ids** | **str**| Guest ID(s) to be assigned to room. If more than one, send as comma-separated, i.e. 37,345,89 | [optional] 
 **remove_guest_ids** | **str**| If sent, will remove guest ID(s) before adding guests sent in guestIDs parameter. If more than one, send as comma-separated, i.e. 37,345,89. Main Guest is never removed. | [optional] 
 **remove_guest_ids_from_room** | **str**| If sent, will remove guest ID(s) only from the specified Room ID(s). If more than one, send as comma-separated, i.e. 37,345,89. Incompatible with removeAll parameter. | [optional] 
 **remove_all** | **bool**| If set true, will remove all guests assigned to roomID before assigning guests sent in guestIDs parameter. Main Guest is never removed. | [optional] 

### Return type

[**PostGuestsToRoomResponse**](PostGuestsToRoomResponse.md)

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

# **put_guest_note_put**
> PutGuestNoteResponse put_guest_note_put(property_id=property_id, guest_id=guest_id, note_id=note_id, guest_note=guest_note)

putGuestNote

Updates an existing guest note.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.put_guest_note_response import PutGuestNoteResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    guest_id = 'guest_id_example' # str | Guest ID (optional)
    note_id = 'note_id_example' # str | Note ID (optional)
    guest_note = 'guest_note_example' # str | Note to be added to guest profile. It's strictly forbidden to send unencrypted payment data through the API. Numeric values longer than 12 characters and considered valid by Luhn's algorithm will be rejected. (optional)

    try:
        # putGuestNote
        api_response = api_instance.put_guest_note_put(property_id=property_id, guest_id=guest_id, note_id=note_id, guest_note=guest_note)
        print("The response of GuestApi->put_guest_note_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->put_guest_note_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **guest_id** | **str**| Guest ID | [optional] 
 **note_id** | **str**| Note ID | [optional] 
 **guest_note** | **str**| Note to be added to guest profile. It&#39;s strictly forbidden to send unencrypted payment data through the API. Numeric values longer than 12 characters and considered valid by Luhn&#39;s algorithm will be rejected. | [optional] 

### Return type

[**PutGuestNoteResponse**](PutGuestNoteResponse.md)

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

# **put_guest_put**
> PutGuestResponse put_guest_put(property_id=property_id, guest_id=guest_id, guest_first_name=guest_first_name, guest_last_name=guest_last_name, guest_gender=guest_gender, guest_email=guest_email, guest_phone=guest_phone, guest_cell_phone=guest_cell_phone, guest_address1=guest_address1, guest_address2=guest_address2, guest_city=guest_city, guest_country=guest_country, guest_state=guest_state, guest_zip=guest_zip, guest_birth_date=guest_birth_date, guest_document_type=guest_document_type, guest_document_number=guest_document_number, guest_document_issue_date=guest_document_issue_date, guest_document_issuing_country=guest_document_issuing_country, guest_document_expiration_date=guest_document_expiration_date, guest_requirements=guest_requirements, guest_custom_fields=guest_custom_fields, guest_company_name=guest_company_name, guest_company_tax_id=guest_company_tax_id, guest_tax_id=guest_tax_id)

putGuest

Updates an existing guest with information provided. At least one information field is required for this call.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.put_guest_request_guest_custom_fields_inner import PutGuestRequestGuestCustomFieldsInner
from cloudbeds_pms_v1_3.models.put_guest_response import PutGuestResponse
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
    api_instance = cloudbeds_pms_v1_3.GuestApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    guest_id = 'guest_id_example' # str | Valid Guest ID (optional)
    guest_first_name = 'guest_first_name_example' # str |  (optional)
    guest_last_name = 'guest_last_name_example' # str |  (optional)
    guest_gender = 'guest_gender_example' # str |  (optional)
    guest_email = 'guest_email_example' # str |  (optional)
    guest_phone = 'guest_phone_example' # str |  (optional)
    guest_cell_phone = 'guest_cell_phone_example' # str |  (optional)
    guest_address1 = 'guest_address1_example' # str |  (optional)
    guest_address2 = 'guest_address2_example' # str |  (optional)
    guest_city = 'guest_city_example' # str |  (optional)
    guest_country = 'guest_country_example' # str | ISO-Code for Country (2 characters) (optional)
    guest_state = 'guest_state_example' # str |  (optional)
    guest_zip = 'guest_zip_example' # str |  (optional)
    guest_birth_date = '2013-10-20' # date |  (optional)
    guest_document_type = 'guest_document_type_example' # str | It is mandatory to send all document information<br /> na - non selection<br /> dni - Identity card<br /> nie - Residence permit<br /> (optional)
    guest_document_number = 'guest_document_number_example' # str | (mandatory when guestDocumentType is sent) (optional)
    guest_document_issue_date = '2013-10-20' # date | (mandatory when guestDocumentType is sent and is not DNI) (optional)
    guest_document_issuing_country = 'guest_document_issuing_country_example' # str | ISO-Code for Country (2 characters) (mandatory when guestDocumentType is sent) (optional)
    guest_document_expiration_date = '2013-10-20' # date | (mandatory when guestDocumentType is sent and is not DNI or NIE) (optional)
    guest_requirements = None # List[object] | Object with guest requirements information. (optional)
    guest_custom_fields = [cloudbeds_pms_v1_3.PutGuestRequestGuestCustomFieldsInner()] # List[PutGuestRequestGuestCustomFieldsInner] |  (optional)
    guest_company_name = 'guest_company_name_example' # str | Guest company name (optional)
    guest_company_tax_id = 'guest_company_tax_id_example' # str | Guest company tax ID (optional)
    guest_tax_id = 'guest_tax_id_example' # str | Guest tax ID unencrypted payment data through the API. Numeric values longer than 12 characters and considered valid by Luhn's algorithm will be rejected. (optional)

    try:
        # putGuest
        api_response = api_instance.put_guest_put(property_id=property_id, guest_id=guest_id, guest_first_name=guest_first_name, guest_last_name=guest_last_name, guest_gender=guest_gender, guest_email=guest_email, guest_phone=guest_phone, guest_cell_phone=guest_cell_phone, guest_address1=guest_address1, guest_address2=guest_address2, guest_city=guest_city, guest_country=guest_country, guest_state=guest_state, guest_zip=guest_zip, guest_birth_date=guest_birth_date, guest_document_type=guest_document_type, guest_document_number=guest_document_number, guest_document_issue_date=guest_document_issue_date, guest_document_issuing_country=guest_document_issuing_country, guest_document_expiration_date=guest_document_expiration_date, guest_requirements=guest_requirements, guest_custom_fields=guest_custom_fields, guest_company_name=guest_company_name, guest_company_tax_id=guest_company_tax_id, guest_tax_id=guest_tax_id)
        print("The response of GuestApi->put_guest_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->put_guest_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **guest_id** | **str**| Valid Guest ID | [optional] 
 **guest_first_name** | **str**|  | [optional] 
 **guest_last_name** | **str**|  | [optional] 
 **guest_gender** | **str**|  | [optional] 
 **guest_email** | **str**|  | [optional] 
 **guest_phone** | **str**|  | [optional] 
 **guest_cell_phone** | **str**|  | [optional] 
 **guest_address1** | **str**|  | [optional] 
 **guest_address2** | **str**|  | [optional] 
 **guest_city** | **str**|  | [optional] 
 **guest_country** | **str**| ISO-Code for Country (2 characters) | [optional] 
 **guest_state** | **str**|  | [optional] 
 **guest_zip** | **str**|  | [optional] 
 **guest_birth_date** | **date**|  | [optional] 
 **guest_document_type** | **str**| It is mandatory to send all document information&lt;br /&gt; na - non selection&lt;br /&gt; dni - Identity card&lt;br /&gt; nie - Residence permit&lt;br /&gt; | [optional] 
 **guest_document_number** | **str**| (mandatory when guestDocumentType is sent) | [optional] 
 **guest_document_issue_date** | **date**| (mandatory when guestDocumentType is sent and is not DNI) | [optional] 
 **guest_document_issuing_country** | **str**| ISO-Code for Country (2 characters) (mandatory when guestDocumentType is sent) | [optional] 
 **guest_document_expiration_date** | **date**| (mandatory when guestDocumentType is sent and is not DNI or NIE) | [optional] 
 **guest_requirements** | [**List[object]**](object.md)| Object with guest requirements information. | [optional] 
 **guest_custom_fields** | [**List[PutGuestRequestGuestCustomFieldsInner]**](PutGuestRequestGuestCustomFieldsInner.md)|  | [optional] 
 **guest_company_name** | **str**| Guest company name | [optional] 
 **guest_company_tax_id** | **str**| Guest company tax ID | [optional] 
 **guest_tax_id** | **str**| Guest tax ID unencrypted payment data through the API. Numeric values longer than 12 characters and considered valid by Luhn&#39;s algorithm will be rejected. | [optional] 

### Return type

[**PutGuestResponse**](PutGuestResponse.md)

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

