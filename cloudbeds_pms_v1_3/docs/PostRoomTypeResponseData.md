# PostRoomTypeResponseData

Details for the new accommodation type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | ID for the newly-created accommodation type | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_room_type_response_data import PostRoomTypeResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostRoomTypeResponseData from a JSON string
post_room_type_response_data_instance = PostRoomTypeResponseData.from_json(json)
# print the JSON string representation of the object
print(PostRoomTypeResponseData.to_json())

# convert the object into a dict
post_room_type_response_data_dict = post_room_type_response_data_instance.to_dict()
# create an instance of PostRoomTypeResponseData from a dict
post_room_type_response_data_from_dict = PostRoomTypeResponseData.from_dict(post_room_type_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


