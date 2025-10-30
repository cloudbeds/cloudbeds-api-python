# UpdateReservationRoomRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** | Reservation ID | 
**reservation_room_id** | **str** | Reservation Room ID | 
**room_id** | **str** | Room ID to assign (format: &#39;roomTypeId-roomNumber&#39;), or null to unassign | [optional] 
**room_type_id** | **int** | Room type ID to change to (without assigning specific room), or null | [optional] 
**adjust_price** | **bool** | Whether to adjust price if room assignment changes rate | [optional] [default to False]

## Example

```python
from cloudbeds_pms.models.update_reservation_room_request_schema import UpdateReservationRoomRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReservationRoomRequestSchema from a JSON string
update_reservation_room_request_schema_instance = UpdateReservationRoomRequestSchema.from_json(json)
# print the JSON string representation of the object
print(UpdateReservationRoomRequestSchema.to_json())

# convert the object into a dict
update_reservation_room_request_schema_dict = update_reservation_room_request_schema_instance.to_dict()
# create an instance of UpdateReservationRoomRequestSchema from a dict
update_reservation_room_request_schema_from_dict = UpdateReservationRoomRequestSchema.from_dict(update_reservation_room_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


