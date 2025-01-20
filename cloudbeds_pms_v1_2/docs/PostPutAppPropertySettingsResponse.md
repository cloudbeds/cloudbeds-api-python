# PostPutAppPropertySettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success | [optional] 
**data** | [**PostAppPropertySettingResponseData**](PostAppPropertySettingResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_put_app_property_settings_response import PostPutAppPropertySettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostPutAppPropertySettingsResponse from a JSON string
post_put_app_property_settings_response_instance = PostPutAppPropertySettingsResponse.from_json(json)
# print the JSON string representation of the object
print(PostPutAppPropertySettingsResponse.to_json())

# convert the object into a dict
post_put_app_property_settings_response_dict = post_put_app_property_settings_response_instance.to_dict()
# create an instance of PostPutAppPropertySettingsResponse from a dict
post_put_app_property_settings_response_from_dict = PostPutAppPropertySettingsResponse.from_dict(post_put_app_property_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


