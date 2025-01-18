# PostRoomBlockRequestRoomsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_id** | **str** | Room ID | [optional] 
**room_type_id** | **str** | Room type ID | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_room_block_request_rooms_inner import PostRoomBlockRequestRoomsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostRoomBlockRequestRoomsInner from a JSON string
post_room_block_request_rooms_inner_instance = PostRoomBlockRequestRoomsInner.from_json(json)
# print the JSON string representation of the object
print(PostRoomBlockRequestRoomsInner.to_json())

# convert the object into a dict
post_room_block_request_rooms_inner_dict = post_room_block_request_rooms_inner_instance.to_dict()
# create an instance of PostRoomBlockRequestRoomsInner from a dict
post_room_block_request_rooms_inner_from_dict = PostRoomBlockRequestRoomsInner.from_dict(post_room_block_request_rooms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


