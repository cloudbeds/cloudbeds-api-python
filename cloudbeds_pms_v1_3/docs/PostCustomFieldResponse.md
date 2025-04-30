# PostCustomFieldResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**PostCustomFieldResponseData**](PostCustomFieldResponseData.md) |  | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_custom_field_response import PostCustomFieldResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostCustomFieldResponse from a JSON string
post_custom_field_response_instance = PostCustomFieldResponse.from_json(json)
# print the JSON string representation of the object
print(PostCustomFieldResponse.to_json())

# convert the object into a dict
post_custom_field_response_dict = post_custom_field_response_instance.to_dict()
# create an instance of PostCustomFieldResponse from a dict
post_custom_field_response_from_dict = PostCustomFieldResponse.from_dict(post_custom_field_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


