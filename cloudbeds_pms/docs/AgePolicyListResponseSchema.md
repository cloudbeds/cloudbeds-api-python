# AgePolicyListResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AgePolicyResponseSchema]**](AgePolicyResponseSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.age_policy_list_response_schema import AgePolicyListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AgePolicyListResponseSchema from a JSON string
age_policy_list_response_schema_instance = AgePolicyListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AgePolicyListResponseSchema.to_json())

# convert the object into a dict
age_policy_list_response_schema_dict = age_policy_list_response_schema_instance.to_dict()
# create an instance of AgePolicyListResponseSchema from a dict
age_policy_list_response_schema_from_dict = AgePolicyListResponseSchema.from_dict(age_policy_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


