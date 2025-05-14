# PostAppStateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_app_state_response import PostAppStateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAppStateResponse from a JSON string
post_app_state_response_instance = PostAppStateResponse.from_json(json)
# print the JSON string representation of the object
print(PostAppStateResponse.to_json())

# convert the object into a dict
post_app_state_response_dict = post_app_state_response_instance.to_dict()
# create an instance of PostAppStateResponse from a dict
post_app_state_response_from_dict = PostAppStateResponse.from_dict(post_app_state_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


