# AgePolicyUpdateRequestSchemaGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Age group ID. | [optional] 
**group_type** | **str** | Age group type. Must be one of the valid age group types. | 
**min_age** | **int** | Minimum age for this age group. | 
**max_age** | **int** | Maximum age for this age group. | [optional] 
**apply_rate_from_id** | **str** | Apply rate from age group ID. | [optional] 

## Example

```python
from cloudbeds_pms.models.age_policy_update_request_schema_groups_inner import AgePolicyUpdateRequestSchemaGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AgePolicyUpdateRequestSchemaGroupsInner from a JSON string
age_policy_update_request_schema_groups_inner_instance = AgePolicyUpdateRequestSchemaGroupsInner.from_json(json)
# print the JSON string representation of the object
print(AgePolicyUpdateRequestSchemaGroupsInner.to_json())

# convert the object into a dict
age_policy_update_request_schema_groups_inner_dict = age_policy_update_request_schema_groups_inner_instance.to_dict()
# create an instance of AgePolicyUpdateRequestSchemaGroupsInner from a dict
age_policy_update_request_schema_groups_inner_from_dict = AgePolicyUpdateRequestSchemaGroupsInner.from_dict(age_policy_update_request_schema_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


