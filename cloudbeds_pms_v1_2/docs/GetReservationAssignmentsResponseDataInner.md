# GetReservationAssignmentsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_name** | **str** | Guest Name | [optional] 
**reservation_id** | **str** | Reservation identifier, used for all query operations | [optional] 
**unassigned** | **int** | Number of rooms unassigned | [optional] 
**assigned** | [**List[GetReservationAssignmentsResponseDataInnerAssignedInner]**](GetReservationAssignmentsResponseDataInnerAssignedInner.md) | Assigned Rooms information. May not exist if no room is assigned. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_reservation_assignments_response_data_inner import GetReservationAssignmentsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationAssignmentsResponseDataInner from a JSON string
get_reservation_assignments_response_data_inner_instance = GetReservationAssignmentsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationAssignmentsResponseDataInner.to_json())

# convert the object into a dict
get_reservation_assignments_response_data_inner_dict = get_reservation_assignments_response_data_inner_instance.to_dict()
# create an instance of GetReservationAssignmentsResponseDataInner from a dict
get_reservation_assignments_response_data_inner_from_dict = GetReservationAssignmentsResponseDataInner.from_dict(get_reservation_assignments_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


