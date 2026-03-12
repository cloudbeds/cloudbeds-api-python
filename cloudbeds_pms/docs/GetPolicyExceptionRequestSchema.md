# GetPolicyExceptionRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exception_id** | **str** | Policy exception ID. | 

## Example

```python
from cloudbeds_pms.models.get_policy_exception_request_schema import GetPolicyExceptionRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyExceptionRequestSchema from a JSON string
get_policy_exception_request_schema_instance = GetPolicyExceptionRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GetPolicyExceptionRequestSchema.to_json())

# convert the object into a dict
get_policy_exception_request_schema_dict = get_policy_exception_request_schema_instance.to_dict()
# create an instance of GetPolicyExceptionRequestSchema from a dict
get_policy_exception_request_schema_from_dict = GetPolicyExceptionRequestSchema.from_dict(get_policy_exception_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


