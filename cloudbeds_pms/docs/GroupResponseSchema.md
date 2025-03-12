# GroupResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**can_edit** | **bool** |  | [optional] 
**can_delete** | **bool** |  | [optional] 
**can_disable** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.group_response_schema import GroupResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupResponseSchema from a JSON string
group_response_schema_instance = GroupResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GroupResponseSchema.to_json())

# convert the object into a dict
group_response_schema_dict = group_response_schema_instance.to_dict()
# create an instance of GroupResponseSchema from a dict
group_response_schema_from_dict = GroupResponseSchema.from_dict(group_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


