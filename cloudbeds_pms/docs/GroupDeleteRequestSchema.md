# GroupDeleteRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Group ID. | 

## Example

```python
from cloudbeds_pms.models.group_delete_request_schema import GroupDeleteRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDeleteRequestSchema from a JSON string
group_delete_request_schema_instance = GroupDeleteRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GroupDeleteRequestSchema.to_json())

# convert the object into a dict
group_delete_request_schema_dict = group_delete_request_schema_instance.to_dict()
# create an instance of GroupDeleteRequestSchema from a dict
group_delete_request_schema_from_dict = GroupDeleteRequestSchema.from_dict(group_delete_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


