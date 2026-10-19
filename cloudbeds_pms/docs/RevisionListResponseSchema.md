# RevisionListResponseSchema

A view's revisions, newest first. Unpaginated: retention keeps at most the three newest published revisions, but drafts staged ahead of the live revision are never swept — so what actually bounds this collection is the ceiling of 50 revisions per view, enforced on save.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RevisionResponseSchema]**](RevisionResponseSchema.md) | Revision metadata, newest first. | 

## Example

```python
from cloudbeds_pms.models.revision_list_response_schema import RevisionListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RevisionListResponseSchema from a JSON string
revision_list_response_schema_instance = RevisionListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(RevisionListResponseSchema.to_json())

# convert the object into a dict
revision_list_response_schema_dict = revision_list_response_schema_instance.to_dict()
# create an instance of RevisionListResponseSchema from a dict
revision_list_response_schema_from_dict = RevisionListResponseSchema.from_dict(revision_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


