# RoomTypeAvailabilityResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **int** |  | 
**room_type_name** | **str** |  | 
**max_guests** | **int** |  | 
**rooms_available** | **int** | Minimum rooms available across all dates | 
**min_rate** | **float** | Lowest nightly rate across the date range | 
**max_rate** | **float** | Highest nightly rate across the date range | 

## Example

```python
from cloudbeds_pms.models.room_type_availability_response_schema import RoomTypeAvailabilityResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTypeAvailabilityResponseSchema from a JSON string
room_type_availability_response_schema_instance = RoomTypeAvailabilityResponseSchema.from_json(json)
# print the JSON string representation of the object
print(RoomTypeAvailabilityResponseSchema.to_json())

# convert the object into a dict
room_type_availability_response_schema_dict = room_type_availability_response_schema_instance.to_dict()
# create an instance of RoomTypeAvailabilityResponseSchema from a dict
room_type_availability_response_schema_from_dict = RoomTypeAvailabilityResponseSchema.from_dict(room_type_availability_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


