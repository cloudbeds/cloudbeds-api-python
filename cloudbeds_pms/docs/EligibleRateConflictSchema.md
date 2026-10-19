# EligibleRateConflictSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exception_id** | **str** | ID of the blocking exception. | 
**exception_name** | **str** | Name of the blocking exception. | 

## Example

```python
from cloudbeds_pms.models.eligible_rate_conflict_schema import EligibleRateConflictSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EligibleRateConflictSchema from a JSON string
eligible_rate_conflict_schema_instance = EligibleRateConflictSchema.from_json(json)
# print the JSON string representation of the object
print(EligibleRateConflictSchema.to_json())

# convert the object into a dict
eligible_rate_conflict_schema_dict = eligible_rate_conflict_schema_instance.to_dict()
# create an instance of EligibleRateConflictSchema from a dict
eligible_rate_conflict_schema_from_dict = EligibleRateConflictSchema.from_dict(eligible_rate_conflict_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


