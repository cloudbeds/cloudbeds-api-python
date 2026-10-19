# SetActiveRevisionRequestSchema

Which revision the view should serve.  The live revision belongs to the view, not to the revision, so this writes the view's pointer and copies no content: what an admin previewed is exactly what goes live. Any revision qualifies — naming an older one is the rollback — and naming the one already live changes nothing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **str** | The revision to make live. | 

## Example

```python
from cloudbeds_pms.models.set_active_revision_request_schema import SetActiveRevisionRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SetActiveRevisionRequestSchema from a JSON string
set_active_revision_request_schema_instance = SetActiveRevisionRequestSchema.from_json(json)
# print the JSON string representation of the object
print(SetActiveRevisionRequestSchema.to_json())

# convert the object into a dict
set_active_revision_request_schema_dict = set_active_revision_request_schema_instance.to_dict()
# create an instance of SetActiveRevisionRequestSchema from a dict
set_active_revision_request_schema_from_dict = SetActiveRevisionRequestSchema.from_dict(set_active_revision_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


