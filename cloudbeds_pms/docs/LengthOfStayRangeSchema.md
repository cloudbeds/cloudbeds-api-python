# LengthOfStayRangeSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_nights** | **int** | Minimum nights for this range to apply (inclusive). | 
**maximum_nights** | **int** | Maximum nights for this range (inclusive). Null means no upper limit. | [optional] 
**amount** | **str** | Override tax/fee amount for this range, in minor currency units (e.g. 1000 &#x3D; $10.00). | [optional] 
**amount_adult** | **str** | Override per-adult amount for this range, in minor currency units (e.g. 500 &#x3D; $5.00). | [optional] 
**amount_child** | **str** | Override per-child amount for this range, in minor currency units (e.g. 250 &#x3D; $2.50). | [optional] 
**amount_rate_based** | [**List[RateBasedTierSchema]**](RateBasedTierSchema.md) | Override rate-based tiers for this range. | [optional] 
**max_length** | **int** | Override max nights to charge for per-person taxes. | [optional] 
**amount_per_person_rate_based** | [**List[PerPersonRateBasedTierSchema]**](PerPersonRateBasedTierSchema.md) | Override per-person rate tiers for this range. | [optional] 

## Example

```python
from cloudbeds_pms.models.length_of_stay_range_schema import LengthOfStayRangeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LengthOfStayRangeSchema from a JSON string
length_of_stay_range_schema_instance = LengthOfStayRangeSchema.from_json(json)
# print the JSON string representation of the object
print(LengthOfStayRangeSchema.to_json())

# convert the object into a dict
length_of_stay_range_schema_dict = length_of_stay_range_schema_instance.to_dict()
# create an instance of LengthOfStayRangeSchema from a dict
length_of_stay_range_schema_from_dict = LengthOfStayRangeSchema.from_dict(length_of_stay_range_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


