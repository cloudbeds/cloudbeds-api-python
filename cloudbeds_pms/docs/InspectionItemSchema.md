# InspectionItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_date** | **str** |  | 
**room_type_id** | **str** |  | 
**room_id** | **str** |  | 
**room_condition** | **str** |  | 
**room_occupied** | **bool** |  | [optional] 
**room_blocked** | **bool** |  | 
**frontdesk_status** | **str** |  | 
**housekeeper_id** | **str** |  | 
**do_not_disturb** | **bool** |  | 
**refused_service** | **bool** |  | 
**vacant_pickup** | **bool** |  | 
**room_note** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.inspection_item_schema import InspectionItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionItemSchema from a JSON string
inspection_item_schema_instance = InspectionItemSchema.from_json(json)
# print the JSON string representation of the object
print(InspectionItemSchema.to_json())

# convert the object into a dict
inspection_item_schema_dict = inspection_item_schema_instance.to_dict()
# create an instance of InspectionItemSchema from a dict
inspection_item_schema_from_dict = InspectionItemSchema.from_dict(inspection_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


