# UnitItemResponseSchema

A single unit (room) within an accommodation type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unit ID | 
**property_id** | **int** | Property ID | 
**room_type_id** | **int** | Room type (accommodation) ID | 
**name** | **str** | Unit name | 
**connecting_unit_ids** | **List[str]** | IDs of connecting units | 
**description** | **str** | Unit description | 
**images** | **List[object]** | Unit images (JSON objects as stored on the unit). | 
**name_langs** | **Dict[str, str]** | Per-language unit name map (IETF language codes → localized strings). | 
**description_langs** | **Dict[str, str]** | Per-language unit description map (IETF language codes → localized strings). | 
**doorlock_id** | **str** | Door lock integration identifier. | 

## Example

```python
from cloudbeds_pms.models.unit_item_response_schema import UnitItemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UnitItemResponseSchema from a JSON string
unit_item_response_schema_instance = UnitItemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(UnitItemResponseSchema.to_json())

# convert the object into a dict
unit_item_response_schema_dict = unit_item_response_schema_instance.to_dict()
# create an instance of UnitItemResponseSchema from a dict
unit_item_response_schema_from_dict = UnitItemResponseSchema.from_dict(unit_item_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


