# AgePolicyCreateRequestSchemaGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_type** | **str** | Age group type. Must be one of the valid age group types. | 
**min_age** | **int** | Minimum age for this age group. | 
**max_age** | **int** | Maximum age for this age group. | [optional] 

## Example

```python
from cloudbeds_pms.models.age_policy_create_request_schema_groups_inner import AgePolicyCreateRequestSchemaGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AgePolicyCreateRequestSchemaGroupsInner from a JSON string
age_policy_create_request_schema_groups_inner_instance = AgePolicyCreateRequestSchemaGroupsInner.from_json(json)
# print the JSON string representation of the object
print(AgePolicyCreateRequestSchemaGroupsInner.to_json())

# convert the object into a dict
age_policy_create_request_schema_groups_inner_dict = age_policy_create_request_schema_groups_inner_instance.to_dict()
# create an instance of AgePolicyCreateRequestSchemaGroupsInner from a dict
age_policy_create_request_schema_groups_inner_from_dict = AgePolicyCreateRequestSchemaGroupsInner.from_dict(age_policy_create_request_schema_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


