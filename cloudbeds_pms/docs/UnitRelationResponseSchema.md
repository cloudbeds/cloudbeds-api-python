# UnitRelationResponseSchema

Generic `{type, unitId}` so a new relation kind is a new value, not a new shape.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Relation kind. | 
**unit_id** | **str** | The related unit. | 

## Example

```python
from cloudbeds_pms.models.unit_relation_response_schema import UnitRelationResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UnitRelationResponseSchema from a JSON string
unit_relation_response_schema_instance = UnitRelationResponseSchema.from_json(json)
# print the JSON string representation of the object
print(UnitRelationResponseSchema.to_json())

# convert the object into a dict
unit_relation_response_schema_dict = unit_relation_response_schema_instance.to_dict()
# create an instance of UnitRelationResponseSchema from a dict
unit_relation_response_schema_from_dict = UnitRelationResponseSchema.from_dict(unit_relation_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


