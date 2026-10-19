# AreaItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Area type code. Valid values: BEDROOM, LIVING_ROOM (for MULTI layout), SLEEPING_AREA (for SINGLE layout) | 
**position** | **int** | Position/order of this area | 
**arrangements** | [**List[ArrangementItemSchema]**](ArrangementItemSchema.md) | List of bed arrangements in this area. BEDROOM and SLEEPING_AREA require exactly 1 default arrangement (isDefault&#x3D;true); LIVING_ROOM can have 0 to 2. An optional second arrangement with isDefault&#x3D;false represents the alternative sleeping arrangement. | 

## Example

```python
from cloudbeds_pms.models.area_item_schema import AreaItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AreaItemSchema from a JSON string
area_item_schema_instance = AreaItemSchema.from_json(json)
# print the JSON string representation of the object
print(AreaItemSchema.to_json())

# convert the object into a dict
area_item_schema_dict = area_item_schema_instance.to_dict()
# create an instance of AreaItemSchema from a dict
area_item_schema_from_dict = AreaItemSchema.from_dict(area_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


