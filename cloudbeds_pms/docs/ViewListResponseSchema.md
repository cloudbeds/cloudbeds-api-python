# ViewListResponseSchema

The property's views. Unpaginated: two built-ins plus at most five stored keys, so the collection is bounded at seven by the model itself rather than by a page size.  A caller with the manage permission additionally sees views with nothing published; everyone else sees only what is live.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ViewSummaryResponseSchema]**](ViewSummaryResponseSchema.md) | View summaries, built-ins first. | 

## Example

```python
from cloudbeds_pms.models.view_list_response_schema import ViewListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ViewListResponseSchema from a JSON string
view_list_response_schema_instance = ViewListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ViewListResponseSchema.to_json())

# convert the object into a dict
view_list_response_schema_dict = view_list_response_schema_instance.to_dict()
# create an instance of ViewListResponseSchema from a dict
view_list_response_schema_from_dict = ViewListResponseSchema.from_dict(view_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


