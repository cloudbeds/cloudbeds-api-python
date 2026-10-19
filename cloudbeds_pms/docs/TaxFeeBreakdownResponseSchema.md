# TaxFeeBreakdownResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**MoneySchema**](MoneySchema.md) |  | 
**items** | [**List[TaxFeeItemResponseSchema]**](TaxFeeItemResponseSchema.md) | Individual line items | 

## Example

```python
from cloudbeds_pms.models.tax_fee_breakdown_response_schema import TaxFeeBreakdownResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaxFeeBreakdownResponseSchema from a JSON string
tax_fee_breakdown_response_schema_instance = TaxFeeBreakdownResponseSchema.from_json(json)
# print the JSON string representation of the object
print(TaxFeeBreakdownResponseSchema.to_json())

# convert the object into a dict
tax_fee_breakdown_response_schema_dict = tax_fee_breakdown_response_schema_instance.to_dict()
# create an instance of TaxFeeBreakdownResponseSchema from a dict
tax_fee_breakdown_response_schema_from_dict = TaxFeeBreakdownResponseSchema.from_dict(tax_fee_breakdown_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


