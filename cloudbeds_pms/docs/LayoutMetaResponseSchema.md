# LayoutMetaResponseSchema

What was rendered and how much of it. `revision`/`status` appear only for a view resolved from a stored revision — their absence is how a client tells a derived built-in from a materialized one, without a discriminator field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_id** | **str** | The view this layout was resolved from. | 
**total_units** | **int** | Sellable spaces in the property. A dorm container is a structural row and is not counted; each of its beds is. | 
**hidden_units** | **int** | Units the filters removed from this response. | 
**filters_applied** | **bool** | Whether any filter was applied. | 
**revision** | **str** | Revision rendered. Absent when the view resolved to its derived layout. | [optional] 
**status** | **str** | Status of the rendered revision. Absent alongside &#x60;revision&#x60;. | [optional] 
**focused_date** | **date** | Echo of the &#x60;date&#x60; the filters were evaluated against. Present only when a day-scoped filter ran. | [optional] 

## Example

```python
from cloudbeds_pms.models.layout_meta_response_schema import LayoutMetaResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LayoutMetaResponseSchema from a JSON string
layout_meta_response_schema_instance = LayoutMetaResponseSchema.from_json(json)
# print the JSON string representation of the object
print(LayoutMetaResponseSchema.to_json())

# convert the object into a dict
layout_meta_response_schema_dict = layout_meta_response_schema_instance.to_dict()
# create an instance of LayoutMetaResponseSchema from a dict
layout_meta_response_schema_from_dict = LayoutMetaResponseSchema.from_dict(layout_meta_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


