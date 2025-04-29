# GetReservationInvoiceInformationResponseDataInnerReservationRoomsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_name** | **str** | Room type name | [optional] 
**guest_name** | **str** | Assigned guest name | [optional] 
**start_date** | **date** | Check-in date | [optional] 
**end_date** | **date** | Check-out date | [optional] 
**adults** | **int** | Number of adults for the room | [optional] 
**children** | **int** | Number of children for the room | [optional] 
**nights** | **int** | Number of nights | [optional] 
**room_total** | **float** | Total rate for the room | [optional] 
**room_id** | **str** | Unique ID of the room | [optional] 
**room_name** | **str** | Name of the room | [optional] 
**room_type_id** | **str** | ID of the room type | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_invoice_information_response_data_inner_reservation_rooms_inner import GetReservationInvoiceInformationResponseDataInnerReservationRoomsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationInvoiceInformationResponseDataInnerReservationRoomsInner from a JSON string
get_reservation_invoice_information_response_data_inner_reservation_rooms_inner_instance = GetReservationInvoiceInformationResponseDataInnerReservationRoomsInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationInvoiceInformationResponseDataInnerReservationRoomsInner.to_json())

# convert the object into a dict
get_reservation_invoice_information_response_data_inner_reservation_rooms_inner_dict = get_reservation_invoice_information_response_data_inner_reservation_rooms_inner_instance.to_dict()
# create an instance of GetReservationInvoiceInformationResponseDataInnerReservationRoomsInner from a dict
get_reservation_invoice_information_response_data_inner_reservation_rooms_inner_from_dict = GetReservationInvoiceInformationResponseDataInnerReservationRoomsInner.from_dict(get_reservation_invoice_information_response_data_inner_reservation_rooms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


