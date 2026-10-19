# RevisionResponseSchema

Revision metadata — no definition content, which is why listing revisions never decodes the layout blobs.  `status` is immutable history: a revision stamped `published` was live at some point, whether or not it is the active one now. Which revision is live is the view's active-revision pointer.  The revision number is this resource's `id` — an item in `/revisions` is identified by `id`, not by a field repeating the resource name — and it is a string, as every numeric identifier is.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Revision number, from a monotonic per-view counter. Never reused, so a discard leaves a gap and an old preview link cannot come to point at new content. | 
**name** | **str** | The view&#39;s name as of this revision. Names are versioned with the layout, so a rename staged in a draft shows here before it reaches the picker. | 
**status** | **str** | Whether this revision has ever been published. History, not state: a revision that was taken down keeps it. What is live now is the view&#39;s active revision. | 
**created** | **datetime** | When the revision was stamped. | 
**created_by** | **str** | User who stamped it. | [optional] 

## Example

```python
from cloudbeds_pms.models.revision_response_schema import RevisionResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RevisionResponseSchema from a JSON string
revision_response_schema_instance = RevisionResponseSchema.from_json(json)
# print the JSON string representation of the object
print(RevisionResponseSchema.to_json())

# convert the object into a dict
revision_response_schema_dict = revision_response_schema_instance.to_dict()
# create an instance of RevisionResponseSchema from a dict
revision_response_schema_from_dict = RevisionResponseSchema.from_dict(revision_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


