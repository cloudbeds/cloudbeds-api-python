# GetTaxesAndFeesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type. Fee or tax. | [optional] 
**fee_id** | **str** | Fee&#39;s unique identifier. Only exists if type &#x3D; fee. | [optional] 
**tax_id** | **str** | Tax&#39;s unique identifier. Only exists if type &#x3D; tax. | [optional] 
**name** | **str** | Name | [optional] 
**code** | **str** | Code | [optional] 
**kind** | **str** | Tax kind. Currently supports \&quot;vat\&quot; or null. Only exists if type &#x3D; tax. | [optional] 
**amount** | **str** | Amount | [optional] 
**amount_adult** | [**GetTaxesAndFeesResponseDataInnerAmountAdult**](GetTaxesAndFeesResponseDataInnerAmountAdult.md) |  | [optional] 
**amount_child** | [**GetTaxesAndFeesResponseDataInnerAmountChild**](GetTaxesAndFeesResponseDataInnerAmountChild.md) |  | [optional] 
**amount_rate_based** | [**List[GetTaxesAndFeesResponseDataInnerAmountRateBasedInner]**](GetTaxesAndFeesResponseDataInnerAmountRateBasedInner.md) | Rules defined for Rate-Based taxes/fees. Only applicable if amountType &#x3D; percentage_rate_based (Rate-based) | [optional] 
**amount_type** | **str** | Amount type. They mean:&lt;br/&gt; &lt;table&gt; &lt;tr&gt;&lt;th&gt;Value&lt;/th&gt;&lt;th&gt;Meaning&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;percentage&lt;/td&gt;&lt;td&gt;Percentage of Total Amount&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;fixed&lt;/td&gt;&lt;td&gt;Fixed per Room Night / Item&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;fixed_per_person&lt;/td&gt;&lt;td&gt;Fixed per Person per Night&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;fixed_per_accomodation&lt;/td&gt;&lt;td&gt;Fixed per Accomodation&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;fixed_per_reservation&lt;/td&gt;&lt;td&gt;Fixed per Reservation&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;percentage_rate_based&lt;/td&gt;&lt;td&gt;Rate-based&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; | [optional] 
**available_for** | **List[str]** | Where this tax/fee is available?&lt;br/&gt;They mean:&lt;br/&gt; &lt;table&gt; &lt;tr&gt;&lt;th&gt;Value&lt;/th&gt;&lt;th&gt;Meaning&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;product&lt;/td&gt;&lt;td&gt;Items&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;rate&lt;/td&gt;&lt;td&gt;Reservations&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;fee&lt;/td&gt;&lt;td&gt;Fees -- this tax is charged on top of some fees&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;custom_item&lt;/td&gt;&lt;td&gt;Custom item - this tax was charged for a custom item&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; | [optional] 
**fees_charged** | **List[str]** | List of Fee IDs charged by the current tax. Only exists if type &#x3D; tax. | [optional] 
**inclusive_or_exclusive** | **str** | If this tax/fee is inclusive or exclusive | [optional] 
**is_deleted** | **bool** | Flag indicating if tax was deleted from the system | [optional] 
**child_id** | **str** | ID of the tax or fee that replaced current one | [optional] 
**created_at** | **str** | Date when tax or fee was created in the system | [optional] 
**expired_at** | **str** | Date when tax or fee was expired | [optional] 
**room_types** | [**List[GetTaxesAndFeesResponseDataInnerRoomTypesInner]**](GetTaxesAndFeesResponseDataInnerRoomTypesInner.md) | Room types this tax/fee applies to | [optional] 
**date_ranges** | [**List[GetTaxesAndFeesResponseDataInnerDateRangesInner]**](GetTaxesAndFeesResponseDataInnerDateRangesInner.md) | Date ranges when this tax/fee is applicable | [optional] 
**length_of_stay_settings** | [**GetTaxesAndFeesResponseDataInnerLengthOfStaySettings**](GetTaxesAndFeesResponseDataInnerLengthOfStaySettings.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_taxes_and_fees_response_data_inner import GetTaxesAndFeesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaxesAndFeesResponseDataInner from a JSON string
get_taxes_and_fees_response_data_inner_instance = GetTaxesAndFeesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetTaxesAndFeesResponseDataInner.to_json())

# convert the object into a dict
get_taxes_and_fees_response_data_inner_dict = get_taxes_and_fees_response_data_inner_instance.to_dict()
# create an instance of GetTaxesAndFeesResponseDataInner from a dict
get_taxes_and_fees_response_data_inner_from_dict = GetTaxesAndFeesResponseDataInner.from_dict(get_taxes_and_fees_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


