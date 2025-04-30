# PostAppendCustomItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**PostAppendCustomItemResponseData**](PostAppendCustomItemResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_append_custom_item_response import PostAppendCustomItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAppendCustomItemResponse from a JSON string
post_append_custom_item_response_instance = PostAppendCustomItemResponse.from_json(json)
# print the JSON string representation of the object
print(PostAppendCustomItemResponse.to_json())

# convert the object into a dict
post_append_custom_item_response_dict = post_append_custom_item_response_instance.to_dict()
# create an instance of PostAppendCustomItemResponse from a dict
post_append_custom_item_response_from_dict = PostAppendCustomItemResponse.from_dict(post_append_custom_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


