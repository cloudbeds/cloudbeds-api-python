# GetReservationArrivalsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_id** | **str** | Guest ID | [optional] 
**guest_name** | **str** | Guest Name | [optional] 
**room_id** | **str** | Room ID where the guest is assigned | [optional] 
**balance** | **float** | Balance owed at the time | [optional] 
**reservation_id** | **str** | Reservation identifier, used for all query operations | [optional] 
**sub_reservation_id** | **str** | Unique Room-Reservation identifier | [optional] 
**estimated_arrival_time** | **str** | Estimated arrival time, 24-hour format. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_arrivals_response_data_inner import GetReservationArrivalsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationArrivalsResponseDataInner from a JSON string
get_reservation_arrivals_response_data_inner_instance = GetReservationArrivalsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationArrivalsResponseDataInner.to_json())

# convert the object into a dict
get_reservation_arrivals_response_data_inner_dict = get_reservation_arrivals_response_data_inner_instance.to_dict()
# create an instance of GetReservationArrivalsResponseDataInner from a dict
get_reservation_arrivals_response_data_inner_from_dict = GetReservationArrivalsResponseDataInner.from_dict(get_reservation_arrivals_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


