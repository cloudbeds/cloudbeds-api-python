# ViewDetailResponseSchema

A stored view's definition at one revision — what the builder edits, and symmetric with the save.  `unresolvedUnitIds` is computed at read time: saved ids the current catalog can no longer resolve, because the unit was deactivated or re-typed (re-typing mints a new id). They stay in `sections` verbatim and are flagged here rather than dropped, so a read/modify/write cycle cannot silently delete units that may come back.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The view id. | 
**name** | **str** | Display name. | 
**revision** | **str** | The revision this definition is from. | 
**status** | **str** | Status of this revision. | 
**sections** | [**List[DefinitionSectionResponseSchema]**](DefinitionSectionResponseSchema.md) | Sections in order. The uncategorized tail is computed at render time and is not stored here. | 
**published_revision** | **str** | The active revision, if any. | [optional] 
**created** | **datetime** | When the view was created. | [optional] 
**modified** | **datetime** | When this revision was stamped. | [optional] 
**created_by** | **str** | User who created the view. | [optional] 
**unresolved_unit_ids** | **List[str]** | Saved unit ids the current catalog cannot resolve. Absent when every id still resolves. | [optional] 

## Example

```python
from cloudbeds_pms.models.view_detail_response_schema import ViewDetailResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ViewDetailResponseSchema from a JSON string
view_detail_response_schema_instance = ViewDetailResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ViewDetailResponseSchema.to_json())

# convert the object into a dict
view_detail_response_schema_dict = view_detail_response_schema_instance.to_dict()
# create an instance of ViewDetailResponseSchema from a dict
view_detail_response_schema_from_dict = ViewDetailResponseSchema.from_dict(view_detail_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


