# GetCurrencySettingsResponseDataRates

Currency rates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed** | [**List[GetCurrencySettingsResponseDataRatesFixedInner]**](GetCurrencySettingsResponseDataRatesFixedInner.md) | Fixed currency rates (configured by the property) | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_currency_settings_response_data_rates import GetCurrencySettingsResponseDataRates

# TODO update the JSON string below
json = "{}"
# create an instance of GetCurrencySettingsResponseDataRates from a JSON string
get_currency_settings_response_data_rates_instance = GetCurrencySettingsResponseDataRates.from_json(json)
# print the JSON string representation of the object
print(GetCurrencySettingsResponseDataRates.to_json())

# convert the object into a dict
get_currency_settings_response_data_rates_dict = get_currency_settings_response_data_rates_instance.to_dict()
# create an instance of GetCurrencySettingsResponseDataRates from a dict
get_currency_settings_response_data_rates_from_dict = GetCurrencySettingsResponseDataRates.from_dict(get_currency_settings_response_data_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


