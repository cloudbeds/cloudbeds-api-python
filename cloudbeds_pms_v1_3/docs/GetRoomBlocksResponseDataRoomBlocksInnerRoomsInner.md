# GetRoomBlocksResponseDataRoomBlocksInnerRoomsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Event ID (unique identifier for this specific room’s block entry) | [optional] 
**room_id** | **str** | Room ID | [optional] 
**room_type_id** | [**GetRoomBlocksResponseDataRoomBlocksInnerRoomsInnerRoomTypeID**](GetRoomBlocksResponseDataRoomBlocksInnerRoomsInnerRoomTypeID.md) |  | [optional] 
**is_source** | **bool** | Indicates whether this room was explicitly requested (true) or automatically added due to split inventory configuration (false). Auto-added rooms cannot be individually removed or swapped; they are managed through their source room. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_room_blocks_response_data_room_blocks_inner_rooms_inner import GetRoomBlocksResponseDataRoomBlocksInnerRoomsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomBlocksResponseDataRoomBlocksInnerRoomsInner from a JSON string
get_room_blocks_response_data_room_blocks_inner_rooms_inner_instance = GetRoomBlocksResponseDataRoomBlocksInnerRoomsInner.from_json(json)
# print the JSON string representation of the object
print(GetRoomBlocksResponseDataRoomBlocksInnerRoomsInner.to_json())

# convert the object into a dict
get_room_blocks_response_data_room_blocks_inner_rooms_inner_dict = get_room_blocks_response_data_room_blocks_inner_rooms_inner_instance.to_dict()
# create an instance of GetRoomBlocksResponseDataRoomBlocksInnerRoomsInner from a dict
get_room_blocks_response_data_room_blocks_inner_rooms_inner_from_dict = GetRoomBlocksResponseDataRoomBlocksInnerRoomsInner.from_dict(get_room_blocks_response_data_room_blocks_inner_rooms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


