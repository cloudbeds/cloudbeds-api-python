# AssignableRoomsControllerGetAssignableRooms200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation** | [**LegacyReservationContextSchema**](LegacyReservationContextSchema.md) |  | 
**room_types** | [**List[LegacyRoomTypeOptionSchema]**](LegacyRoomTypeOptionSchema.md) | Selectable room types (names only, no pricing). | 
**selected_room_type_id** | **int** | The room type the rates and rooms below are scoped to. | 
**rates** | [**List[LegacyRatePlanSchema]**](LegacyRatePlanSchema.md) | Rate plans for the selected room type, totalled over the stay. | 
**rooms** | [**List[AssignableRoomSchema]**](AssignableRoomSchema.md) | Rooms of the selected type free for the whole stay. Includes the reservation&#39;s currently-assigned room when the selected type matches its current type (match on reservation.currentRoomId), so the drawer can render it as selected. | 

## Example

```python
from cloudbeds_pms.models.assignable_rooms_controller_get_assignable_rooms200_response import AssignableRoomsControllerGetAssignableRooms200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AssignableRoomsControllerGetAssignableRooms200Response from a JSON string
assignable_rooms_controller_get_assignable_rooms200_response_instance = AssignableRoomsControllerGetAssignableRooms200Response.from_json(json)
# print the JSON string representation of the object
print(AssignableRoomsControllerGetAssignableRooms200Response.to_json())

# convert the object into a dict
assignable_rooms_controller_get_assignable_rooms200_response_dict = assignable_rooms_controller_get_assignable_rooms200_response_instance.to_dict()
# create an instance of AssignableRoomsControllerGetAssignableRooms200Response from a dict
assignable_rooms_controller_get_assignable_rooms200_response_from_dict = AssignableRoomsControllerGetAssignableRooms200Response.from_dict(assignable_rooms_controller_get_assignable_rooms200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


