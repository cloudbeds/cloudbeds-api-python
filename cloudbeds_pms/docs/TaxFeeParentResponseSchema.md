# TaxFeeParentResponseSchema

Compound parent reference echoed back on each tax/fee line item — counterpart of the request-side `TaxFeeParentSchema`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the parent tax or fee. | 
**kind** | **str** | Whether the parent is a tax or a fee. | 

## Example

```python
from cloudbeds_pms.models.tax_fee_parent_response_schema import TaxFeeParentResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaxFeeParentResponseSchema from a JSON string
tax_fee_parent_response_schema_instance = TaxFeeParentResponseSchema.from_json(json)
# print the JSON string representation of the object
print(TaxFeeParentResponseSchema.to_json())

# convert the object into a dict
tax_fee_parent_response_schema_dict = tax_fee_parent_response_schema_instance.to_dict()
# create an instance of TaxFeeParentResponseSchema from a dict
tax_fee_parent_response_schema_from_dict = TaxFeeParentResponseSchema.from_dict(tax_fee_parent_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


