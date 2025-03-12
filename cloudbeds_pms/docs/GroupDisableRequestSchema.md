# GroupDisableRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Group ID. | 

## Example

```python
from cloudbeds_pms.models.group_disable_request_schema import GroupDisableRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDisableRequestSchema from a JSON string
group_disable_request_schema_instance = GroupDisableRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GroupDisableRequestSchema.to_json())

# convert the object into a dict
group_disable_request_schema_dict = group_disable_request_schema_instance.to_dict()
# create an instance of GroupDisableRequestSchema from a dict
group_disable_request_schema_from_dict = GroupDisableRequestSchema.from_dict(group_disable_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


