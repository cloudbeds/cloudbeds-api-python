# PostRoomBlockResponseRoomsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Event ID (unique identifier for this specific room&#39;s block entry) | [optional] 
**room_id** | **str** | Room ID | [optional] 
**room_type_id** | **str** | Room Type ID | [optional] 
**is_source** | **bool** | Indicates whether this room was explicitly requested (true) or automatically added due to split inventory configuration (false). Auto-added rooms cannot be individually removed or swapped; they are managed through their source room. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_room_block_response_rooms_inner import PostRoomBlockResponseRoomsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostRoomBlockResponseRoomsInner from a JSON string
post_room_block_response_rooms_inner_instance = PostRoomBlockResponseRoomsInner.from_json(json)
# print the JSON string representation of the object
print(PostRoomBlockResponseRoomsInner.to_json())

# convert the object into a dict
post_room_block_response_rooms_inner_dict = post_room_block_response_rooms_inner_instance.to_dict()
# create an instance of PostRoomBlockResponseRoomsInner from a dict
post_room_block_response_rooms_inner_from_dict = PostRoomBlockResponseRoomsInner.from_dict(post_room_block_response_rooms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


