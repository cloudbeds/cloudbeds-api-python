# UnitResponseSchema

One unit — a space that can be filled. Identity and structure only; volatile per-day state (housekeeping, busy/free) lives on the existing state endpoints.  `restrictions` and `relations` are `required` so an empty one serializes as `[]` rather than being dropped: a client reading `unit.relations` must never meet an undefined.  `sectionId` is always present: a unit only crosses the wire as part of a layout, and a unit in a layout always renders under exactly one section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | PMS room identifier. | 
**name** | **str** | Server-resolved display name. | 
**kind** | **str** | &#x60;standard&#x60;: a room in its own right. &#x60;dorm&#x60;: a shared unit whose beds sell individually — a structural row, not inventory. &#x60;bed&#x60;: an individually sellable bed. &#x60;virtual&#x60;: a space composed of other units. | 
**unit_type_id** | **str** | Accommodation type this unit belongs to. | 
**restrictions** | [**List[UnitRestrictionResponseSchema]**](UnitRestrictionResponseSchema.md) | What the unit restricts, e.g. dorm gender. A mixed dorm carries no entry — absence already means anyone. | 
**relations** | [**List[UnitRelationResponseSchema]**](UnitRelationResponseSchema.md) | Structural links: &#x60;part_of&#x60; (bed to its dorm) and &#x60;composed_of&#x60; (virtual to each physical component). | 
**section_id** | **str** | The section this unit renders under. | 

## Example

```python
from cloudbeds_pms.models.unit_response_schema import UnitResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UnitResponseSchema from a JSON string
unit_response_schema_instance = UnitResponseSchema.from_json(json)
# print the JSON string representation of the object
print(UnitResponseSchema.to_json())

# convert the object into a dict
unit_response_schema_dict = unit_response_schema_instance.to_dict()
# create an instance of UnitResponseSchema from a dict
unit_response_schema_from_dict = UnitResponseSchema.from_dict(unit_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


