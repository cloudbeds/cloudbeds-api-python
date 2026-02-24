# GetRoomBlocksResponseDataInnerRoomsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Event ID (unique identifier for this specific room&#39;s block entry) | [optional] 
**room_id** | **str** | Room ID | [optional] 
**room_type_id** | **str** | Room type ID | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_room_blocks_response_data_inner_rooms_inner import GetRoomBlocksResponseDataInnerRoomsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomBlocksResponseDataInnerRoomsInner from a JSON string
get_room_blocks_response_data_inner_rooms_inner_instance = GetRoomBlocksResponseDataInnerRoomsInner.from_json(json)
# print the JSON string representation of the object
print(GetRoomBlocksResponseDataInnerRoomsInner.to_json())

# convert the object into a dict
get_room_blocks_response_data_inner_rooms_inner_dict = get_room_blocks_response_data_inner_rooms_inner_instance.to_dict()
# create an instance of GetRoomBlocksResponseDataInnerRoomsInner from a dict
get_room_blocks_response_data_inner_rooms_inner_from_dict = GetRoomBlocksResponseDataInnerRoomsInner.from_dict(get_room_blocks_response_data_inner_rooms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


