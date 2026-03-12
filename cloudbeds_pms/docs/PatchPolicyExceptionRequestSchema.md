# PatchPolicyExceptionRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exception_id** | **str** | Policy exception ID. | 
**policy_root_id** | **int** | Smart policy root ID. | [optional] 
**intervals** | [**List[PolicyExceptionIntervalSchema]**](PolicyExceptionIntervalSchema.md) | List of date intervals for this exception. | [optional] 
**rates** | [**List[PolicyExceptionRateSchema]**](PolicyExceptionRateSchema.md) | List of rates this exception applies to. | [optional] 
**name** | **str** | Internal name for this exception. | [optional] 
**enabled** | **bool** | Whether the exception is enabled. | [optional] 

## Example

```python
from cloudbeds_pms.models.patch_policy_exception_request_schema import PatchPolicyExceptionRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPolicyExceptionRequestSchema from a JSON string
patch_policy_exception_request_schema_instance = PatchPolicyExceptionRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PatchPolicyExceptionRequestSchema.to_json())

# convert the object into a dict
patch_policy_exception_request_schema_dict = patch_policy_exception_request_schema_instance.to_dict()
# create an instance of PatchPolicyExceptionRequestSchema from a dict
patch_policy_exception_request_schema_from_dict = PatchPolicyExceptionRequestSchema.from_dict(patch_policy_exception_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


