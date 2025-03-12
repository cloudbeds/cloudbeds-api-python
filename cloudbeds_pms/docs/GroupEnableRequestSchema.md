# GroupEnableRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Group ID. | 

## Example

```python
from cloudbeds_pms.models.group_enable_request_schema import GroupEnableRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupEnableRequestSchema from a JSON string
group_enable_request_schema_instance = GroupEnableRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GroupEnableRequestSchema.to_json())

# convert the object into a dict
group_enable_request_schema_dict = group_enable_request_schema_instance.to_dict()
# create an instance of GroupEnableRequestSchema from a dict
group_enable_request_schema_from_dict = GroupEnableRequestSchema.from_dict(group_enable_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


