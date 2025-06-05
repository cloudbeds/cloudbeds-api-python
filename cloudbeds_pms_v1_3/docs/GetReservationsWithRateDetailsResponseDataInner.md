# GetReservationsWithRateDetailsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Properties identifier | [optional] 
**reservation_id** | **str** | Reservation&#39;s unique identifier | [optional] 
**is_deleted** | **bool** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_created_utc** | **datetime** |  | [optional] 
**date_modified** | **datetime** |  | [optional] 
**date_modified_utc** | **datetime** |  | [optional] 
**date_cancelled** | **datetime** | Will be displayed only if \&quot;status &#x3D; &#39;canceled&#39;\&quot; | [optional] 
**date_cancelled_utc** | **datetime** | Will be displayed only if \&quot;status &#x3D; &#39;canceled&#39;\&quot; | [optional] 
**status** | **str** | Reservation status&lt;br /&gt; &#39;not_confirmed&#39; - Reservation is pending confirmation&lt;br /&gt; &#39;confirmed&#39; - Reservation is confirmed&lt;br /&gt; &#39;canceled&#39; - Reservation is canceled&lt;br /&gt; &#39;checked_in&#39; - Guest is in hotel&lt;br /&gt; &#39;checked_out&#39; - Guest already left hotel&lt;br /&gt; &#39;no_show&#39; - Guest didn&#39;t showed up on check-in date | [optional] 
**reservation_check_in** | **datetime** |  | [optional] 
**reservation_check_out** | **datetime** |  | [optional] 
**guest_id** | **str** | Main guest ID | [optional] 
**profile_id** | **str** | Main guest profile ID | [optional] 
**guest_country** | **int** | Main guest Country | [optional] 
**source_name** | **str** | Reservation source | [optional] 
**source** | [**List[GetReservationsWithRateDetailsResponseDataInnerSourceInner]**](GetReservationsWithRateDetailsResponseDataInnerSourceInner.md) |  | [optional] 
**source_category** | **int** | Reservation source category | [optional] 
**source_reservation_id** | **int** | Reservation ID on the source | [optional] 
**property_currency** | **int** | Property currency ISO-formatted (3 characters) | [optional] 
**balance_detailed** | [**List[GetReservationResponseDataBalanceDetailedOneOf]**](GetReservationResponseDataBalanceDetailedOneOf.md) | Reservation balance detailed with the information available on MyFrontdesk, describing the financial items calculated | [optional] 
**detailed_rates** | **List[object]** | Associative object, where key is the date, and value is the total rate for that date. | [optional] 
**rooms** | [**List[GetReservationsWithRateDetailsResponseDataInnerRoomsInner]**](GetReservationsWithRateDetailsResponseDataInnerRoomsInner.md) | Array with rooms information | [optional] 
**origin** | **str** | Reservation origin | [optional] 
**meal_plans** | **str** | Reservation meal plans | [optional] 
**guest_list** | [**Dict[str, GetReservationsResponseDataInnerGuestListValue]**](GetReservationsResponseDataInnerGuestListValue.md) | A map of guest IDs to guest objects (key is the Guest ID). It contains an entry for each guest included on the reservation. Only returned if \&quot;includeGuestsDetails\&quot; is true | [optional] 
**third_party_identifier** | **str** |  | [optional] 
**custom_fields** | [**List[GetGuestsModifiedResponseDataInnerCustomFieldsInner]**](GetGuestsModifiedResponseDataInnerCustomFieldsInner.md) | List of reservation custom fields. Only returned if \&quot;includeCustomFields\&quot; is true | [optional] 
**estimated_arrival_time** | **str** | Estimated arrival time, 24-hour format. | [optional] 
**total** | **float** | Total price of the booking | [optional] 
**balance** | **float** | Balance currently owed | [optional] 
**date_imported** | **str** | Date when the reservation was imported | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservations_with_rate_details_response_data_inner import GetReservationsWithRateDetailsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationsWithRateDetailsResponseDataInner from a JSON string
get_reservations_with_rate_details_response_data_inner_instance = GetReservationsWithRateDetailsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationsWithRateDetailsResponseDataInner.to_json())

# convert the object into a dict
get_reservations_with_rate_details_response_data_inner_dict = get_reservations_with_rate_details_response_data_inner_instance.to_dict()
# create an instance of GetReservationsWithRateDetailsResponseDataInner from a dict
get_reservations_with_rate_details_response_data_inner_from_dict = GetReservationsWithRateDetailsResponseDataInner.from_dict(get_reservations_with_rate_details_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


