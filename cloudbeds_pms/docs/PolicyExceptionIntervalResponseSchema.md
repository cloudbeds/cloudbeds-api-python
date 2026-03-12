# PolicyExceptionIntervalResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**day0** | **bool** | Sunday (day 0) -- apply exception on this day of the week. | [optional] 
**day1** | **bool** | Monday (day 1) -- apply exception on this day of the week. | [optional] 
**day2** | **bool** | Tuesday (day 2) -- apply exception on this day of the week. | [optional] 
**day3** | **bool** | Wednesday (day 3) -- apply exception on this day of the week. | [optional] 
**day4** | **bool** | Thursday (day 4) -- apply exception on this day of the week. | [optional] 
**day5** | **bool** | Friday (day 5) -- apply exception on this day of the week. | [optional] 
**day6** | **bool** | Saturday (day 6) -- apply exception on this day of the week. | [optional] 

## Example

```python
from cloudbeds_pms.models.policy_exception_interval_response_schema import PolicyExceptionIntervalResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyExceptionIntervalResponseSchema from a JSON string
policy_exception_interval_response_schema_instance = PolicyExceptionIntervalResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PolicyExceptionIntervalResponseSchema.to_json())

# convert the object into a dict
policy_exception_interval_response_schema_dict = policy_exception_interval_response_schema_instance.to_dict()
# create an instance of PolicyExceptionIntervalResponseSchema from a dict
policy_exception_interval_response_schema_from_dict = PolicyExceptionIntervalResponseSchema.from_dict(policy_exception_interval_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


