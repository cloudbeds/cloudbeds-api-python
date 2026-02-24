# cloudbeds_pms_v1_3.ReservationApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_reservation_note_delete**](ReservationApi.md#delete_reservation_note_delete) | **DELETE** /deleteReservationNote | deleteReservationNote
[**get_reservation_assignments_get**](ReservationApi.md#get_reservation_assignments_get) | **GET** /getReservationAssignments | getReservationAssignments
[**get_reservation_get**](ReservationApi.md#get_reservation_get) | **GET** /getReservation | getReservation
[**get_reservation_notes_get**](ReservationApi.md#get_reservation_notes_get) | **GET** /getReservationNotes | getReservationNotes
[**get_reservations_get**](ReservationApi.md#get_reservations_get) | **GET** /getReservations | getReservations
[**get_reservations_with_rate_details_get**](ReservationApi.md#get_reservations_with_rate_details_get) | **GET** /getReservationsWithRateDetails | getReservationsWithRateDetails
[**get_sources_get**](ReservationApi.md#get_sources_get) | **GET** /getSources | getSources
[**post_reservation_document_post**](ReservationApi.md#post_reservation_document_post) | **POST** /postReservationDocument | postReservationDocument
[**post_reservation_note_post**](ReservationApi.md#post_reservation_note_post) | **POST** /postReservationNote | postReservationNote
[**post_reservation_post**](ReservationApi.md#post_reservation_post) | **POST** /postReservation | postReservation
[**put_reservation_note_put**](ReservationApi.md#put_reservation_note_put) | **PUT** /putReservationNote | putReservationNote
[**put_reservation_put**](ReservationApi.md#put_reservation_put) | **PUT** /putReservation | putReservation


# **delete_reservation_note_delete**
> DeleteReservationNoteResponse delete_reservation_note_delete(reservation_id, reservation_note_id, property_id=property_id)

deleteReservationNote

Archives an existing reservation note.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.delete_reservation_note_response import DeleteReservationNoteResponse
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
    api_instance = cloudbeds_pms_v1_3.ReservationApi(api_client)
    reservation_id = 'reservation_id_example' # str | Reservation Unique Identifier
    reservation_note_id = 'reservation_note_id_example' # str | Reservation Note ID
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # deleteReservationNote
        api_response = api_instance.delete_reservation_note_delete(reservation_id, reservation_note_id, property_id=property_id)
        print("The response of ReservationApi->delete_reservation_note_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->delete_reservation_note_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**| Reservation Unique Identifier | 
 **reservation_note_id** | **str**| Reservation Note ID | 
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**DeleteReservationNoteResponse**](DeleteReservationNoteResponse.md)

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

# **get_reservation_assignments_get**
> GetReservationAssignmentsResponse get_reservation_assignments_get(property_id=property_id, var_date=var_date)

getReservationAssignments

Returns a list of rooms/reservations assigned for a selected date.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_reservation_assignments_response import GetReservationAssignmentsResponse
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
    api_instance = cloudbeds_pms_v1_3.ReservationApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    var_date = '2013-10-20' # date | Date selected to get the assignments. If no date is passed, it will return the results for the current day. (optional)

    try:
        # getReservationAssignments
        api_response = api_instance.get_reservation_assignments_get(property_id=property_id, var_date=var_date)
        print("The response of ReservationApi->get_reservation_assignments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->get_reservation_assignments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **var_date** | **date**| Date selected to get the assignments. If no date is passed, it will return the results for the current day. | [optional] 

### Return type

[**GetReservationAssignmentsResponse**](GetReservationAssignmentsResponse.md)

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

# **get_reservation_get**
> GetReservationResponse get_reservation_get(reservation_id, property_id=property_id, include_guest_requirements=include_guest_requirements)

getReservation

Returns information on a booking specified by the reservationID parameter

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_reservation_response import GetReservationResponse
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
    api_instance = cloudbeds_pms_v1_3.ReservationApi(api_client)
    reservation_id = 'reservation_id_example' # str | Reservation Unique Identifier. Obtained from one of the \"Reservations\" group methods
    property_id = 'property_id_example' # str | Property ID (optional)
    include_guest_requirements = False # bool | Includes guest requirements data in the response. (optional) (default to False)

    try:
        # getReservation
        api_response = api_instance.get_reservation_get(reservation_id, property_id=property_id, include_guest_requirements=include_guest_requirements)
        print("The response of ReservationApi->get_reservation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->get_reservation_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**| Reservation Unique Identifier. Obtained from one of the \&quot;Reservations\&quot; group methods | 
 **property_id** | **str**| Property ID | [optional] 
 **include_guest_requirements** | **bool**| Includes guest requirements data in the response. | [optional] [default to False]

### Return type

[**GetReservationResponse**](GetReservationResponse.md)

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

# **get_reservation_notes_get**
> GetReservationNotesResponse get_reservation_notes_get(reservation_id, property_id=property_id)

getReservationNotes

Retrieves reservation notes based on parameters

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_reservation_notes_response import GetReservationNotesResponse
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
    api_instance = cloudbeds_pms_v1_3.ReservationApi(api_client)
    reservation_id = 'reservation_id_example' # str | Reservation Unique Identifier
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # getReservationNotes
        api_response = api_instance.get_reservation_notes_get(reservation_id, property_id=property_id)
        print("The response of ReservationApi->get_reservation_notes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->get_reservation_notes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**| Reservation Unique Identifier | 
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**GetReservationNotesResponse**](GetReservationNotesResponse.md)

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

# **get_reservations_get**
> GetReservationsResponse get_reservations_get(property_id=property_id, status=status, results_from=results_from, results_to=results_to, modified_from=modified_from, modified_to=modified_to, check_in_from=check_in_from, check_in_to=check_in_to, check_out_from=check_out_from, check_out_to=check_out_to, dates_query_mode=dates_query_mode, room_id=room_id, room_name=room_name, room_type_id=room_type_id, include_guests_details=include_guests_details, include_guest_requirements=include_guest_requirements, include_custom_fields=include_custom_fields, include_all_rooms=include_all_rooms, source_id=source_id, source_reservation_id=source_reservation_id, rate_plan_id=rate_plan_id, first_name=first_name, last_name=last_name, guest_id=guest_id, allotment_block_code=allotment_block_code, group_code=group_code, sort_by_recent=sort_by_recent, page_number=page_number, page_size=page_size)

getReservations

Returns a list of reservations that matched the filters criteria.<br /> Please note that some reservations modification may not be reflected in this timestamp. ### Group account support

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_reservations_response import GetReservationsResponse
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
    api_instance = cloudbeds_pms_v1_3.ReservationApi(api_client)
    property_id = 'property_id_example' # str | ID for the properties to be queried (comma-separated, i.e. 37,345,89).<br /> It can be omitted if the API key is single-property, or to get results from all properties on an association. (optional)
    status = 'status_example' # str | Filter by current reservation status (optional)
    results_from = '2013-10-20T19:20:30+01:00' # datetime | Inferior limit datetime, used to filter reservations, based on booking date (optional)
    results_to = '2013-10-20T19:20:30+01:00' # datetime | Superior limit datetime, used to filter reservations, based on booking date (optional)
    modified_from = '2013-10-20T19:20:30+01:00' # datetime | Inferior limit datetime, used to filter reservations, based on booking modification date (optional)
    modified_to = '2013-10-20T19:20:30+01:00' # datetime | Superior limit datetime, used to filter reservations, based on booking modification date (optional)
    check_in_from = '2013-10-20' # date | Filters reservations result to return only reservations with check-in date range starting on this date (optional)
    check_in_to = '2013-10-20' # date | Filters reservations result to return only reservations with check-in date range ending on this date (optional)
    check_out_from = '2013-10-20' # date | Filters reservations result to return only reservations with check-out date range starting on this date (optional)
    check_out_to = '2013-10-20' # date | Filters reservations result to return only reservations with check-out date range ending on this date (optional)
    dates_query_mode = booking # str | If we should consider the booking's check-in/check-out dates or the start and end dates for the associated rooms. (optional) (default to booking)
    room_id = 'room_id_example' # str | Filters reservation with the supplied room ID. CheckIn/checkOut dates OR status are required. If dates are provided and span more than one day, more than one reservation can be returned. If roomID supplied, roomName is ignored. (optional)
    room_name = 'room_name_example' # str | Filters reservation with the supplied room name (customizable by each property). CheckIn/checkOut dates OR status are required. If dates are provided and span more than one day, more than one reservation can be returned. (optional)
    room_type_id = 'room_type_id_example' # str | Filters reservation with the supplied Room Type ID. (optional)
    include_guests_details = False # bool | If guests details should be included or not (optional) (default to False)
    include_guest_requirements = False # bool | Includes guest requirements data in the response. Requires `includeGuestsDetails=true`. (optional) (default to False)
    include_custom_fields = False # bool | If reservation custom fields should be included or not (optional) (default to False)
    include_all_rooms = False # bool | When specified, the response will include an additional rooms field that combines both unassigned and assigned rooms. (optional) (default to False)
    source_id = 'source_id_example' # str | Filters reservation with the supplied source ID. (optional)
    source_reservation_id = 'source_reservation_id_example' # str | Filters reservation with the supplied reservation source ID. (optional)
    rate_plan_id = 'rate_plan_id_example' # str | Filters reservation with the supplied rate plan ID. (optional)
    first_name = 'first_name_example' # str | Filters reservation with the supplied primary guest first name. (optional)
    last_name = 'last_name_example' # str | Filters reservation with the supplied primary guest last name. (optional)
    guest_id = 'guest_id_example' # str | Filters reservation with the supplied Guest ID (Including additional guests). (optional)
    allotment_block_code = 'allotment_block_code_example' # str | Filters reservation with the supplied allotment block code. (optional)
    group_code = 'group_code_example' # str | Filters reservation with the supplied group code. (optional)
    sort_by_recent = True # bool | Sort response results by most recent action (optional)
    page_number = 1 # int | Results page number (optional) (default to 1)
    page_size = 100 # int | Results page size. Max = 100 (optional) (default to 100)

    try:
        # getReservations
        api_response = api_instance.get_reservations_get(property_id=property_id, status=status, results_from=results_from, results_to=results_to, modified_from=modified_from, modified_to=modified_to, check_in_from=check_in_from, check_in_to=check_in_to, check_out_from=check_out_from, check_out_to=check_out_to, dates_query_mode=dates_query_mode, room_id=room_id, room_name=room_name, room_type_id=room_type_id, include_guests_details=include_guests_details, include_guest_requirements=include_guest_requirements, include_custom_fields=include_custom_fields, include_all_rooms=include_all_rooms, source_id=source_id, source_reservation_id=source_reservation_id, rate_plan_id=rate_plan_id, first_name=first_name, last_name=last_name, guest_id=guest_id, allotment_block_code=allotment_block_code, group_code=group_code, sort_by_recent=sort_by_recent, page_number=page_number, page_size=page_size)
        print("The response of ReservationApi->get_reservations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->get_reservations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| ID for the properties to be queried (comma-separated, i.e. 37,345,89).&lt;br /&gt; It can be omitted if the API key is single-property, or to get results from all properties on an association. | [optional] 
 **status** | **str**| Filter by current reservation status | [optional] 
 **results_from** | **datetime**| Inferior limit datetime, used to filter reservations, based on booking date | [optional] 
 **results_to** | **datetime**| Superior limit datetime, used to filter reservations, based on booking date | [optional] 
 **modified_from** | **datetime**| Inferior limit datetime, used to filter reservations, based on booking modification date | [optional] 
 **modified_to** | **datetime**| Superior limit datetime, used to filter reservations, based on booking modification date | [optional] 
 **check_in_from** | **date**| Filters reservations result to return only reservations with check-in date range starting on this date | [optional] 
 **check_in_to** | **date**| Filters reservations result to return only reservations with check-in date range ending on this date | [optional] 
 **check_out_from** | **date**| Filters reservations result to return only reservations with check-out date range starting on this date | [optional] 
 **check_out_to** | **date**| Filters reservations result to return only reservations with check-out date range ending on this date | [optional] 
 **dates_query_mode** | **str**| If we should consider the booking&#39;s check-in/check-out dates or the start and end dates for the associated rooms. | [optional] [default to booking]
 **room_id** | **str**| Filters reservation with the supplied room ID. CheckIn/checkOut dates OR status are required. If dates are provided and span more than one day, more than one reservation can be returned. If roomID supplied, roomName is ignored. | [optional] 
 **room_name** | **str**| Filters reservation with the supplied room name (customizable by each property). CheckIn/checkOut dates OR status are required. If dates are provided and span more than one day, more than one reservation can be returned. | [optional] 
 **room_type_id** | **str**| Filters reservation with the supplied Room Type ID. | [optional] 
 **include_guests_details** | **bool**| If guests details should be included or not | [optional] [default to False]
 **include_guest_requirements** | **bool**| Includes guest requirements data in the response. Requires &#x60;includeGuestsDetails&#x3D;true&#x60;. | [optional] [default to False]
 **include_custom_fields** | **bool**| If reservation custom fields should be included or not | [optional] [default to False]
 **include_all_rooms** | **bool**| When specified, the response will include an additional rooms field that combines both unassigned and assigned rooms. | [optional] [default to False]
 **source_id** | **str**| Filters reservation with the supplied source ID. | [optional] 
 **source_reservation_id** | **str**| Filters reservation with the supplied reservation source ID. | [optional] 
 **rate_plan_id** | **str**| Filters reservation with the supplied rate plan ID. | [optional] 
 **first_name** | **str**| Filters reservation with the supplied primary guest first name. | [optional] 
 **last_name** | **str**| Filters reservation with the supplied primary guest last name. | [optional] 
 **guest_id** | **str**| Filters reservation with the supplied Guest ID (Including additional guests). | [optional] 
 **allotment_block_code** | **str**| Filters reservation with the supplied allotment block code. | [optional] 
 **group_code** | **str**| Filters reservation with the supplied group code. | [optional] 
 **sort_by_recent** | **bool**| Sort response results by most recent action | [optional] 
 **page_number** | **int**| Results page number | [optional] [default to 1]
 **page_size** | **int**| Results page size. Max &#x3D; 100 | [optional] [default to 100]

### Return type

[**GetReservationsResponse**](GetReservationsResponse.md)

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

# **get_reservations_with_rate_details_get**
> GetReservationsWithRateDetailsResponse get_reservations_with_rate_details_get(property_id=property_id, results_from=results_from, results_to=results_to, modified_from=modified_from, modified_to=modified_to, sort_by_recent=sort_by_recent, reservation_id=reservation_id, reservation_check_out_from=reservation_check_out_from, reservation_check_out_to=reservation_check_out_to, include_deleted=include_deleted, exclude_statuses=exclude_statuses, include_guests_details=include_guests_details, include_guest_requirements=include_guest_requirements, include_custom_fields=include_custom_fields, guest_id=guest_id, page_number=page_number, page_size=page_size)

getReservationsWithRateDetails

Returns a list of reservations with added information regarding booked rates and sources.<br /> Please note that some reservations modification may not be reflected in this timestamp.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_reservations_with_rate_details_response import GetReservationsWithRateDetailsResponse
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
    api_instance = cloudbeds_pms_v1_3.ReservationApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    results_from = '2013-10-20T19:20:30+01:00' # datetime | Inferior limit datetime, used to filter reservations, based on booking date (optional)
    results_to = '2013-10-20T19:20:30+01:00' # datetime | Superior limit datetime, used to filter reservations, based on booking date. If it is not set, will return the reservations up to current date (optional)
    modified_from = '2013-10-20T19:20:30+01:00' # datetime | Superior limit datetime, used to filter reservations, based on modification date. (optional)
    modified_to = '2013-10-20T19:20:30+01:00' # datetime | Superior limit datetime, used to filter reservations, based on modification date. (optional)
    sort_by_recent = True # bool | Sort response results by most recent action (optional)
    reservation_id = 'reservation_id_example' # str | Reservation identifiers, comma-separated, i.e. 37,345,89, used to return transactions limited to the selected reservations. (optional)
    reservation_check_out_from = '2013-10-20' # date | Superior limit datetime, used to filter reservations, based on reservation check-out date. (optional)
    reservation_check_out_to = '2013-10-20' # date | Superior limit datetime, used to filter reservations, based on reservation check-out date. (optional)
    include_deleted = False # bool | Include deleted reservations (optional) (default to False)
    exclude_statuses = 'exclude_statuses_example' # str | List of statuses (separated by comma) to be excluded from search (optional)
    include_guests_details = False # bool | If guests details should be included or not (optional) (default to False)
    include_guest_requirements = False # bool | Includes guest requirements data in the response. Requires `includeGuestsDetails=true`. (optional) (default to False)
    include_custom_fields = False # bool | If reservation custom fields should be included or not (optional) (default to False)
    guest_id = 'guest_id_example' # str | Filters reservations with the supplied Guest ID (Including additional guests). (optional)
    page_number = 1 # int | Results page number (optional) (default to 1)
    page_size = 100 # int | Results page size. Max = 100 (optional) (default to 100)

    try:
        # getReservationsWithRateDetails
        api_response = api_instance.get_reservations_with_rate_details_get(property_id=property_id, results_from=results_from, results_to=results_to, modified_from=modified_from, modified_to=modified_to, sort_by_recent=sort_by_recent, reservation_id=reservation_id, reservation_check_out_from=reservation_check_out_from, reservation_check_out_to=reservation_check_out_to, include_deleted=include_deleted, exclude_statuses=exclude_statuses, include_guests_details=include_guests_details, include_guest_requirements=include_guest_requirements, include_custom_fields=include_custom_fields, guest_id=guest_id, page_number=page_number, page_size=page_size)
        print("The response of ReservationApi->get_reservations_with_rate_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->get_reservations_with_rate_details_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **results_from** | **datetime**| Inferior limit datetime, used to filter reservations, based on booking date | [optional] 
 **results_to** | **datetime**| Superior limit datetime, used to filter reservations, based on booking date. If it is not set, will return the reservations up to current date | [optional] 
 **modified_from** | **datetime**| Superior limit datetime, used to filter reservations, based on modification date. | [optional] 
 **modified_to** | **datetime**| Superior limit datetime, used to filter reservations, based on modification date. | [optional] 
 **sort_by_recent** | **bool**| Sort response results by most recent action | [optional] 
 **reservation_id** | **str**| Reservation identifiers, comma-separated, i.e. 37,345,89, used to return transactions limited to the selected reservations. | [optional] 
 **reservation_check_out_from** | **date**| Superior limit datetime, used to filter reservations, based on reservation check-out date. | [optional] 
 **reservation_check_out_to** | **date**| Superior limit datetime, used to filter reservations, based on reservation check-out date. | [optional] 
 **include_deleted** | **bool**| Include deleted reservations | [optional] [default to False]
 **exclude_statuses** | **str**| List of statuses (separated by comma) to be excluded from search | [optional] 
 **include_guests_details** | **bool**| If guests details should be included or not | [optional] [default to False]
 **include_guest_requirements** | **bool**| Includes guest requirements data in the response. Requires &#x60;includeGuestsDetails&#x3D;true&#x60;. | [optional] [default to False]
 **include_custom_fields** | **bool**| If reservation custom fields should be included or not | [optional] [default to False]
 **guest_id** | **str**| Filters reservations with the supplied Guest ID (Including additional guests). | [optional] 
 **page_number** | **int**| Results page number | [optional] [default to 1]
 **page_size** | **int**| Results page size. Max &#x3D; 100 | [optional] [default to 100]

### Return type

[**GetReservationsWithRateDetailsResponse**](GetReservationsWithRateDetailsResponse.md)

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

# **get_sources_get**
> GetSourcesResponse get_sources_get(property_ids=property_ids)

getSources

Gets available property sources

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_sources_response import GetSourcesResponse
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
    api_instance = cloudbeds_pms_v1_3.ReservationApi(api_client)
    property_ids = 'property_ids_example' # str | ID for the properties to be queried (comma-separated, i.e. 37,345,89).<br /> (optional)

    try:
        # getSources
        api_response = api_instance.get_sources_get(property_ids=property_ids)
        print("The response of ReservationApi->get_sources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->get_sources_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_ids** | **str**| ID for the properties to be queried (comma-separated, i.e. 37,345,89).&lt;br /&gt; | [optional] 

### Return type

[**GetSourcesResponse**](GetSourcesResponse.md)

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

# **post_reservation_document_post**
> PostReservationDocumentResponse post_reservation_document_post(property_id=property_id, reservation_id=reservation_id, file=file)

postReservationDocument

Attaches a document to a reservation

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_reservation_document_response import PostReservationDocumentResponse
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
    api_instance = cloudbeds_pms_v1_3.ReservationApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation Unique Identifier (optional)
    file = None # bytearray | Form-based File Upload<br/> Allowed file types: <code>*.pdf, *.rtf, *.doc, *.docx, *.txt, *.jpg, *.jpeg, *.png, *.gif, *.csv, *.xls, *.xlsx, *.xml, *.json</code><br/> Allowed max file size: 100MB (optional)

    try:
        # postReservationDocument
        api_response = api_instance.post_reservation_document_post(property_id=property_id, reservation_id=reservation_id, file=file)
        print("The response of ReservationApi->post_reservation_document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->post_reservation_document_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation Unique Identifier | [optional] 
 **file** | **bytearray**| Form-based File Upload&lt;br/&gt; Allowed file types: &lt;code&gt;*.pdf, *.rtf, *.doc, *.docx, *.txt, *.jpg, *.jpeg, *.png, *.gif, *.csv, *.xls, *.xlsx, *.xml, *.json&lt;/code&gt;&lt;br/&gt; Allowed max file size: 100MB | [optional] 

### Return type

[**PostReservationDocumentResponse**](PostReservationDocumentResponse.md)

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

# **post_reservation_note_post**
> PostReservationNoteResponse post_reservation_note_post(property_id=property_id, reservation_id=reservation_id, reservation_note=reservation_note, user_id=user_id, date_created=date_created)

postReservationNote

Adds a reservation note

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_reservation_note_response import PostReservationNoteResponse
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
    api_instance = cloudbeds_pms_v1_3.ReservationApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation Unique Identifier (optional)
    reservation_note = 'reservation_note_example' # str | Note to be added to reservation (optional)
    user_id = 'user_id_example' # str | User ID Identify the actual user that is posting the note (optional)
    date_created = '2013-10-20T19:20:30+01:00' # datetime | Datetime the note was created. (optional)

    try:
        # postReservationNote
        api_response = api_instance.post_reservation_note_post(property_id=property_id, reservation_id=reservation_id, reservation_note=reservation_note, user_id=user_id, date_created=date_created)
        print("The response of ReservationApi->post_reservation_note_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->post_reservation_note_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation Unique Identifier | [optional] 
 **reservation_note** | **str**| Note to be added to reservation | [optional] 
 **user_id** | **str**| User ID Identify the actual user that is posting the note | [optional] 
 **date_created** | **datetime**| Datetime the note was created. | [optional] 

### Return type

[**PostReservationNoteResponse**](PostReservationNoteResponse.md)

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

# **post_reservation_post**
> PostReservationResponse post_reservation_post(property_id=property_id, source_id=source_id, third_party_identifier=third_party_identifier, start_date=start_date, end_date=end_date, guest_first_name=guest_first_name, guest_last_name=guest_last_name, guest_gender=guest_gender, guest_country=guest_country, guest_zip=guest_zip, guest_email=guest_email, guest_phone=guest_phone, guest_requirements=guest_requirements, estimated_arrival_time=estimated_arrival_time, rooms=rooms, adults=adults, children=children, payment_method=payment_method, card_token=card_token, payment_authorization_code=payment_authorization_code, custom_fields=custom_fields, promo_code=promo_code, allotment_block_code=allotment_block_code, group_code=group_code, date_created=date_created, send_email_confirmation=send_email_confirmation)

postReservation

Adds a reservation to the selected property

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_reservation_request_adults_inner import PostReservationRequestAdultsInner
from cloudbeds_pms_v1_3.models.post_reservation_request_children_inner import PostReservationRequestChildrenInner
from cloudbeds_pms_v1_3.models.post_reservation_request_custom_fields_inner import PostReservationRequestCustomFieldsInner
from cloudbeds_pms_v1_3.models.post_reservation_request_rooms_inner import PostReservationRequestRoomsInner
from cloudbeds_pms_v1_3.models.post_reservation_response import PostReservationResponse
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
    api_instance = cloudbeds_pms_v1_3.ReservationApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    source_id = 'source_id_example' # str | The third-party source ID for this reservation. (optional)
    third_party_identifier = 'third_party_identifier_example' # str | If it was received from a booking channel, this can be an identifier from that channel. (optional)
    start_date = '2013-10-20' # date | Check-In date. (optional)
    end_date = '2013-10-20' # date | Check-Out date. (optional)
    guest_first_name = 'guest_first_name_example' # str | First name of the guest (optional)
    guest_last_name = 'guest_last_name_example' # str | Last name of the guest (optional)
    guest_gender = 'guest_gender_example' # str |  (optional)
    guest_country = 'guest_country_example' # str | Valid ISO-Code for Country (2 characters) (optional)
    guest_zip = 'guest_zip_example' # str | ZIP Code (optional)
    guest_email = 'guest_email_example' # str | Guest email (optional)
    guest_phone = 'guest_phone_example' # str | Guest main phone number (optional)
    guest_requirements = None # List[object] | Object with guest requirements information. (optional)
    estimated_arrival_time = 'estimated_arrival_time_example' # str | Estimated Arrival Time, 24-hour format. (optional)
    rooms = [cloudbeds_pms_v1_3.PostReservationRequestRoomsInner()] # List[PostReservationRequestRoomsInner] | Array with quantity of rooms (optional)
    adults = [cloudbeds_pms_v1_3.PostReservationRequestAdultsInner()] # List[PostReservationRequestAdultsInner] | Array with number of adults (optional)
    children = [cloudbeds_pms_v1_3.PostReservationRequestChildrenInner()] # List[PostReservationRequestChildrenInner] | Array with number of children (optional)
    payment_method = 'payment_method_example' # str | Payment Method of choice. (optional)
    card_token = 'card_token_example' # str | Credit Card identifier. Payment Method must be credit. This field should be filled with credit card identifier according to gateway. Only available for Stripe and should send the Customer ID. (optional)
    payment_authorization_code = 'payment_authorization_code_example' # str | Transaction identifier. Payment Method must be credit. This field should be filled with transaction identifier according to gateway. Only available for Stripe and it should be filled with Charge ID associated to the Payment Intent. (optional)
    custom_fields = [cloudbeds_pms_v1_3.PostReservationRequestCustomFieldsInner()] # List[PostReservationRequestCustomFieldsInner] | Array with custom fields information (optional)
    promo_code = 'promo_code_example' # str | Promotional code. Required for specials and packages that uses it. \\\"rateID\\\" parameter required for using \\\"promoCode\\\". (optional)
    allotment_block_code = 'allotment_block_code_example' # str | Allotment block code to add reservation to allotment block. (optional)
    group_code = 'group_code_example' # str | Code from the Aggregate Allotment block the reservation will be added to. (optional)
    date_created = '2013-10-20T19:20:30+01:00' # datetime | Date reservation was made. Defaults to current date if omitted. (optional)
    send_email_confirmation = True # bool | Send confirmation email to guest. (optional) (default to True)

    try:
        # postReservation
        api_response = api_instance.post_reservation_post(property_id=property_id, source_id=source_id, third_party_identifier=third_party_identifier, start_date=start_date, end_date=end_date, guest_first_name=guest_first_name, guest_last_name=guest_last_name, guest_gender=guest_gender, guest_country=guest_country, guest_zip=guest_zip, guest_email=guest_email, guest_phone=guest_phone, guest_requirements=guest_requirements, estimated_arrival_time=estimated_arrival_time, rooms=rooms, adults=adults, children=children, payment_method=payment_method, card_token=card_token, payment_authorization_code=payment_authorization_code, custom_fields=custom_fields, promo_code=promo_code, allotment_block_code=allotment_block_code, group_code=group_code, date_created=date_created, send_email_confirmation=send_email_confirmation)
        print("The response of ReservationApi->post_reservation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->post_reservation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **source_id** | **str**| The third-party source ID for this reservation. | [optional] 
 **third_party_identifier** | **str**| If it was received from a booking channel, this can be an identifier from that channel. | [optional] 
 **start_date** | **date**| Check-In date. | [optional] 
 **end_date** | **date**| Check-Out date. | [optional] 
 **guest_first_name** | **str**| First name of the guest | [optional] 
 **guest_last_name** | **str**| Last name of the guest | [optional] 
 **guest_gender** | **str**|  | [optional] 
 **guest_country** | **str**| Valid ISO-Code for Country (2 characters) | [optional] 
 **guest_zip** | **str**| ZIP Code | [optional] 
 **guest_email** | **str**| Guest email | [optional] 
 **guest_phone** | **str**| Guest main phone number | [optional] 
 **guest_requirements** | [**List[object]**](object.md)| Object with guest requirements information. | [optional] 
 **estimated_arrival_time** | **str**| Estimated Arrival Time, 24-hour format. | [optional] 
 **rooms** | [**List[PostReservationRequestRoomsInner]**](PostReservationRequestRoomsInner.md)| Array with quantity of rooms | [optional] 
 **adults** | [**List[PostReservationRequestAdultsInner]**](PostReservationRequestAdultsInner.md)| Array with number of adults | [optional] 
 **children** | [**List[PostReservationRequestChildrenInner]**](PostReservationRequestChildrenInner.md)| Array with number of children | [optional] 
 **payment_method** | **str**| Payment Method of choice. | [optional] 
 **card_token** | **str**| Credit Card identifier. Payment Method must be credit. This field should be filled with credit card identifier according to gateway. Only available for Stripe and should send the Customer ID. | [optional] 
 **payment_authorization_code** | **str**| Transaction identifier. Payment Method must be credit. This field should be filled with transaction identifier according to gateway. Only available for Stripe and it should be filled with Charge ID associated to the Payment Intent. | [optional] 
 **custom_fields** | [**List[PostReservationRequestCustomFieldsInner]**](PostReservationRequestCustomFieldsInner.md)| Array with custom fields information | [optional] 
 **promo_code** | **str**| Promotional code. Required for specials and packages that uses it. \\\&quot;rateID\\\&quot; parameter required for using \\\&quot;promoCode\\\&quot;. | [optional] 
 **allotment_block_code** | **str**| Allotment block code to add reservation to allotment block. | [optional] 
 **group_code** | **str**| Code from the Aggregate Allotment block the reservation will be added to. | [optional] 
 **date_created** | **datetime**| Date reservation was made. Defaults to current date if omitted. | [optional] 
 **send_email_confirmation** | **bool**| Send confirmation email to guest. | [optional] [default to True]

### Return type

[**PostReservationResponse**](PostReservationResponse.md)

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

# **put_reservation_note_put**
> PutReservationNoteResponse put_reservation_note_put(property_id=property_id, reservation_id=reservation_id, reservation_note_id=reservation_note_id, reservation_note=reservation_note)

putReservationNote

Updates an existing reservation note.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.put_reservation_note_response import PutReservationNoteResponse
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
    api_instance = cloudbeds_pms_v1_3.ReservationApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation Unique Identifier (optional)
    reservation_note_id = 'reservation_note_id_example' # str | Reservation Note ID (optional)
    reservation_note = 'reservation_note_example' # str | Note to be added to reservation (optional)

    try:
        # putReservationNote
        api_response = api_instance.put_reservation_note_put(property_id=property_id, reservation_id=reservation_id, reservation_note_id=reservation_note_id, reservation_note=reservation_note)
        print("The response of ReservationApi->put_reservation_note_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->put_reservation_note_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation Unique Identifier | [optional] 
 **reservation_note_id** | **str**| Reservation Note ID | [optional] 
 **reservation_note** | **str**| Note to be added to reservation | [optional] 

### Return type

[**PutReservationNoteResponse**](PutReservationNoteResponse.md)

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

# **put_reservation_put**
> PutReservationResponse put_reservation_put(property_id=property_id, reservation_id=reservation_id, estimated_arrival_time=estimated_arrival_time, status=status, checkout_date=checkout_date, custom_fields=custom_fields, rooms=rooms, date_created=date_created, send_status_change_email=send_status_change_email)

putReservation

Updates a reservation, such as custom fields, estimated arrival time, room configuration and reservation status.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.put_reservation_request_custom_fields_inner import PutReservationRequestCustomFieldsInner
from cloudbeds_pms_v1_3.models.put_reservation_request_rooms_inner import PutReservationRequestRoomsInner
from cloudbeds_pms_v1_3.models.put_reservation_response import PutReservationResponse
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
    api_instance = cloudbeds_pms_v1_3.ReservationApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation Unique Identifier, one reservation ID per call. (optional)
    estimated_arrival_time = 'estimated_arrival_time_example' # str | Estimated Arrival Time, 24-hour format. (optional)
    status = 'status_example' # str | Reservation status<br /> 'confirmed' - Reservation is confirmed<br /> 'not_confirmed' - Reservation not passed confirmation<br /> 'canceled' - Reservation is canceled<br /> 'checked_in' - Guest is in hotel<br /> 'checked_out' - Guest already left hotel<br /> 'no_show' - Guest didn't showed up on check-in date (optional)
    checkout_date = '2013-10-20' # date | Update the checkoutDate across the whole reservation (optional)
    custom_fields = [cloudbeds_pms_v1_3.PutReservationRequestCustomFieldsInner()] # List[PutReservationRequestCustomFieldsInner] | Array with custom fields information (optional)
    rooms = [cloudbeds_pms_v1_3.PutReservationRequestRoomsInner()] # List[PutReservationRequestRoomsInner] | Array with rooms information to change accommodations assigned to the reservation (optional)
    date_created = '2013-10-20T19:20:30+01:00' # datetime | Date reservation was made. Do not change if omitted. (optional)
    send_status_change_email = False # bool | Send email on reservation status change to property and guest. (optional) (default to False)

    try:
        # putReservation
        api_response = api_instance.put_reservation_put(property_id=property_id, reservation_id=reservation_id, estimated_arrival_time=estimated_arrival_time, status=status, checkout_date=checkout_date, custom_fields=custom_fields, rooms=rooms, date_created=date_created, send_status_change_email=send_status_change_email)
        print("The response of ReservationApi->put_reservation_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->put_reservation_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation Unique Identifier, one reservation ID per call. | [optional] 
 **estimated_arrival_time** | **str**| Estimated Arrival Time, 24-hour format. | [optional] 
 **status** | **str**| Reservation status&lt;br /&gt; &#39;confirmed&#39; - Reservation is confirmed&lt;br /&gt; &#39;not_confirmed&#39; - Reservation not passed confirmation&lt;br /&gt; &#39;canceled&#39; - Reservation is canceled&lt;br /&gt; &#39;checked_in&#39; - Guest is in hotel&lt;br /&gt; &#39;checked_out&#39; - Guest already left hotel&lt;br /&gt; &#39;no_show&#39; - Guest didn&#39;t showed up on check-in date | [optional] 
 **checkout_date** | **date**| Update the checkoutDate across the whole reservation | [optional] 
 **custom_fields** | [**List[PutReservationRequestCustomFieldsInner]**](PutReservationRequestCustomFieldsInner.md)| Array with custom fields information | [optional] 
 **rooms** | [**List[PutReservationRequestRoomsInner]**](PutReservationRequestRoomsInner.md)| Array with rooms information to change accommodations assigned to the reservation | [optional] 
 **date_created** | **datetime**| Date reservation was made. Do not change if omitted. | [optional] 
 **send_status_change_email** | **bool**| Send email on reservation status change to property and guest. | [optional] [default to False]

### Return type

[**PutReservationResponse**](PutReservationResponse.md)

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

