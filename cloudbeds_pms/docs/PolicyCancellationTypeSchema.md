# PolicyCancellationTypeSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Human-readable cancellation type label. | 
**type** | **str** | Machine-readable cancellation type. | 
**fully_refundable_until_days_before_check_in** | **int** | Days before check-in midnight until which the reservation is fully refundable (floored, legacy field); null when not applicable. | [optional] 
**fully_refundable_until_days_before_date** | **str** | ISO date (YYYY-MM-DD) of the refund deadline (legacy, day-rounded); null when not applicable. | [optional] 
**fully_refundable_until_date_time** | **datetime** | Exact ISO 8601 datetime of the refund deadline; null when not applicable. | [optional] 
**fully_refundable_until_minutes_before_check_in** | **int** | Minutes before check-in date midnight (not check-in time) of the refund deadline; null when not applicable. | [optional] 

## Example

```python
from cloudbeds_pms.models.policy_cancellation_type_schema import PolicyCancellationTypeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyCancellationTypeSchema from a JSON string
policy_cancellation_type_schema_instance = PolicyCancellationTypeSchema.from_json(json)
# print the JSON string representation of the object
print(PolicyCancellationTypeSchema.to_json())

# convert the object into a dict
policy_cancellation_type_schema_dict = policy_cancellation_type_schema_instance.to_dict()
# create an instance of PolicyCancellationTypeSchema from a dict
policy_cancellation_type_schema_from_dict = PolicyCancellationTypeSchema.from_dict(policy_cancellation_type_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


