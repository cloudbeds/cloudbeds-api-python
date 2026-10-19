# GetViewRequestSchema

Reading a stored view's definition — what the builder edits.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_id** | **str** | The view whose definition to read. | 

## Example

```python
from cloudbeds_pms.models.get_view_request_schema import GetViewRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetViewRequestSchema from a JSON string
get_view_request_schema_instance = GetViewRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GetViewRequestSchema.to_json())

# convert the object into a dict
get_view_request_schema_dict = get_view_request_schema_instance.to_dict()
# create an instance of GetViewRequestSchema from a dict
get_view_request_schema_from_dict = GetViewRequestSchema.from_dict(get_view_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


