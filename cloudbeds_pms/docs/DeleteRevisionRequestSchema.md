# DeleteRevisionRequestSchema

Discarding a draft an admin tried and rejected. Only drafts are deletable — the active revision, published history and a view's last remaining revision refuse with `REVISION_NOT_DELETABLE`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_id** | **str** | The view the revision belongs to. | 
**revision** | **str** | The draft revision to discard. | 

## Example

```python
from cloudbeds_pms.models.delete_revision_request_schema import DeleteRevisionRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRevisionRequestSchema from a JSON string
delete_revision_request_schema_instance = DeleteRevisionRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DeleteRevisionRequestSchema.to_json())

# convert the object into a dict
delete_revision_request_schema_dict = delete_revision_request_schema_instance.to_dict()
# create an instance of DeleteRevisionRequestSchema from a dict
delete_revision_request_schema_from_dict = DeleteRevisionRequestSchema.from_dict(delete_revision_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


