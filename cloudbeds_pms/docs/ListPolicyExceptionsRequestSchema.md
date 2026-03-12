# ListPolicyExceptionsRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit for the number of items to return (max 500) | [optional] [default to 100]
**offset** | **int** | The offset for the current page of results | [optional] [default to 0]
**sort** | [**SortSchema**](SortSchema.md) |  | [optional] 
**policy_root_id** | **str** | Filter by smart policy root ID. | [optional] 

## Example

```python
from cloudbeds_pms.models.list_policy_exceptions_request_schema import ListPolicyExceptionsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ListPolicyExceptionsRequestSchema from a JSON string
list_policy_exceptions_request_schema_instance = ListPolicyExceptionsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ListPolicyExceptionsRequestSchema.to_json())

# convert the object into a dict
list_policy_exceptions_request_schema_dict = list_policy_exceptions_request_schema_instance.to_dict()
# create an instance of ListPolicyExceptionsRequestSchema from a dict
list_policy_exceptions_request_schema_from_dict = ListPolicyExceptionsRequestSchema.from_dict(list_policy_exceptions_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


