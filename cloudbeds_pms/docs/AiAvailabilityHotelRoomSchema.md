# AiAvailabilityHotelRoomSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Booking-engine URL of the room type, keyed by &#x60;roomId&#x60;. | 
**name** | [**List[AiAvailabilityHotelRoomSchemaNameInner]**](AiAvailabilityHotelRoomSchemaNameInner.md) | Language-tagged values: always the property&#39;s default language and English, plus the requested &#x60;lang&#x60; when a translation exists. | 
**occupancy** | [**AiAvailabilityHotelRoomSchemaOccupancy**](AiAvailabilityHotelRoomSchemaOccupancy.md) |  | 
**offers** | [**List[AiAvailabilityOfferSchema]**](AiAvailabilityOfferSchema.md) |  | 
**additional_property** | [**List[AiAvailabilityHotelRoomSchemaAdditionalPropertyInner]**](AiAvailabilityHotelRoomSchemaAdditionalPropertyInner.md) | &#x60;unitsAvailable&#x60; (integer) and &#x60;policyId&#x60; (string, or null when the room type has no policy). Identifiers are strings; only counts and amounts are numbers. | 

## Example

```python
from cloudbeds_pms.models.ai_availability_hotel_room_schema import AiAvailabilityHotelRoomSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AiAvailabilityHotelRoomSchema from a JSON string
ai_availability_hotel_room_schema_instance = AiAvailabilityHotelRoomSchema.from_json(json)
# print the JSON string representation of the object
print(AiAvailabilityHotelRoomSchema.to_json())

# convert the object into a dict
ai_availability_hotel_room_schema_dict = ai_availability_hotel_room_schema_instance.to_dict()
# create an instance of AiAvailabilityHotelRoomSchema from a dict
ai_availability_hotel_room_schema_from_dict = AiAvailabilityHotelRoomSchema.from_dict(ai_availability_hotel_room_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


