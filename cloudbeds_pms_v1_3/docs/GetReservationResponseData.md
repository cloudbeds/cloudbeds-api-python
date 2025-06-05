# GetReservationResponseData

Details for the reservation queried

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Property ID | [optional] 
**guest_name** | **str** | Main Guest Name | [optional] 
**guest_email** | **str** | Main Guest Email | [optional] 
**is_anonymized** | **bool** | Flag indicating the main guest data was removed upon request | [optional] 
**guest_list** | [**Dict[str, GetReservationResponseDataGuestListValue]**](GetReservationResponseDataGuestListValue.md) | A map of guest IDs to guest objects (key is the Guest ID). It contains an entry for each guest included on the reservation. | [optional] 
**reservation_id** | **str** | Reservation identifier | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_modified** | **datetime** |  | [optional] 
**estimated_arrival_time** | **str** | Estimated arrival time, 24-hour format. | [optional] 
**source** | **str** | Booking source (e.g. Website, Facebook Widget, Booking.com, etc) | [optional] 
**source_id** | **str** | Booking source unique id | [optional] 
**third_party_identifier** | **str** | If it was received from a booking channel, it displays its identifier. If not, it will be empty | [optional] 
**status** | **str** | Reservation status&lt;br /&gt; &#39;not_confirmed&#39; - Reservation is pending confirmation&lt;br /&gt; &#39;confirmed&#39; - Reservation is confirmed&lt;br /&gt; &#39;canceled&#39; - Reservation is canceled&lt;br /&gt; &#39;checked_in&#39; - Guest is in hotel&lt;br /&gt; &#39;checked_out&#39; - Guest already left hotel&lt;br /&gt; &#39;no_show&#39; - Guest didn&#39;t showed up on check-in date | [optional] 
**total** | **float** | Total price of the booking | [optional] 
**balance** | **float** | Balance currently owed | [optional] 
**balance_detailed** | [**GetReservationResponseDataBalanceDetailed**](GetReservationResponseDataBalanceDetailed.md) |  | [optional] 
**assigned** | [**List[GetReservationResponseDataAssignedInner]**](GetReservationResponseDataAssignedInner.md) | Assigned Rooms information | [optional] 
**unassigned** | [**List[GetReservationResponseDataUnassignedInner]**](GetReservationResponseDataUnassignedInner.md) | Unassigned Rooms information | [optional] 
**cards_on_file** | [**List[GetReservationResponseDataCardsOnFileInner]**](GetReservationResponseDataCardsOnFileInner.md) | Credit Cards stored for the reservation | [optional] 
**custom_fields** | [**List[GetReservationResponseDataGuestListValueCustomFieldsInner]**](GetReservationResponseDataGuestListValueCustomFieldsInner.md) | Custom Fields related to the reservation | [optional] 
**start_date** | **date** | First reservation check-in date | [optional] 
**end_date** | **date** | Last reservation check-out date | [optional] 
**allotment_block_code** | **str** | Allotment block code | [optional] 
**channel_provided_credit_card** | **bool** | Whether a credit card was provided by the channel. Only included for reservations originating from OTAs. | [optional] 
**group_inventory** | [**List[GetReservationResponseDataGroupInventoryInner]**](GetReservationResponseDataGroupInventoryInner.md) | Aggregate allotment block information | [optional] 
**origin** | **str** | Reservation origin | [optional] 
**meal_plans** | **str** | Reservation Meal Plans | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_response_data import GetReservationResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationResponseData from a JSON string
get_reservation_response_data_instance = GetReservationResponseData.from_json(json)
# print the JSON string representation of the object
print(GetReservationResponseData.to_json())

# convert the object into a dict
get_reservation_response_data_dict = get_reservation_response_data_instance.to_dict()
# create an instance of GetReservationResponseData from a dict
get_reservation_response_data_from_dict = GetReservationResponseData.from_dict(get_reservation_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


