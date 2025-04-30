# PostRoomBlockResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**property_id** | **str** | Property ID | [optional] 
**room_block_id** | **str** | Room block ID | [optional] 
**room_block_type** | **str** | Room block type. ‘blocked’ - Room block. ‘out_of_service’ - Out of service block | [optional] 
**room_block_reason** | **str** | Room block reason | [optional] 
**start_date** | **date** | Room block start date | [optional] 
**end_date** | **date** | Room block end date | [optional] 
**rooms** | [**List[PostRoomBlockResponseRoomsInner]**](PostRoomBlockResponseRoomsInner.md) | All rooms for room block | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false).  If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_room_block_response import PostRoomBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostRoomBlockResponse from a JSON string
post_room_block_response_instance = PostRoomBlockResponse.from_json(json)
# print the JSON string representation of the object
print(PostRoomBlockResponse.to_json())

# convert the object into a dict
post_room_block_response_dict = post_room_block_response_instance.to_dict()
# create an instance of PostRoomBlockResponse from a dict
post_room_block_response_from_dict = PostRoomBlockResponse.from_dict(post_room_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


