# GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOfRangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_nights** | **int** | Minimum number of nights required for this range | [optional] 
**maximum_nights** | **int** | Maximum number of nights for this range (null means no limit) | [optional] 
**amount** | **float** | Amount for this range | [optional] 
**amount_adult** | **float** | Amount per adult for this range | [optional] 
**amount_child** | **float** | Amount per child for this range | [optional] 
**amount_rate_based** | **List[object]** | Rate-based amounts for this range | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_taxes_and_fees_response_data_inner_date_ranges_inner_length_of_stay_settings_one_of_ranges_inner import GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOfRangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOfRangesInner from a JSON string
get_taxes_and_fees_response_data_inner_date_ranges_inner_length_of_stay_settings_one_of_ranges_inner_instance = GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOfRangesInner.from_json(json)
# print the JSON string representation of the object
print(GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOfRangesInner.to_json())

# convert the object into a dict
get_taxes_and_fees_response_data_inner_date_ranges_inner_length_of_stay_settings_one_of_ranges_inner_dict = get_taxes_and_fees_response_data_inner_date_ranges_inner_length_of_stay_settings_one_of_ranges_inner_instance.to_dict()
# create an instance of GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOfRangesInner from a dict
get_taxes_and_fees_response_data_inner_date_ranges_inner_length_of_stay_settings_one_of_ranges_inner_from_dict = GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettingsOneOfRangesInner.from_dict(get_taxes_and_fees_response_data_inner_date_ranges_inner_length_of_stay_settings_one_of_ranges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


