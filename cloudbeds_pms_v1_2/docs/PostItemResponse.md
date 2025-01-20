# PostItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**PostItemResponseData**](PostItemResponseData.md) |  | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_item_response import PostItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostItemResponse from a JSON string
post_item_response_instance = PostItemResponse.from_json(json)
# print the JSON string representation of the object
print(PostItemResponse.to_json())

# convert the object into a dict
post_item_response_dict = post_item_response_instance.to_dict()
# create an instance of PostItemResponse from a dict
post_item_response_from_dict = PostItemResponse.from_dict(post_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


