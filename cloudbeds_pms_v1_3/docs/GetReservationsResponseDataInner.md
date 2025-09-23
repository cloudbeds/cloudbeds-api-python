# GetReservationsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Properties identifier | [optional] 
**reservation_id** | **str** | Reservation&#39;s unique identifier | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_modified** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**guest_id** | **str** |  | [optional] 
**profile_id** | **str** |  | [optional] 
**guest_name** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**allotment_block_code** | **str** | Allotment block code | [optional] 
**group_code** | **str** | Group profile code | [optional] 
**adults** | **int** |  | [optional] 
**children** | **int** |  | [optional] 
**balance** | **float** |  | [optional] 
**source_name** | **str** | Source of reservation | [optional] 
**source_id** | **str** | Booking source unique id | [optional] 
**third_party_identifier** | **str** |  | [optional] 
**group_inventory** | [**List[GetReservationResponseDataGroupInventoryInner]**](GetReservationResponseDataGroupInventoryInner.md) | Aggregate allotment block information | [optional] 
**sub_reservation_id** | **str** | If roomID or roomName are given, the respective subReservationID (to that room) is informed. | [optional] 
**custom_fields** | [**List[GetGuestsModifiedResponseDataInnerCustomFieldsInner]**](GetGuestsModifiedResponseDataInnerCustomFieldsInner.md) | List of reservation custom fields. Only returned if \&quot;includeCustomFields\&quot; is true | [optional] 
**rooms** | [**List[GetReservationsResponseDataInnerRoomsInner]**](GetReservationsResponseDataInnerRoomsInner.md) | Array with rooms information. Only returned if \&quot;includeAllRooms\&quot; is true | [optional] 
**guest_list** | [**Dict[str, GetReservationsResponseDataInnerGuestListValue]**](GetReservationsResponseDataInnerGuestListValue.md) | A map of guest IDs to guest objects (key is the Guest ID). It contains an entry for each guest included on the reservation. Only returned if \&quot;includeGuestsDetails\&quot; is true | [optional] 
**origin** | **str** | Reservation origin | [optional] 
**meal_plans** | **str** | Reservation meal plans | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservations_response_data_inner import GetReservationsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationsResponseDataInner from a JSON string
get_reservations_response_data_inner_instance = GetReservationsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationsResponseDataInner.to_json())

# convert the object into a dict
get_reservations_response_data_inner_dict = get_reservations_response_data_inner_instance.to_dict()
# create an instance of GetReservationsResponseDataInner from a dict
get_reservations_response_data_inner_from_dict = GetReservationsResponseDataInner.from_dict(get_reservations_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


