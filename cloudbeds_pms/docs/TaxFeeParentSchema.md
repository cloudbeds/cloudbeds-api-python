# TaxFeeParentSchema

Compound parent reference — points to another tax (tax-on-tax) or fee (tax-on-fee) in the same request. A tax row may carry multiple parents (e.g. taxed on both a parent fee AND a parent tax); see `TaxFeeConfigSchema::$parents`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the parent tax or fee (must match an &#x60;id&#x60; in the same request). | 
**kind** | **str** | Whether the parent is a tax or a fee. | 

## Example

```python
from cloudbeds_pms.models.tax_fee_parent_schema import TaxFeeParentSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaxFeeParentSchema from a JSON string
tax_fee_parent_schema_instance = TaxFeeParentSchema.from_json(json)
# print the JSON string representation of the object
print(TaxFeeParentSchema.to_json())

# convert the object into a dict
tax_fee_parent_schema_dict = tax_fee_parent_schema_instance.to_dict()
# create an instance of TaxFeeParentSchema from a dict
tax_fee_parent_schema_from_dict = TaxFeeParentSchema.from_dict(tax_fee_parent_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


