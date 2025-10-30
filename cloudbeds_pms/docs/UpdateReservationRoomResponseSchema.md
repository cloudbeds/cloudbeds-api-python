# UpdateReservationRoomResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_room_id** | **int** | Reservation room ID that was updated | 
**room_id** | **str** | Assigned room ID (null if unassigned) | 
**room_type_id** | **int** | Room type ID | 
**room_name** | **str** | Room name | 
**total** | [**UpdateReservationRoomResponseSchemaTotal**](UpdateReservationRoomResponseSchemaTotal.md) |  | 

## Example

```python
from cloudbeds_pms.models.update_reservation_room_response_schema import UpdateReservationRoomResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReservationRoomResponseSchema from a JSON string
update_reservation_room_response_schema_instance = UpdateReservationRoomResponseSchema.from_json(json)
# print the JSON string representation of the object
print(UpdateReservationRoomResponseSchema.to_json())

# convert the object into a dict
update_reservation_room_response_schema_dict = update_reservation_room_response_schema_instance.to_dict()
# create an instance of UpdateReservationRoomResponseSchema from a dict
update_reservation_room_response_schema_from_dict = UpdateReservationRoomResponseSchema.from_dict(update_reservation_room_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


