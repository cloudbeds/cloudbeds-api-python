# ClearActiveRevisionRequestSchema

Taking a view down: clears the live revision, leaving nothing published.  Revisions and their publish history survive, so the view can be brought back by making one live again. On a customized built-in, clearing the pointer is the revert-to-default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_id** | **str** | The view to take down. | 

## Example

```python
from cloudbeds_pms.models.clear_active_revision_request_schema import ClearActiveRevisionRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ClearActiveRevisionRequestSchema from a JSON string
clear_active_revision_request_schema_instance = ClearActiveRevisionRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ClearActiveRevisionRequestSchema.to_json())

# convert the object into a dict
clear_active_revision_request_schema_dict = clear_active_revision_request_schema_instance.to_dict()
# create an instance of ClearActiveRevisionRequestSchema from a dict
clear_active_revision_request_schema_from_dict = ClearActiveRevisionRequestSchema.from_dict(clear_active_revision_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


