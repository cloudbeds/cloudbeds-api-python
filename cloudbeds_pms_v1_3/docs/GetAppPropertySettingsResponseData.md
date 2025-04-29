# GetAppPropertySettingsResponseData

Data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**key** | **str** | Key | [optional] 
**value** | **str** | Value | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_app_property_settings_response_data import GetAppPropertySettingsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppPropertySettingsResponseData from a JSON string
get_app_property_settings_response_data_instance = GetAppPropertySettingsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetAppPropertySettingsResponseData.to_json())

# convert the object into a dict
get_app_property_settings_response_data_dict = get_app_property_settings_response_data_instance.to_dict()
# create an instance of GetAppPropertySettingsResponseData from a dict
get_app_property_settings_response_data_from_dict = GetAppPropertySettingsResponseData.from_dict(get_app_property_settings_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


