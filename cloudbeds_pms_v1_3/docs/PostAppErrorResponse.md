# PostAppErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**PostAppErrorResponseData**](PostAppErrorResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_app_error_response import PostAppErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAppErrorResponse from a JSON string
post_app_error_response_instance = PostAppErrorResponse.from_json(json)
# print the JSON string representation of the object
print(PostAppErrorResponse.to_json())

# convert the object into a dict
post_app_error_response_dict = post_app_error_response_instance.to_dict()
# create an instance of PostAppErrorResponse from a dict
post_app_error_response_from_dict = PostAppErrorResponse.from_dict(post_app_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


