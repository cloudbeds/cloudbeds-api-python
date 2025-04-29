# PostAppSettingsRequestSettingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name of a setting option | [optional] 
**value** | **str** | A value of a setting option | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_app_settings_request_settings_inner import PostAppSettingsRequestSettingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostAppSettingsRequestSettingsInner from a JSON string
post_app_settings_request_settings_inner_instance = PostAppSettingsRequestSettingsInner.from_json(json)
# print the JSON string representation of the object
print(PostAppSettingsRequestSettingsInner.to_json())

# convert the object into a dict
post_app_settings_request_settings_inner_dict = post_app_settings_request_settings_inner_instance.to_dict()
# create an instance of PostAppSettingsRequestSettingsInner from a dict
post_app_settings_request_settings_inner_from_dict = PostAppSettingsRequestSettingsInner.from_dict(post_app_settings_request_settings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


