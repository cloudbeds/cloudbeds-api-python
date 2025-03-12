# GroupSingleRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Group ID. | 

## Example

```python
from cloudbeds_pms.models.group_single_request_schema import GroupSingleRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSingleRequestSchema from a JSON string
group_single_request_schema_instance = GroupSingleRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GroupSingleRequestSchema.to_json())

# convert the object into a dict
group_single_request_schema_dict = group_single_request_schema_instance.to_dict()
# create an instance of GroupSingleRequestSchema from a dict
group_single_request_schema_from_dict = GroupSingleRequestSchema.from_dict(group_single_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


