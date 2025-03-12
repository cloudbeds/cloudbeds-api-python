# GroupListResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**data** | [**List[GroupResponseSchema]**](GroupResponseSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.group_list_response_schema import GroupListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupListResponseSchema from a JSON string
group_list_response_schema_instance = GroupListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GroupListResponseSchema.to_json())

# convert the object into a dict
group_list_response_schema_dict = group_list_response_schema_instance.to_dict()
# create an instance of GroupListResponseSchema from a dict
group_list_response_schema_from_dict = GroupListResponseSchema.from_dict(group_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


