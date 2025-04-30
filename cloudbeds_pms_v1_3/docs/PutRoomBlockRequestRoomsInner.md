# PutRoomBlockRequestRoomsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_id** | **str** | Room ID | [optional] 
**room_type_id** | **str** | Room type ID | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.put_room_block_request_rooms_inner import PutRoomBlockRequestRoomsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PutRoomBlockRequestRoomsInner from a JSON string
put_room_block_request_rooms_inner_instance = PutRoomBlockRequestRoomsInner.from_json(json)
# print the JSON string representation of the object
print(PutRoomBlockRequestRoomsInner.to_json())

# convert the object into a dict
put_room_block_request_rooms_inner_dict = put_room_block_request_rooms_inner_instance.to_dict()
# create an instance of PutRoomBlockRequestRoomsInner from a dict
put_room_block_request_rooms_inner_from_dict = PutRoomBlockRequestRoomsInner.from_dict(put_room_block_request_rooms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


