# AssignableRoomsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation** | [**ReservationContextSchema**](ReservationContextSchema.md) |  | 
**room_types** | [**List[RoomTypeOptionSchema]**](RoomTypeOptionSchema.md) | Selectable room types (names only, no pricing). | 
**selected_room_type_id** | **str** | The room type the rates and rooms below are scoped to. | 
**rates** | [**List[RatePlanSchema]**](RatePlanSchema.md) | Rate plans for the selected room type, totalled over the stay. | 
**rooms** | [**List[AssignableRoomSchema]**](AssignableRoomSchema.md) | Rooms of the selected type free for the whole stay. Includes the reservation&#39;s currently-assigned room when the selected type matches its current type (match on reservation.currentRoomId), so the drawer can render it as selected. | 

## Example

```python
from cloudbeds_pms.models.assignable_rooms_response_schema import AssignableRoomsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AssignableRoomsResponseSchema from a JSON string
assignable_rooms_response_schema_instance = AssignableRoomsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AssignableRoomsResponseSchema.to_json())

# convert the object into a dict
assignable_rooms_response_schema_dict = assignable_rooms_response_schema_instance.to_dict()
# create an instance of AssignableRoomsResponseSchema from a dict
assignable_rooms_response_schema_from_dict = AssignableRoomsResponseSchema.from_dict(assignable_rooms_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


