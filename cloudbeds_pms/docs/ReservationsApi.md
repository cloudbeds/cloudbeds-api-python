# cloudbeds_pms.ReservationsApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservation_room_controller_update_room**](ReservationsApi.md#reservation_room_controller_update_room) | **PATCH** /reservation/v1/reservations/{reservationId}/rooms/{reservationRoomId} | Update room assignment for a reservation


# **reservation_room_controller_update_room**
> UpdateReservationRoomResponseSchema reservation_room_controller_update_room(x_property_id, reservation_id, reservation_room_id, reservation_room_controller_update_room_request)

Update room assignment for a reservation

Assign, reassign, or unassign a room to/from a reservation booking room

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.reservation_room_controller_update_room_request import ReservationRoomControllerUpdateRoomRequest
from cloudbeds_pms.models.update_reservation_room_response_schema import UpdateReservationRoomResponseSchema
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
    api_instance = cloudbeds_pms.ReservationsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    reservation_id = '12345' # str | Reservation identifier
    reservation_room_id = '67890' # str | Reservation room identifier
    reservation_room_controller_update_room_request = cloudbeds_pms.ReservationRoomControllerUpdateRoomRequest() # ReservationRoomControllerUpdateRoomRequest | Room update data

    try:
        # Update room assignment for a reservation
        api_response = api_instance.reservation_room_controller_update_room(x_property_id, reservation_id, reservation_room_id, reservation_room_controller_update_room_request)
        print("The response of ReservationsApi->reservation_room_controller_update_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationsApi->reservation_room_controller_update_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **reservation_id** | **str**| Reservation identifier | 
 **reservation_room_id** | **str**| Reservation room identifier | 
 **reservation_room_controller_update_room_request** | [**ReservationRoomControllerUpdateRoomRequest**](ReservationRoomControllerUpdateRoomRequest.md)| Room update data | 

### Return type

[**UpdateReservationRoomResponseSchema**](UpdateReservationRoomResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room updated successfully |  -  |
**400** | Bad Request - Invalid input data |  -  |
**401** | Unauthorized response |  -  |
**403** | Forbidden response |  -  |
**404** | Not Found - Reservation or reservation room not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

