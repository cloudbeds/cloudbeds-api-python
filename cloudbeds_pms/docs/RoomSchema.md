# RoomSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | Room type ID for per-room-type tax filtering | [optional] 
**start_date** | **str** | Check-in date (YYYY-MM-DD) | 
**end_date** | **str** | Check-out date (YYYY-MM-DD) | 
**adults** | **int** | Number of adults (&gt;&#x3D; 1) | 
**children** | **int** | Number of children (&gt;&#x3D; 0) | 
**rate_id** | **str** | Rate plan ID (context only) | [optional] 
**detailed_rates** | [**List[DetailedRateSchema]**](DetailedRateSchema.md) | Per-night rate breakdown. One entry per night of the stay. | 
**addons** | [**List[AddonSchema]**](AddonSchema.md) | Add-ons to include in calculation | [optional] 

## Example

```python
from cloudbeds_pms.models.room_schema import RoomSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RoomSchema from a JSON string
room_schema_instance = RoomSchema.from_json(json)
# print the JSON string representation of the object
print(RoomSchema.to_json())

# convert the object into a dict
room_schema_dict = room_schema_instance.to_dict()
# create an instance of RoomSchema from a dict
room_schema_from_dict = RoomSchema.from_dict(room_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


