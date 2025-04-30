# PostRoomCheckInResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_room_check_in_response import PostRoomCheckInResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostRoomCheckInResponse from a JSON string
post_room_check_in_response_instance = PostRoomCheckInResponse.from_json(json)
# print the JSON string representation of the object
print(PostRoomCheckInResponse.to_json())

# convert the object into a dict
post_room_check_in_response_dict = post_room_check_in_response_instance.to_dict()
# create an instance of PostRoomCheckInResponse from a dict
post_room_check_in_response_from_dict = PostRoomCheckInResponse.from_dict(post_room_check_in_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


