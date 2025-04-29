# PostAppSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | **object** | Application settings details | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_app_settings_response import PostAppSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAppSettingsResponse from a JSON string
post_app_settings_response_instance = PostAppSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(PostAppSettingsResponse.to_json())

# convert the object into a dict
post_app_settings_response_dict = post_app_settings_response_instance.to_dict()
# create an instance of PostAppSettingsResponse from a dict
post_app_settings_response_from_dict = PostAppSettingsResponse.from_dict(post_app_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


