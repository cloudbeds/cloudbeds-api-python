# PutRoomTypeAreasRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout_type_code** | **str** | Layout type: SINGLE (1 area) or MULTI (2+ areas). Set to null to clear all areas configuration. | 
**areas** | [**List[AreaItemSchema]**](AreaItemSchema.md) | List of areas for this room type. Must be empty when layoutTypeCode is null. Must have at least 1 area when layoutTypeCode is not null. | 

## Example

```python
from cloudbeds_pms.models.put_room_type_areas_request_schema import PutRoomTypeAreasRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PutRoomTypeAreasRequestSchema from a JSON string
put_room_type_areas_request_schema_instance = PutRoomTypeAreasRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PutRoomTypeAreasRequestSchema.to_json())

# convert the object into a dict
put_room_type_areas_request_schema_dict = put_room_type_areas_request_schema_instance.to_dict()
# create an instance of PutRoomTypeAreasRequestSchema from a dict
put_room_type_areas_request_schema_from_dict = PutRoomTypeAreasRequestSchema.from_dict(put_room_type_areas_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


