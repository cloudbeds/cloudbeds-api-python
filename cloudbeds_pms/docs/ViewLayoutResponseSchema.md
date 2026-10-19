# ViewLayoutResponseSchema

A view resolved into a layout: every unit to draw, flat and in final render order, each naming its section; the ordered section index; and what was rendered.  The units are under `units` rather than the platform's `data`: this is not a collection of the resource in the path — it is one layout, whose parts happen to include units.  Deliberately unpaginated. A partial layout is not a layout: the calendar needs every row before it can draw one, so paging this would mean N requests before first paint. Bounded by construction instead — a stored view is capped on write, a built-in by the property's inventory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | [**List[UnitResponseSchema]**](UnitResponseSchema.md) | Units in final render order, each carrying its &#x60;sectionId&#x60;. | 
**sections** | [**List[SectionResponseSchema]**](SectionResponseSchema.md) | The ordered section index.  What it contains depends on how the view resolved. A view resolved from a stored definition ends with the uncategorized tail, always last and always present even when every unit is placed. The two derived built-ins have no tail: &#x60;accommodation-type&#x60; returns one section per unit type, and &#x60;alphabetical&#x60; returns a single band. Do not index off the last section to find the tail — match on &#x60;systemLabel&#x60;. | 
**meta** | [**LayoutMetaResponseSchema**](LayoutMetaResponseSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.view_layout_response_schema import ViewLayoutResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ViewLayoutResponseSchema from a JSON string
view_layout_response_schema_instance = ViewLayoutResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ViewLayoutResponseSchema.to_json())

# convert the object into a dict
view_layout_response_schema_dict = view_layout_response_schema_instance.to_dict()
# create an instance of ViewLayoutResponseSchema from a dict
view_layout_response_schema_from_dict = ViewLayoutResponseSchema.from_dict(view_layout_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


