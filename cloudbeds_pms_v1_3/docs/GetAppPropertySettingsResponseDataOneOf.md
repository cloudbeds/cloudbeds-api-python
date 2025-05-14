# GetAppPropertySettingsResponseDataOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**key** | **str** | Key | [optional] 
**value** | **str** | Value | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_app_property_settings_response_data_one_of import GetAppPropertySettingsResponseDataOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppPropertySettingsResponseDataOneOf from a JSON string
get_app_property_settings_response_data_one_of_instance = GetAppPropertySettingsResponseDataOneOf.from_json(json)
# print the JSON string representation of the object
print(GetAppPropertySettingsResponseDataOneOf.to_json())

# convert the object into a dict
get_app_property_settings_response_data_one_of_dict = get_app_property_settings_response_data_one_of_instance.to_dict()
# create an instance of GetAppPropertySettingsResponseDataOneOf from a dict
get_app_property_settings_response_data_one_of_from_dict = GetAppPropertySettingsResponseDataOneOf.from_dict(get_app_property_settings_response_data_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


