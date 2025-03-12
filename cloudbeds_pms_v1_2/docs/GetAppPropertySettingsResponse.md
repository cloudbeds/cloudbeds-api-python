# GetAppPropertySettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success | [optional] 
**data** | [**GetAppPropertySettingsResponseData**](GetAppPropertySettingsResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_app_property_settings_response import GetAppPropertySettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppPropertySettingsResponse from a JSON string
get_app_property_settings_response_instance = GetAppPropertySettingsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAppPropertySettingsResponse.to_json())

# convert the object into a dict
get_app_property_settings_response_dict = get_app_property_settings_response_instance.to_dict()
# create an instance of GetAppPropertySettingsResponse from a dict
get_app_property_settings_response_from_dict = GetAppPropertySettingsResponse.from_dict(get_app_property_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


