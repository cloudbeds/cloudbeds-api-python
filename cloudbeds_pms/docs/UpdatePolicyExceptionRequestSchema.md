# UpdatePolicyExceptionRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exception_id** | **str** | Policy exception ID. | 
**policy_root_id** | **int** | Smart policy root ID. | 
**intervals** | [**List[PolicyExceptionIntervalSchema]**](PolicyExceptionIntervalSchema.md) | List of date intervals for this exception. | 
**rates** | [**List[PolicyExceptionRateSchema]**](PolicyExceptionRateSchema.md) | List of rates this exception applies to. | 
**name** | **str** | Internal name for this exception. | 
**enabled** | **bool** | Whether the exception is enabled. Omit to preserve current value. | [optional] 

## Example

```python
from cloudbeds_pms.models.update_policy_exception_request_schema import UpdatePolicyExceptionRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePolicyExceptionRequestSchema from a JSON string
update_policy_exception_request_schema_instance = UpdatePolicyExceptionRequestSchema.from_json(json)
# print the JSON string representation of the object
print(UpdatePolicyExceptionRequestSchema.to_json())

# convert the object into a dict
update_policy_exception_request_schema_dict = update_policy_exception_request_schema_instance.to_dict()
# create an instance of UpdatePolicyExceptionRequestSchema from a dict
update_policy_exception_request_schema_from_dict = UpdatePolicyExceptionRequestSchema.from_dict(update_policy_exception_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


