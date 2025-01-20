# PostVoidItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_void_item_response import PostVoidItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostVoidItemResponse from a JSON string
post_void_item_response_instance = PostVoidItemResponse.from_json(json)
# print the JSON string representation of the object
print(PostVoidItemResponse.to_json())

# convert the object into a dict
post_void_item_response_dict = post_void_item_response_instance.to_dict()
# create an instance of PostVoidItemResponse from a dict
post_void_item_response_from_dict = PostVoidItemResponse.from_dict(post_void_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


