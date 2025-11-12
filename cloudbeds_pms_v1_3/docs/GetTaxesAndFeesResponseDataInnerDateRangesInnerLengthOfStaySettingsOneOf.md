# GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_type** | **str** | Application type for Length of Stay rules | [optional] 
**ranges** | [**List[GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOfRangesInner]**](GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOfRangesInner.md) | Night-based ranges for Length of Stay configuration | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_taxes_and_fees_response_data_inner_date_ranges_inner_length_of_stay_settings_one_of import GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOf from a JSON string
get_taxes_and_fees_response_data_inner_date_ranges_inner_length_of_stay_settings_one_of_instance = GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOf.from_json(json)
# print the JSON string representation of the object
print(GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOf.to_json())

# convert the object into a dict
get_taxes_and_fees_response_data_inner_date_ranges_inner_length_of_stay_settings_one_of_dict = get_taxes_and_fees_response_data_inner_date_ranges_inner_length_of_stay_settings_one_of_instance.to_dict()
# create an instance of GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOf from a dict
get_taxes_and_fees_response_data_inner_date_ranges_inner_length_of_stay_settings_one_of_from_dict = GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOf.from_dict(get_taxes_and_fees_response_data_inner_date_ranges_inner_length_of_stay_settings_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


