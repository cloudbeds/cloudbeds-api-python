# DeleteViewRequestSchema

Deleting a view. On a built-in this deletes the property's customization rather than the view: the id reverts to its derived layout and keeps working, which is why a reserved id is accepted here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_id** | **str** | The view to delete. | 

## Example

```python
from cloudbeds_pms.models.delete_view_request_schema import DeleteViewRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteViewRequestSchema from a JSON string
delete_view_request_schema_instance = DeleteViewRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DeleteViewRequestSchema.to_json())

# convert the object into a dict
delete_view_request_schema_dict = delete_view_request_schema_instance.to_dict()
# create an instance of DeleteViewRequestSchema from a dict
delete_view_request_schema_from_dict = DeleteViewRequestSchema.from_dict(delete_view_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


