# TaxFeeConfigSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier within the request | 
**name** | **str** | Display name | 
**category** | **str** | Whether this is a tax or a fee | 
**calculation_type** | **str** | How the amount is calculated | 
**value** | **str** | Rate or amount value in minor units. For percentage types: the percentage in minor units (e.g., \&quot;1000\&quot; &#x3D; 10.00%). For fixed types: the amount in minor currency units (e.g., \&quot;1500\&quot; &#x3D; $15.00). | 
**tax_treatment** | **str** | How this tax/fee relates to the base amount | 
**applied_to** | **List[str]** | Application targets — where the tax/fee gets applied. A tax with &#x60;appliedTo&#x3D;[\&quot;rate\&quot;,\&quot;fee\&quot;]&#x60; is applied both to the base rate AND to each parent of type \&quot;fee\&quot;. Defaults are derived from &#x60;category&#x60; + &#x60;parents&#x60; when omitted: a fee → &#x60;[\&quot;rate\&quot;]&#x60;; a tax with no parent → &#x60;[\&quot;rate\&quot;]&#x60;; a tax with a &#x60;fee&#x60; parent → &#x60;[\&quot;fee\&quot;]&#x60;; a tax with a &#x60;tax&#x60; parent → &#x60;[\&quot;tax\&quot;]&#x60;. | [optional] 
**parents** | [**List[TaxFeeParentSchema]**](TaxFeeParentSchema.md) | Compound parents (tax-on-fee, tax-on-tax). A tax may reference multiple parents. | [optional] 
**parent_id** | **str** | Deprecated — use &#x60;parents&#x60; instead. Single parent ID for tax-on-fee or tax-on-tax. Kept for backward compatibility; when set (and &#x60;parents&#x60; is omitted) it is mapped to a single-element &#x60;parents&#x60; list. | [optional] 
**parent_kind** | **str** | Deprecated — use &#x60;parents&#x60; instead. Kind of the legacy &#x60;parentId&#x60; parent. | [optional] 
**room_type_ids** | **List[str]** | Room type IDs this tax/fee applies to. Empty means all room types. | [optional] 
**type_settings** | [**TypeSettingsSchema**](TypeSettingsSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.tax_fee_config_schema import TaxFeeConfigSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaxFeeConfigSchema from a JSON string
tax_fee_config_schema_instance = TaxFeeConfigSchema.from_json(json)
# print the JSON string representation of the object
print(TaxFeeConfigSchema.to_json())

# convert the object into a dict
tax_fee_config_schema_dict = tax_fee_config_schema_instance.to_dict()
# create an instance of TaxFeeConfigSchema from a dict
tax_fee_config_schema_from_dict = TaxFeeConfigSchema.from_dict(tax_fee_config_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


