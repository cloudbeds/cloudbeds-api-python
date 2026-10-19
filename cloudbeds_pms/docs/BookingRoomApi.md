# cloudbeds_pms.BookingRoomApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignable_rooms_controller_get_assignable_rooms**](BookingRoomApi.md#assignable_rooms_controller_get_assignable_rooms) | **GET** /booking-room/v1/{bookingRoomId}/assignable-rooms | Get rooms a reservation can be reassigned to


# **assignable_rooms_controller_get_assignable_rooms**
> AssignableRoomsControllerGetAssignableRooms200Response assignable_rooms_controller_get_assignable_rooms(x_property_id, booking_room_id, room_type_id=room_type_id)

Get rooms a reservation can be reassigned to

Returns the reservation's current room assignment, the property's room types, and the rates and rooms available for a room type: the reservation's current type when roomTypeId is omitted, or the requested type when it is provided.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.assignable_rooms_controller_get_assignable_rooms200_response import AssignableRoomsControllerGetAssignableRooms200Response
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
    api_instance = cloudbeds_pms.BookingRoomApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    booking_room_id = '713' # str | The reservation's current room assignment.
    room_type_id = '713' # str | Scopes rates and rooms to this room type. Omit to use the reservation's current type. (optional)

    try:
        # Get rooms a reservation can be reassigned to
        api_response = api_instance.assignable_rooms_controller_get_assignable_rooms(x_property_id, booking_room_id, room_type_id=room_type_id)
        print("The response of BookingRoomApi->assignable_rooms_controller_get_assignable_rooms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookingRoomApi->assignable_rooms_controller_get_assignable_rooms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **booking_room_id** | **str**| The reservation&#39;s current room assignment. | 
 **room_type_id** | **str**| Scopes rates and rooms to this room type. Omit to use the reservation&#39;s current type. | [optional] 

### Return type

[**AssignableRoomsControllerGetAssignableRooms200Response**](AssignableRoomsControllerGetAssignableRooms200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assignable rooms and supporting data |  -  |
**400** | Malformed request |  -  |
**403** | No permission for the property |  -  |
**404** | Booking room not found / out of scope |  -  |
**422** | Invalid room type for property, or reservation not reassignable |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

