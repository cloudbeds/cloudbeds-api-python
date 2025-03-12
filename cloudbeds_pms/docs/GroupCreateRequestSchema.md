# GroupCreateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Group name. | 
**code** | **str** | Group code. | 
**description** | **str** | Group description. | 

## Example

```python
from cloudbeds_pms.models.group_create_request_schema import GroupCreateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCreateRequestSchema from a JSON string
group_create_request_schema_instance = GroupCreateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GroupCreateRequestSchema.to_json())

# convert the object into a dict
group_create_request_schema_dict = group_create_request_schema_instance.to_dict()
# create an instance of GroupCreateRequestSchema from a dict
group_create_request_schema_from_dict = GroupCreateRequestSchema.from_dict(group_create_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


