# AddonSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_id** | **str** | Add-on ID | 
**name** | **str** | Add-on display name | 
**amount** | [**MoneyInputSchema**](MoneyInputSchema.md) |  | 
**quantity** | **int** | Quantity (&gt;&#x3D; 1) | 
**taxes_and_fees** | [**List[TaxFeeConfigSchema]**](TaxFeeConfigSchema.md) | Tax/fee configuration for this addon | [optional] 
**is_default** | **bool** | Whether this is a default (package) add-on | [optional] 

## Example

```python
from cloudbeds_pms.models.addon_schema import AddonSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AddonSchema from a JSON string
addon_schema_instance = AddonSchema.from_json(json)
# print the JSON string representation of the object
print(AddonSchema.to_json())

# convert the object into a dict
addon_schema_dict = addon_schema_instance.to_dict()
# create an instance of AddonSchema from a dict
addon_schema_from_dict = AddonSchema.from_dict(addon_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


