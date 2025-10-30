# ReservationRoomControllerUpdateRoomRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_id** | **str** | Room ID to assign (format: &#39;roomTypeId-roomNumber&#39;), or null to unassign | [optional] 
**adjust_price** | **bool** | Whether to adjust price if room assignment changes rate | [optional] [default to False]

## Example

```python
from cloudbeds_pms.models.reservation_room_controller_update_room_request import ReservationRoomControllerUpdateRoomRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationRoomControllerUpdateRoomRequest from a JSON string
reservation_room_controller_update_room_request_instance = ReservationRoomControllerUpdateRoomRequest.from_json(json)
# print the JSON string representation of the object
print(ReservationRoomControllerUpdateRoomRequest.to_json())

# convert the object into a dict
reservation_room_controller_update_room_request_dict = reservation_room_controller_update_room_request_instance.to_dict()
# create an instance of ReservationRoomControllerUpdateRoomRequest from a dict
reservation_room_controller_update_room_request_from_dict = ReservationRoomControllerUpdateRoomRequest.from_dict(reservation_room_controller_update_room_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


