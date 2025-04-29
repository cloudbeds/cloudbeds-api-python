# PostReservationRequestRoomsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | Room Type ID | [optional] 
**quantity** | **int** | Quantity of rooms for the room type ID | [optional] 
**room_id** | **str** | ID of the individual room to be booked. This feature must be enabled on \&quot;MyBookings\&quot; settings, and the room should be available at the time of the booking or else it will result in an unassigned room. It will automatically override \&quot;quantity\&quot; value to 1 and roomTypeID when used. | [optional] 
**room_rate_id** | **str** | Specific Rate ID used for the room type ID. Can be ommitted. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_reservation_request_rooms_inner import PostReservationRequestRoomsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostReservationRequestRoomsInner from a JSON string
post_reservation_request_rooms_inner_instance = PostReservationRequestRoomsInner.from_json(json)
# print the JSON string representation of the object
print(PostReservationRequestRoomsInner.to_json())

# convert the object into a dict
post_reservation_request_rooms_inner_dict = post_reservation_request_rooms_inner_instance.to_dict()
# create an instance of PostReservationRequestRoomsInner from a dict
post_reservation_request_rooms_inner_from_dict = PostReservationRequestRoomsInner.from_dict(post_reservation_request_rooms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


