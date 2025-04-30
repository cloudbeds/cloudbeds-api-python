# GetReservationDeparturesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_name** | **str** | Main Guest Name | [optional] 
**guest_id** | **str** | Guest ID, can be used to get the corresponding guest details from \&quot;reservationDetails\&quot;. | [optional] 
**balance** | **float** | Balance owed at the time | [optional] 
**reservation_id** | **str** | Reservation identifier, used for all query operations | [optional] 
**reservation_details** | **List[object]** | Reservation details, please check response from \&quot;getReservation\&quot; method | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_departures_response_data_inner import GetReservationDeparturesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationDeparturesResponseDataInner from a JSON string
get_reservation_departures_response_data_inner_instance = GetReservationDeparturesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationDeparturesResponseDataInner.to_json())

# convert the object into a dict
get_reservation_departures_response_data_inner_dict = get_reservation_departures_response_data_inner_instance.to_dict()
# create an instance of GetReservationDeparturesResponseDataInner from a dict
get_reservation_departures_response_data_inner_from_dict = GetReservationDeparturesResponseDataInner.from_dict(get_reservation_departures_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


