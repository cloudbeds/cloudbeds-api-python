# DeletePolicyExceptionRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exception_id** | **str** | Policy exception ID. | 

## Example

```python
from cloudbeds_pms.models.delete_policy_exception_request_schema import DeletePolicyExceptionRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePolicyExceptionRequestSchema from a JSON string
delete_policy_exception_request_schema_instance = DeletePolicyExceptionRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DeletePolicyExceptionRequestSchema.to_json())

# convert the object into a dict
delete_policy_exception_request_schema_dict = delete_policy_exception_request_schema_instance.to_dict()
# create an instance of DeletePolicyExceptionRequestSchema from a dict
delete_policy_exception_request_schema_from_dict = DeletePolicyExceptionRequestSchema.from_dict(delete_policy_exception_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


