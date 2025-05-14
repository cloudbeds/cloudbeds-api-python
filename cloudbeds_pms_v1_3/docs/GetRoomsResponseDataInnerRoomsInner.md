# GetRoomsResponseDataInnerRoomsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_id** | **str** | Room ID | [optional] 
**room_name** | **str** | Room Name | [optional] 
**dorm_room_name** | **str** | Name of the dorm room. Used for the shared dorm beds that are organized into rooms within the same room type | [optional] 
**room_description** | **str** | Room Description | [optional] 
**max_guests** | **int** | Number of guests that room allows | [optional] 
**is_private** | **bool** | If room is private (true) or shared (false) | [optional] 
**is_virtual** | **bool** | If room is virtual (true) or physical (false) | [optional] 
**room_blocked** | **bool** | If room is blocked on calendar during the period selected. If no check-in/out dates are sent, it returns the status for the current day. | [optional] 
**room_type_id** | **str** | Room type ID | [optional] 
**room_type_name** | **str** | Room type Name | [optional] 
**room_type_name_short** | **str** | Room type Short Name | [optional] 
**doorlock_id** | **str** | The doorlock ID for the room | [optional] 
**linked_room_ids** | **List[str]** | List of linked room IDs for this room (including nested relations). Only returned if includeRoomRelations is set to true | [optional] 
**linked_room_type_ids** | **List[str]** | List of linked room type IDs. Only returned if includeRoomRelations is set to true | [optional] 
**linked_room_type_qty** | [**List[GetRoomsResponseDataInnerRoomsInnerLinkedRoomTypeQtyInner]**](GetRoomsResponseDataInnerRoomsInnerLinkedRoomTypeQtyInner.md) | Data about linked rooms count, grouped by room type. Only returned if includeRoomRelations is set to true | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_rooms_response_data_inner_rooms_inner import GetRoomsResponseDataInnerRoomsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomsResponseDataInnerRoomsInner from a JSON string
get_rooms_response_data_inner_rooms_inner_instance = GetRoomsResponseDataInnerRoomsInner.from_json(json)
# print the JSON string representation of the object
print(GetRoomsResponseDataInnerRoomsInner.to_json())

# convert the object into a dict
get_rooms_response_data_inner_rooms_inner_dict = get_rooms_response_data_inner_rooms_inner_instance.to_dict()
# create an instance of GetRoomsResponseDataInnerRoomsInner from a dict
get_rooms_response_data_inner_rooms_inner_from_dict = GetRoomsResponseDataInnerRoomsInner.from_dict(get_rooms_response_data_inner_rooms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


