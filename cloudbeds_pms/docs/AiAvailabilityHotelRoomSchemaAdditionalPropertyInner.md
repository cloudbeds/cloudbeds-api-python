# AiAvailabilityHotelRoomSchemaAdditionalPropertyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**value** | [**AiAvailabilityHotelRoomSchemaAdditionalPropertyInnerValue**](AiAvailabilityHotelRoomSchemaAdditionalPropertyInnerValue.md) |  | 

## Example

```python
from cloudbeds_pms.models.ai_availability_hotel_room_schema_additional_property_inner import AiAvailabilityHotelRoomSchemaAdditionalPropertyInner

# TODO update the JSON string below
json = "{}"
# create an instance of AiAvailabilityHotelRoomSchemaAdditionalPropertyInner from a JSON string
ai_availability_hotel_room_schema_additional_property_inner_instance = AiAvailabilityHotelRoomSchemaAdditionalPropertyInner.from_json(json)
# print the JSON string representation of the object
print(AiAvailabilityHotelRoomSchemaAdditionalPropertyInner.to_json())

# convert the object into a dict
ai_availability_hotel_room_schema_additional_property_inner_dict = ai_availability_hotel_room_schema_additional_property_inner_instance.to_dict()
# create an instance of AiAvailabilityHotelRoomSchemaAdditionalPropertyInner from a dict
ai_availability_hotel_room_schema_additional_property_inner_from_dict = AiAvailabilityHotelRoomSchemaAdditionalPropertyInner.from_dict(ai_availability_hotel_room_schema_additional_property_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


