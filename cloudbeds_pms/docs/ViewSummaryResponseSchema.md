# ViewSummaryResponseSchema

One entry in the view picker.  A view with no `publishedRevision` has nothing active: it is out of the picker for everyone but an admin, which is how a view is put away. `latestRevision` above `publishedRevision` means an admin has work staged ahead of what is live.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Either a reserved built-in id (&#x60;accommodation-type&#x60;, &#x60;alphabetical&#x60;) or a stored key. | 
**name** | **str** | Display name. For a built-in the property has not customized this is server-generated English — localize it from &#x60;systemLabel&#x60; instead of showing it verbatim. | 
**is_default** | **bool** | Whether this is the default view and the client&#39;s fallback target. | 
**published_revision** | **str** | The active revision. Absent when nothing is published — a derived built-in, or a view that has been put away. | [optional] 
**latest_revision** | **str** | Highest revision that exists. Above &#x60;publishedRevision&#x60; when work is staged ahead of what is live. | [optional] 
**modified** | **datetime** | When the view last changed. | [optional] 
**system_label** | **str** | Token for a built-in view&#39;s server-generated name, so the client can localize it. Absent for a stored view and for a customized built-in, whose names the admin typed. &#x60;name&#x60; carries the English fallback. | [optional] 

## Example

```python
from cloudbeds_pms.models.view_summary_response_schema import ViewSummaryResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ViewSummaryResponseSchema from a JSON string
view_summary_response_schema_instance = ViewSummaryResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ViewSummaryResponseSchema.to_json())

# convert the object into a dict
view_summary_response_schema_dict = view_summary_response_schema_instance.to_dict()
# create an instance of ViewSummaryResponseSchema from a dict
view_summary_response_schema_from_dict = ViewSummaryResponseSchema.from_dict(view_summary_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


