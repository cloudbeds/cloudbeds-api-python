# AgePolicyResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**config** | **str** |  | 
**provides_cribs** | **bool** |  | 
**custom_label** | **str** |  | [optional] 
**extra_guests_config** | **str** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.age_policy_response_schema import AgePolicyResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AgePolicyResponseSchema from a JSON string
age_policy_response_schema_instance = AgePolicyResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AgePolicyResponseSchema.to_json())

# convert the object into a dict
age_policy_response_schema_dict = age_policy_response_schema_instance.to_dict()
# create an instance of AgePolicyResponseSchema from a dict
age_policy_response_schema_from_dict = AgePolicyResponseSchema.from_dict(age_policy_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


