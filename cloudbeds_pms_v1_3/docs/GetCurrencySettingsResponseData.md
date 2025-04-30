# GetCurrencySettingsResponseData

Currency Settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Default Currency ISO CODE | [optional] 
**acceptable** | **List[str]** | Acceptable Currency ISO CODEs | [optional] 
**format** | [**GetCurrencySettingsResponseDataFormat**](GetCurrencySettingsResponseDataFormat.md) |  | [optional] 
**rates** | [**GetCurrencySettingsResponseDataRates**](GetCurrencySettingsResponseDataRates.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_currency_settings_response_data import GetCurrencySettingsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetCurrencySettingsResponseData from a JSON string
get_currency_settings_response_data_instance = GetCurrencySettingsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetCurrencySettingsResponseData.to_json())

# convert the object into a dict
get_currency_settings_response_data_dict = get_currency_settings_response_data_instance.to_dict()
# create an instance of GetCurrencySettingsResponseData from a dict
get_currency_settings_response_data_from_dict = GetCurrencySettingsResponseData.from_dict(get_currency_settings_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


