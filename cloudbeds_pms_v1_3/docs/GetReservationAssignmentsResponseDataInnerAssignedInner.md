# GetReservationAssignmentsResponseDataInnerAssignedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | ID of the room type assigned | [optional] 
**room_type_name** | **str** | Name of the room type assigned | [optional] 
**room_type_name_short** | **str** | Short name of the room type assigned | [optional] 
**dorm_room_name** | **str** | Name of the dorm room. Used for the shared dorm beds that are organized into rooms within the same room type | [optional] 
**room_name** | **str** | Name of the specific room assigned | [optional] 
**room_id** | **str** | ID of the specific room assigned | [optional] 
**sub_reservation_id** | **str** | Associated subReservation ID (specific to room) | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_assignments_response_data_inner_assigned_inner import GetReservationAssignmentsResponseDataInnerAssignedInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationAssignmentsResponseDataInnerAssignedInner from a JSON string
get_reservation_assignments_response_data_inner_assigned_inner_instance = GetReservationAssignmentsResponseDataInnerAssignedInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationAssignmentsResponseDataInnerAssignedInner.to_json())

# convert the object into a dict
get_reservation_assignments_response_data_inner_assigned_inner_dict = get_reservation_assignments_response_data_inner_assigned_inner_instance.to_dict()
# create an instance of GetReservationAssignmentsResponseDataInnerAssignedInner from a dict
get_reservation_assignments_response_data_inner_assigned_inner_from_dict = GetReservationAssignmentsResponseDataInnerAssignedInner.from_dict(get_reservation_assignments_response_data_inner_assigned_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


