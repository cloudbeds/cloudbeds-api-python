# GetReservationResponseDataGroupInventoryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_reservation_id** | **str** | Sub Reservation ID of the specific assigned room | [optional] 
**allotment_block_code** | **str** | Allotment block code | [optional] 
**start_date** | **date** | Check-In date of the room | [optional] 
**end_date** | **date** | Check-Out date of the room | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_response_data_group_inventory_inner import GetReservationResponseDataGroupInventoryInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationResponseDataGroupInventoryInner from a JSON string
get_reservation_response_data_group_inventory_inner_instance = GetReservationResponseDataGroupInventoryInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationResponseDataGroupInventoryInner.to_json())

# convert the object into a dict
get_reservation_response_data_group_inventory_inner_dict = get_reservation_response_data_group_inventory_inner_instance.to_dict()
# create an instance of GetReservationResponseDataGroupInventoryInner from a dict
get_reservation_response_data_group_inventory_inner_from_dict = GetReservationResponseDataGroupInventoryInner.from_dict(get_reservation_response_data_group_inventory_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


