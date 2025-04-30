# GetCurrencySettingsResponseDataRatesFixedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency ISO CODE | [optional] 
**rate** | **float** | Currency rate | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_currency_settings_response_data_rates_fixed_inner import GetCurrencySettingsResponseDataRatesFixedInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCurrencySettingsResponseDataRatesFixedInner from a JSON string
get_currency_settings_response_data_rates_fixed_inner_instance = GetCurrencySettingsResponseDataRatesFixedInner.from_json(json)
# print the JSON string representation of the object
print(GetCurrencySettingsResponseDataRatesFixedInner.to_json())

# convert the object into a dict
get_currency_settings_response_data_rates_fixed_inner_dict = get_currency_settings_response_data_rates_fixed_inner_instance.to_dict()
# create an instance of GetCurrencySettingsResponseDataRatesFixedInner from a dict
get_currency_settings_response_data_rates_fixed_inner_from_dict = GetCurrencySettingsResponseDataRatesFixedInner.from_dict(get_currency_settings_response_data_rates_fixed_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


