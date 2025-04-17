# GetTaxesAndFeesResponseDataInnerDateRangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | **object** | ISO 8601 date range. It can be in the format YYYY-MM-DD/YYYY-MM-DD or YYYY-MM-DD/ (to indicate that the end date is not defined). In case of empty year the format is --MM-DD/--MM-DD | [optional] 
**amount** | **float** | Amount | [optional] 
**amount_adult** | **float** | Amount charged per adult. Only applicable if amountType &#x3D; fixed_per_person (Per Person Per Night) | [optional] 
**amount_child** | **float** | Amount charged per children. Only applicable if amountType &#x3D; fixed_per_person (Per Person Per Night) | [optional] 
**amount_rate_based** | [**List[GetTaxesAndFeesResponseDataInnerAmountRateBasedInner]**](GetTaxesAndFeesResponseDataInnerAmountRateBasedInner.md) | Rules defined for Rate-Based taxes/fees. Only applicable if amountType &#x3D; percentage_rate_based (Rate-based) | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_taxes_and_fees_response_data_inner_date_ranges_inner import GetTaxesAndFeesResponseDataInnerDateRangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaxesAndFeesResponseDataInnerDateRangesInner from a JSON string
get_taxes_and_fees_response_data_inner_date_ranges_inner_instance = GetTaxesAndFeesResponseDataInnerDateRangesInner.from_json(json)
# print the JSON string representation of the object
print(GetTaxesAndFeesResponseDataInnerDateRangesInner.to_json())

# convert the object into a dict
get_taxes_and_fees_response_data_inner_date_ranges_inner_dict = get_taxes_and_fees_response_data_inner_date_ranges_inner_instance.to_dict()
# create an instance of GetTaxesAndFeesResponseDataInnerDateRangesInner from a dict
get_taxes_and_fees_response_data_inner_date_ranges_inner_from_dict = GetTaxesAndFeesResponseDataInnerDateRangesInner.from_dict(get_taxes_and_fees_response_data_inner_date_ranges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


