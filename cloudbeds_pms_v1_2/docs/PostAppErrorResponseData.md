# PostAppErrorResponseData

Integration state details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_id** | **str** | Unique ID of error recorded in Cloudbeds | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_app_error_response_data import PostAppErrorResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostAppErrorResponseData from a JSON string
post_app_error_response_data_instance = PostAppErrorResponseData.from_json(json)
# print the JSON string representation of the object
print(PostAppErrorResponseData.to_json())

# convert the object into a dict
post_app_error_response_data_dict = post_app_error_response_data_instance.to_dict()
# create an instance of PostAppErrorResponseData from a dict
post_app_error_response_data_from_dict = PostAppErrorResponseData.from_dict(post_app_error_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


