# ReservationContextSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booking_room_id** | **str** |  | 
**checkin_date** | **date** |  | 
**checkout_date** | **date** |  | 
**current_room_type_id** | **str** |  | 
**current_room_id** | **str** | Composite room id \&quot;{roomTypeId}-{roomNumber}\&quot;, or null when no room is assigned. | [optional] 
**current_rate_id** | **str** |  | 
**original_rate_total** | [**MoneySchema**](MoneySchema.md) |  | 
**allotment_block_code** | **str** | Allotment block code the reservation belongs to, if any. | [optional] 
**adults** | **int** | Adults on the current assignment. | 
**children** | **int** | Children on the current assignment. | 
**confirmation_number** | **str** | Confirmation number for this specific room within the reservation. | 
**room_group** | **str** | Group key shared by the rooms that were booked together in this reservation. | 
**guest_name** | **str** | Guest full name for the current assignment; empty when unset. | 
**current_package_id** | **str** | Package id of the current rate, or null when the current rate has no package. | 
**detailed_rates** | [**List[NightlyRateSchema]**](NightlyRateSchema.md) | Current assignment&#39;s per-night rates (for \&quot;preserve original price\&quot; saves). | 

## Example

```python
from cloudbeds_pms.models.reservation_context_schema import ReservationContextSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationContextSchema from a JSON string
reservation_context_schema_instance = ReservationContextSchema.from_json(json)
# print the JSON string representation of the object
print(ReservationContextSchema.to_json())

# convert the object into a dict
reservation_context_schema_dict = reservation_context_schema_instance.to_dict()
# create an instance of ReservationContextSchema from a dict
reservation_context_schema_from_dict = ReservationContextSchema.from_dict(reservation_context_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


