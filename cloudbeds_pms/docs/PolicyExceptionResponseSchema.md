# PolicyExceptionResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**property_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**policy_root_id** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**created_by** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**intervals** | [**List[PolicyExceptionIntervalResponseSchema]**](PolicyExceptionIntervalResponseSchema.md) |  | [optional] 
**rates** | [**List[PolicyExceptionRateResponseSchema]**](PolicyExceptionRateResponseSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.policy_exception_response_schema import PolicyExceptionResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyExceptionResponseSchema from a JSON string
policy_exception_response_schema_instance = PolicyExceptionResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PolicyExceptionResponseSchema.to_json())

# convert the object into a dict
policy_exception_response_schema_dict = policy_exception_response_schema_instance.to_dict()
# create an instance of PolicyExceptionResponseSchema from a dict
policy_exception_response_schema_from_dict = PolicyExceptionResponseSchema.from_dict(policy_exception_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


