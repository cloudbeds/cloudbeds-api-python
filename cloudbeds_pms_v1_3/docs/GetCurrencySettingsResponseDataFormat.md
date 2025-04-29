# GetCurrencySettingsResponseDataFormat

Currency Format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decimal** | **str** | Decimal separator | [optional] 
**thousand** | **str** | Thousand separator | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_currency_settings_response_data_format import GetCurrencySettingsResponseDataFormat

# TODO update the JSON string below
json = "{}"
# create an instance of GetCurrencySettingsResponseDataFormat from a JSON string
get_currency_settings_response_data_format_instance = GetCurrencySettingsResponseDataFormat.from_json(json)
# print the JSON string representation of the object
print(GetCurrencySettingsResponseDataFormat.to_json())

# convert the object into a dict
get_currency_settings_response_data_format_dict = get_currency_settings_response_data_format_instance.to_dict()
# create an instance of GetCurrencySettingsResponseDataFormat from a dict
get_currency_settings_response_data_format_from_dict = GetCurrencySettingsResponseDataFormat.from_dict(get_currency_settings_response_data_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


