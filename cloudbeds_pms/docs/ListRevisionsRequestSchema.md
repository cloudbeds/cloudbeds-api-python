# ListRevisionsRequestSchema

Listing a view's revisions. Metadata only — no definition content is decoded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_id** | **str** | The view whose revisions to list. | 

## Example

```python
from cloudbeds_pms.models.list_revisions_request_schema import ListRevisionsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ListRevisionsRequestSchema from a JSON string
list_revisions_request_schema_instance = ListRevisionsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ListRevisionsRequestSchema.to_json())

# convert the object into a dict
list_revisions_request_schema_dict = list_revisions_request_schema_instance.to_dict()
# create an instance of ListRevisionsRequestSchema from a dict
list_revisions_request_schema_from_dict = ListRevisionsRequestSchema.from_dict(list_revisions_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


