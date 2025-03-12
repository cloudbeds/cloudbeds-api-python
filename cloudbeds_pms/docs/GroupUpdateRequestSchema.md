# GroupUpdateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Group ID. | 
**name** | **str** | Group name. | 
**code** | **str** | Group code. | 
**description** | **str** | Group description. | 

## Example

```python
from cloudbeds_pms.models.group_update_request_schema import GroupUpdateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupUpdateRequestSchema from a JSON string
group_update_request_schema_instance = GroupUpdateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GroupUpdateRequestSchema.to_json())

# convert the object into a dict
group_update_request_schema_dict = group_update_request_schema_instance.to_dict()
# create an instance of GroupUpdateRequestSchema from a dict
group_update_request_schema_from_dict = GroupUpdateRequestSchema.from_dict(group_update_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


