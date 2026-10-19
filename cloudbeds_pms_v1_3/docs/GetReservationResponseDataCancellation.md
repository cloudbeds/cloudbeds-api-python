# GetReservationResponseDataCancellation

Cancellation attribution (who and how). Present only for cancelled reservations where attribution was recorded; null otherwise. For the cancellation timestamp use dateCancelled / dateCancelledUTC, which are set for every cancellation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | How the cancellation was received (e.g. user, ota, system) | [optional] 
**canceled_by** | **str** | Name of the actor who canceled the reservation | [optional] 
**canceled_by_id** | **str** | Identifier of the actor who canceled the reservation | [optional] 
**canceled_by_type** | **str** | Type of actor who canceled the reservation (e.g. user, guest, customer, person_version) | [optional] 
**origin** | **str** | Delivery channel the cancellation was received through (e.g. Dashboard, Booking.com) | [optional] 
**by_employee** | **bool** | Whether the actor who canceled the reservation is a Cloudbeds employee. Null when it cannot be determined. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_response_data_cancellation import GetReservationResponseDataCancellation

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationResponseDataCancellation from a JSON string
get_reservation_response_data_cancellation_instance = GetReservationResponseDataCancellation.from_json(json)
# print the JSON string representation of the object
print(GetReservationResponseDataCancellation.to_json())

# convert the object into a dict
get_reservation_response_data_cancellation_dict = get_reservation_response_data_cancellation_instance.to_dict()
# create an instance of GetReservationResponseDataCancellation from a dict
get_reservation_response_data_cancellation_from_dict = GetReservationResponseDataCancellation.from_dict(get_reservation_response_data_cancellation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


