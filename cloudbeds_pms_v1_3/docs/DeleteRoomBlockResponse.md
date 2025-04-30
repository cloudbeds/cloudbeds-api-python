# DeleteRoomBlockResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false).  If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.delete_room_block_response import DeleteRoomBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRoomBlockResponse from a JSON string
delete_room_block_response_instance = DeleteRoomBlockResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteRoomBlockResponse.to_json())

# convert the object into a dict
delete_room_block_response_dict = delete_room_block_response_instance.to_dict()
# create an instance of DeleteRoomBlockResponse from a dict
delete_room_block_response_from_dict = DeleteRoomBlockResponse.from_dict(delete_room_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


