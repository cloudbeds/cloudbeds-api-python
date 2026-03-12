# CreatePolicyExceptionRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_root_id** | **int** | Smart policy root ID. | 
**intervals** | [**List[PolicyExceptionIntervalSchema]**](PolicyExceptionIntervalSchema.md) | List of date intervals for this exception. | 
**rates** | [**List[PolicyExceptionRateSchema]**](PolicyExceptionRateSchema.md) | List of rates this exception applies to. | 
**name** | **str** | Internal name for this exception. | 
**enabled** | **bool** | Whether the exception is enabled. | [optional] 

## Example

```python
from cloudbeds_pms.models.create_policy_exception_request_schema import CreatePolicyExceptionRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePolicyExceptionRequestSchema from a JSON string
create_policy_exception_request_schema_instance = CreatePolicyExceptionRequestSchema.from_json(json)
# print the JSON string representation of the object
print(CreatePolicyExceptionRequestSchema.to_json())

# convert the object into a dict
create_policy_exception_request_schema_dict = create_policy_exception_request_schema_instance.to_dict()
# create an instance of CreatePolicyExceptionRequestSchema from a dict
create_policy_exception_request_schema_from_dict = CreatePolicyExceptionRequestSchema.from_dict(create_policy_exception_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


