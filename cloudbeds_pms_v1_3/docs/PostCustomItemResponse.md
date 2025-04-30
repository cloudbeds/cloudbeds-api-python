# PostCustomItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**PostCustomItemResponseData**](PostCustomItemResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_custom_item_response import PostCustomItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostCustomItemResponse from a JSON string
post_custom_item_response_instance = PostCustomItemResponse.from_json(json)
# print the JSON string representation of the object
print(PostCustomItemResponse.to_json())

# convert the object into a dict
post_custom_item_response_dict = post_custom_item_response_instance.to_dict()
# create an instance of PostCustomItemResponse from a dict
post_custom_item_response_from_dict = PostCustomItemResponse.from_dict(post_custom_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


