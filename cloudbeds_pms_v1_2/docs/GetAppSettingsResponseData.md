# GetAppSettingsResponseData

Application settings details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_revenue_sync** | **bool** | Full Revenue Sync | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_app_settings_response_data import GetAppSettingsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppSettingsResponseData from a JSON string
get_app_settings_response_data_instance = GetAppSettingsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetAppSettingsResponseData.to_json())

# convert the object into a dict
get_app_settings_response_data_dict = get_app_settings_response_data_instance.to_dict()
# create an instance of GetAppSettingsResponseData from a dict
get_app_settings_response_data_from_dict = GetAppSettingsResponseData.from_dict(get_app_settings_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


