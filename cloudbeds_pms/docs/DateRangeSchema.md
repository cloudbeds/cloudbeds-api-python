# DateRangeSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | **str** | Date range in \&quot;start/end\&quot; format. Dates can be full (YYYY-MM-DD) or recurring annual (--MM-DD). End date can be omitted for open-ended ranges. | 
**amount** | **str** | Override tax/fee amount when this date range matches, in minor currency units (e.g. 1500 &#x3D; $15.00). | [optional] 
**amount_adult** | **str** | Override per-adult amount in minor currency units (e.g. 500 &#x3D; $5.00). | [optional] 
**amount_child** | **str** | Override per-child amount in minor currency units (e.g. 250 &#x3D; $2.50). | [optional] 
**amount_rate_based** | [**List[RateBasedTierSchema]**](RateBasedTierSchema.md) | Override rate-based tiers. | [optional] 
**max_length** | **int** | Override max nights to charge. | [optional] 
**length_of_stay** | [**LengthOfStaySchema**](LengthOfStaySchema.md) |  | [optional] 
**amount_per_person_rate_based** | [**List[PerPersonRateBasedTierSchema]**](PerPersonRateBasedTierSchema.md) | Override per-person rate tiers. | [optional] 

## Example

```python
from cloudbeds_pms.models.date_range_schema import DateRangeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DateRangeSchema from a JSON string
date_range_schema_instance = DateRangeSchema.from_json(json)
# print the JSON string representation of the object
print(DateRangeSchema.to_json())

# convert the object into a dict
date_range_schema_dict = date_range_schema_instance.to_dict()
# create an instance of DateRangeSchema from a dict
date_range_schema_from_dict = DateRangeSchema.from_dict(date_range_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


