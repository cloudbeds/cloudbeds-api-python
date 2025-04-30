# GetReservationInHouseResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_id** | **str** | Guest identifier | [optional] 
**guest_name** | **str** | Guest Name | [optional] 
**main_guest_id** | **str** | Guest identifier who made reservation | [optional] 
**main_guest_name** | **str** | Guest Name who made reservation | [optional] 
**balance** | **float** | Balance owed at the time | [optional] 
**reservation_id** | **str** | Reservation identifier, used for all query operations | [optional] 
**room_check_out** | **date** | Check-out date for the room | [optional] 
**reservation_custom_fields** | **List[object]** | Reservation Custom Fields, if existent | [optional] 
**room_id** | **str** | ¹ Room identifier | [optional] 
**room_name** | **str** | ¹ Room name | [optional] 
**guest_first_name** | **str** | Guest&#39;s First Name | [optional] 
**guest_last_name** | **str** | Guest&#39;s Last Name | [optional] 
**guest_phone** | **str** | Guest&#39;s Phone | [optional] 
**guest_address1** | **str** | Guest&#39;s Address (line 1) | [optional] 
**guest_address2** | **str** | Guest&#39;s Address (line 2) | [optional] 
**guest_city** | **str** | Guest&#39;s Address City | [optional] 
**guest_state** | **str** | Guest&#39;s Address State | [optional] 
**guest_country** | **str** | Guest&#39;s Address Country | [optional] 
**guest_zip** | **str** | Guest&#39;s Address Zip code | [optional] 
**guest_birth_date** | **date** | Guest&#39;s BirthDate | [optional] 
**guest_document_type** | **str** | Guest&#39;s Document Type | [optional] 
**guest_document_number** | **str** | Guest&#39;s Document Number | [optional] 
**guest_document_issue_date** | **date** | Guest&#39;s Document Issue Date | [optional] 
**guest_document_issuing_country** | **str** | Guest&#39;s Document Issuing Country | [optional] 
**guest_document_expiration_date** | **date** | Guest&#39;s Document Expiration Date | [optional] 
**guest_custom_fields** | **List[object]** | Guest&#39;s Custom Fields, if any | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_in_house_response_data_inner import GetReservationInHouseResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationInHouseResponseDataInner from a JSON string
get_reservation_in_house_response_data_inner_instance = GetReservationInHouseResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationInHouseResponseDataInner.to_json())

# convert the object into a dict
get_reservation_in_house_response_data_inner_dict = get_reservation_in_house_response_data_inner_instance.to_dict()
# create an instance of GetReservationInHouseResponseDataInner from a dict
get_reservation_in_house_response_data_inner_from_dict = GetReservationInHouseResponseDataInner.from_dict(get_reservation_in_house_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


