# GetAppPropertySettingsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**key** | **str** | Key | [optional] 
**value** | **str** | Value | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_app_property_settings_response_data_inner import GetAppPropertySettingsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppPropertySettingsResponseDataInner from a JSON string
get_app_property_settings_response_data_inner_instance = GetAppPropertySettingsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetAppPropertySettingsResponseDataInner.to_json())

# convert the object into a dict
get_app_property_settings_response_data_inner_dict = get_app_property_settings_response_data_inner_instance.to_dict()
# create an instance of GetAppPropertySettingsResponseDataInner from a dict
get_app_property_settings_response_data_inner_from_dict = GetAppPropertySettingsResponseDataInner.from_dict(get_app_property_settings_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


