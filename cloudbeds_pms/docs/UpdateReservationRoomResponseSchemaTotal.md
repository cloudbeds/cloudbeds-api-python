# UpdateReservationRoomResponseSchemaTotal

Room total after assignment in the booking's currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount in the smallest representable units of the currency (e.g., cents for USD). For example, USD $124.39 would be \&quot;12439\&quot;. | 
**currency_code** | **str** | ISO 4217 currency code | 

## Example

```python
from cloudbeds_pms.models.update_reservation_room_response_schema_total import UpdateReservationRoomResponseSchemaTotal

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReservationRoomResponseSchemaTotal from a JSON string
update_reservation_room_response_schema_total_instance = UpdateReservationRoomResponseSchemaTotal.from_json(json)
# print the JSON string representation of the object
print(UpdateReservationRoomResponseSchemaTotal.to_json())

# convert the object into a dict
update_reservation_room_response_schema_total_dict = update_reservation_room_response_schema_total_instance.to_dict()
# create an instance of UpdateReservationRoomResponseSchemaTotal from a dict
update_reservation_room_response_schema_total_from_dict = UpdateReservationRoomResponseSchemaTotal.from_dict(update_reservation_room_response_schema_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


