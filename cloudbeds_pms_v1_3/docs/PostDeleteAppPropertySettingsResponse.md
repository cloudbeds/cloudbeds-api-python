# PostDeleteAppPropertySettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success | [optional] 
**message** | **str** | Response message | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_delete_app_property_settings_response import PostDeleteAppPropertySettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteAppPropertySettingsResponse from a JSON string
post_delete_app_property_settings_response_instance = PostDeleteAppPropertySettingsResponse.from_json(json)
# print the JSON string representation of the object
print(PostDeleteAppPropertySettingsResponse.to_json())

# convert the object into a dict
post_delete_app_property_settings_response_dict = post_delete_app_property_settings_response_instance.to_dict()
# create an instance of PostDeleteAppPropertySettingsResponse from a dict
post_delete_app_property_settings_response_from_dict = PostDeleteAppPropertySettingsResponse.from_dict(post_delete_app_property_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


