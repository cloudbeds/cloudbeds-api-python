# GetAppSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**GetAppSettingsResponseData**](GetAppSettingsResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_app_settings_response import GetAppSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppSettingsResponse from a JSON string
get_app_settings_response_instance = GetAppSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAppSettingsResponse.to_json())

# convert the object into a dict
get_app_settings_response_dict = get_app_settings_response_instance.to_dict()
# create an instance of GetAppSettingsResponse from a dict
get_app_settings_response_from_dict = GetAppSettingsResponse.from_dict(get_app_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


