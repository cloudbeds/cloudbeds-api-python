# TaxFeeItemResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Tax/fee ID (echoed) | 
**name** | **str** | Display name (echoed) | 
**amount** | [**MoneySchema**](MoneySchema.md) |  | 
**tax_treatment** | **str** | Tax treatment (echoed) | 
**parents** | [**List[TaxFeeParentResponseSchema]**](TaxFeeParentResponseSchema.md) | Compound parents (tax-on-fee, tax-on-tax). Empty when the row is not a compound tax. | [optional] 

## Example

```python
from cloudbeds_pms.models.tax_fee_item_response_schema import TaxFeeItemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaxFeeItemResponseSchema from a JSON string
tax_fee_item_response_schema_instance = TaxFeeItemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(TaxFeeItemResponseSchema.to_json())

# convert the object into a dict
tax_fee_item_response_schema_dict = tax_fee_item_response_schema_instance.to_dict()
# create an instance of TaxFeeItemResponseSchema from a dict
tax_fee_item_response_schema_from_dict = TaxFeeItemResponseSchema.from_dict(tax_fee_item_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


