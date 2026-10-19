# RateBasedTierSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **str** | Rate threshold in minor currency units. Tax tier applies when the base rate is &gt;&#x3D; this value (e.g. 15000 &#x3D; $150.00). | 
**percentage** | **str** | Tax percentage to apply when the rate threshold is met, in minor units (e.g. 1000 &#x3D; 10.00%). | 

## Example

```python
from cloudbeds_pms.models.rate_based_tier_schema import RateBasedTierSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RateBasedTierSchema from a JSON string
rate_based_tier_schema_instance = RateBasedTierSchema.from_json(json)
# print the JSON string representation of the object
print(RateBasedTierSchema.to_json())

# convert the object into a dict
rate_based_tier_schema_dict = rate_based_tier_schema_instance.to_dict()
# create an instance of RateBasedTierSchema from a dict
rate_based_tier_schema_from_dict = RateBasedTierSchema.from_dict(rate_based_tier_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


