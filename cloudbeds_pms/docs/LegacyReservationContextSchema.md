# LegacyReservationContextSchema

An earlier, narrower assignable-rooms reservation-context shape: ids are integers, originalRateTotal is a raw float, and none of the save-context fields are present. See ReservationContextSchema for the current shape.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booking_room_id** | **int** |  | 
**checkin_date** | **date** |  | 
**checkout_date** | **date** |  | 
**current_room_type_id** | **int** |  | 
**current_room_id** | **str** | Composite room id \&quot;{roomTypeId}-{roomNumber}\&quot;, or null when no room is assigned. | [optional] 
**current_rate_id** | **int** |  | 
**original_rate_total** | **float** | Total for the stay under the current rate. | 
**allotment_block_code** | **str** | Allotment block code the reservation belongs to, if any. | [optional] 

## Example

```python
from cloudbeds_pms.models.legacy_reservation_context_schema import LegacyReservationContextSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyReservationContextSchema from a JSON string
legacy_reservation_context_schema_instance = LegacyReservationContextSchema.from_json(json)
# print the JSON string representation of the object
print(LegacyReservationContextSchema.to_json())

# convert the object into a dict
legacy_reservation_context_schema_dict = legacy_reservation_context_schema_instance.to_dict()
# create an instance of LegacyReservationContextSchema from a dict
legacy_reservation_context_schema_from_dict = LegacyReservationContextSchema.from_dict(legacy_reservation_context_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


