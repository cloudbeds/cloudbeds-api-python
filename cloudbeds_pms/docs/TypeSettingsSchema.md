# TypeSettingsSchema

Additional type settings for tax/fee calculation. All properties are optional — only provide what applies to the specific tax/fee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_adult** | **str** | Per-adult fixed amount in minor currency units (e.g. 1000 &#x3D; $10.00). Used with fixed_per_person calculation type when adults and children have different rates. | [optional] 
**amount_child** | **str** | Per-child fixed amount in minor currency units (e.g. 500 &#x3D; $5.00). Used with fixed_per_person calculation type when adults and children have different rates. | [optional] 
**amount_rate_based** | [**List[RateBasedTierSchema]**](RateBasedTierSchema.md) | Rate-based percentage tiers. Required for percentage_rate_based calculation type. Each tier defines a rate threshold and the tax percentage to apply when the base rate meets it. | [optional] 
**max_length** | **int** | Maximum number of nights to charge for per-person taxes. When set, per-person taxes stop accruing after this many nights per guest. | [optional] 
**date_ranges** | [**List[DateRangeSchema]**](DateRangeSchema.md) | Date ranges with amount overrides. When present, the tax/fee only applies on nights that fall within a matching range, using the range&#39;s overridden amounts. If no range matches a given night, the tax/fee is excluded for that night. | [optional] 
**length_of_stay** | [**LengthOfStaySchema**](LengthOfStaySchema.md) |  | [optional] 
**exclusive_base** | **str** | Base an exclusive percentage tax/fee multiplies when exclusiveTaxesOnTotal is on: \&quot;net\&quot; carves inclusive taxes and fees out first, \&quot;gross\&quot; multiplies the quoted price. Meaningful only for exclusive percentage rows; absent defaults to net. | [optional] 
**amount_per_person_rate_based** | [**List[PerPersonRateBasedTierSchema]**](PerPersonRateBasedTierSchema.md) | Per-person rate tiers. Required for fixed_per_person_rate_based calculation type. Each tier defines a gross nightly rate floor and the per-adult and per-child amounts charged when the room&#39;s rate meets it. | [optional] 

## Example

```python
from cloudbeds_pms.models.type_settings_schema import TypeSettingsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TypeSettingsSchema from a JSON string
type_settings_schema_instance = TypeSettingsSchema.from_json(json)
# print the JSON string representation of the object
print(TypeSettingsSchema.to_json())

# convert the object into a dict
type_settings_schema_dict = type_settings_schema_instance.to_dict()
# create an instance of TypeSettingsSchema from a dict
type_settings_schema_from_dict = TypeSettingsSchema.from_dict(type_settings_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


