# GetTaxesAndFeesResponseDataInnerDateRangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | **str** | ISO 8601 date range. It can be in the format YYYY-MM-DD/YYYY-MM-DD or YYYY-MM-DD/ (to indicate that the end date is not defined). In case of empty year the format is --MM-DD/--MM-DD | [optional] 
**amount** | [**GetTaxesAndFeesResponseDataInnerDateRangesInnerAmount**](GetTaxesAndFeesResponseDataInnerDateRangesInnerAmount.md) |  | [optional] 
**amount_adult** | [**GetTaxesAndFeesResponseDataInnerAmountAdult**](GetTaxesAndFeesResponseDataInnerAmountAdult.md) |  | [optional] 
**amount_child** | [**GetTaxesAndFeesResponseDataInnerAmountChild**](GetTaxesAndFeesResponseDataInnerAmountChild.md) |  | [optional] 
**max_length** | [**GetTaxesAndFeesResponseDataInnerDateRangesInnerMaxLength**](GetTaxesAndFeesResponseDataInnerDateRangesInnerMaxLength.md) |  | [optional] 
**amount_rate_based** | [**List[GetTaxesAndFeesResponseDataInnerAmountRateBasedInner]**](GetTaxesAndFeesResponseDataInnerAmountRateBasedInner.md) | Rules defined for Rate-Based taxes/fees. Only applicable if amountType &#x3D; percentage_rate_based (Rate-based) | [optional] 
**length_of_stay_settings** | [**GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettings**](GetTaxesAndFeesResponseDataInnerDateRangesInnerLengthOfStaySettings.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_taxes_and_fees_response_data_inner_date_ranges_inner import GetTaxesAndFeesResponseDataInnerDateRangesInner

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


