# CreateRevisionRequestSchema

Saving a new revision under an existing view id. Existing revisions are never mutated — the id is the stable key, the revisions are immutable content.  `baseRevision` is the optimistic-concurrency assertion and must equal the view's latest revision. `baseRevision: 0` asserts the view has no stored revision yet, which is how a built-in is materialized in place: the same id starts fronting a stored definition, so preferences and shared links keep working. Against an already-stored view that is a 409.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for the view. | 
**sections** | [**List[DefinitionSectionRequestSchema]**](DefinitionSectionRequestSchema.md) | Sections in order, replacing the previous revision&#39;s wholesale. | 
**base_revision** | **str** | The revision this save is based on. Must equal the view&#39;s latest revision; &#x60;\&quot;0\&quot;&#x60; asserts none exists yet and materializes a built-in. | 
**status** | **str** | Status of the new revision. | [optional] [default to 'draft']

## Example

```python
from cloudbeds_pms.models.create_revision_request_schema import CreateRevisionRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRevisionRequestSchema from a JSON string
create_revision_request_schema_instance = CreateRevisionRequestSchema.from_json(json)
# print the JSON string representation of the object
print(CreateRevisionRequestSchema.to_json())

# convert the object into a dict
create_revision_request_schema_dict = create_revision_request_schema_instance.to_dict()
# create an instance of CreateRevisionRequestSchema from a dict
create_revision_request_schema_from_dict = CreateRevisionRequestSchema.from_dict(create_revision_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


