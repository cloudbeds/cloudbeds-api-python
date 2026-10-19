# PatchUnitResponseSchema

Response for PATCH /rooms/v1/units/{unitId}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | [**UnitItemResponseSchema**](UnitItemResponseSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.patch_unit_response_schema import PatchUnitResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PatchUnitResponseSchema from a JSON string
patch_unit_response_schema_instance = PatchUnitResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PatchUnitResponseSchema.to_json())

# convert the object into a dict
patch_unit_response_schema_dict = patch_unit_response_schema_instance.to_dict()
# create an instance of PatchUnitResponseSchema from a dict
patch_unit_response_schema_from_dict = PatchUnitResponseSchema.from_dict(patch_unit_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


