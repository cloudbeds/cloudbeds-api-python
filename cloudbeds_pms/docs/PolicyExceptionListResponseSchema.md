# PolicyExceptionListResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit for the number of items to return. | 
**offset** | **int** | The offset for the current page of results. | 
**data** | [**List[PolicyExceptionResponseSchema]**](PolicyExceptionResponseSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.policy_exception_list_response_schema import PolicyExceptionListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyExceptionListResponseSchema from a JSON string
policy_exception_list_response_schema_instance = PolicyExceptionListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PolicyExceptionListResponseSchema.to_json())

# convert the object into a dict
policy_exception_list_response_schema_dict = policy_exception_list_response_schema_instance.to_dict()
# create an instance of PolicyExceptionListResponseSchema from a dict
policy_exception_list_response_schema_from_dict = PolicyExceptionListResponseSchema.from_dict(policy_exception_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


