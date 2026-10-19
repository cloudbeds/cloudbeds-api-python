# UnitRestrictionResponseSchema

Generic `{type, value}` so a new restriction kind is a new value, not a new shape.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Restriction kind. | 
**value** | **str** | Restriction value. | 

## Example

```python
from cloudbeds_pms.models.unit_restriction_response_schema import UnitRestrictionResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UnitRestrictionResponseSchema from a JSON string
unit_restriction_response_schema_instance = UnitRestrictionResponseSchema.from_json(json)
# print the JSON string representation of the object
print(UnitRestrictionResponseSchema.to_json())

# convert the object into a dict
unit_restriction_response_schema_dict = unit_restriction_response_schema_instance.to_dict()
# create an instance of UnitRestrictionResponseSchema from a dict
unit_restriction_response_schema_from_dict = UnitRestrictionResponseSchema.from_dict(unit_restriction_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


