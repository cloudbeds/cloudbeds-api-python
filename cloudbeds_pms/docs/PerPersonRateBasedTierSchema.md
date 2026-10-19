# PerPersonRateBasedTierSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **str** | Gross nightly rate floor in minor currency units. The tier with the highest rate at or below the room&#39;s nightly rate applies (e.g. 10000 &#x3D; 100.00). | 
**amount_adult** | **str** | Charged once per adult per night, in minor currency units. Absent means adults are not charged. | [optional] 
**amount_child** | **str** | Charged once per child per night, in minor currency units. Absent means children are not charged. | [optional] 

## Example

```python
from cloudbeds_pms.models.per_person_rate_based_tier_schema import PerPersonRateBasedTierSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PerPersonRateBasedTierSchema from a JSON string
per_person_rate_based_tier_schema_instance = PerPersonRateBasedTierSchema.from_json(json)
# print the JSON string representation of the object
print(PerPersonRateBasedTierSchema.to_json())

# convert the object into a dict
per_person_rate_based_tier_schema_dict = per_person_rate_based_tier_schema_instance.to_dict()
# create an instance of PerPersonRateBasedTierSchema from a dict
per_person_rate_based_tier_schema_from_dict = PerPersonRateBasedTierSchema.from_dict(per_person_rate_based_tier_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


