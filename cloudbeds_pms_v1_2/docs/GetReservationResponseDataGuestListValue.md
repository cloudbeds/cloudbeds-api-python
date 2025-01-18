# GetReservationResponseDataGuestListValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_id** | **str** | ID of the guest | [optional] 
**guest_first_name** | **str** | First Name | [optional] 
**guest_last_name** | **str** | Last Name | [optional] 
**guest_gender** | **str** | Gender | [optional] 
**guest_email** | **str** | Email Address | [optional] 
**guest_phone** | **str** | Phone Number | [optional] 
**guest_cell_phone** | **str** | Cell Phone Number | [optional] 
**guest_address** | **str** |  | [optional] 
**guest_address2** | **str** |  | [optional] 
**guest_city** | **str** |  | [optional] 
**guest_state** | **str** |  | [optional] 
**guest_country** | **str** |  | [optional] 
**guest_zip** | **str** |  | [optional] 
**guest_status** | **str** |  | [optional] 
**guest_birthdate** | **date** |  | [optional] 
**guest_document_type** | **str** |  | [optional] 
**guest_document_number** | **str** |  | [optional] 
**guest_document_issue_date** | **date** |  | [optional] 
**guest_document_issuing_country** | **str** |  | [optional] 
**guest_document_expiration_date** | **date** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**company_tax_id** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**assigned_room** | **str** | Returns true if guest has roomed assigned, false if not | [optional] 
**is_anonymized** | **bool** | Flag indicating the guest data was removed upon request | [optional] 
**room_id** | **str** | Room ID where guest is assigned | [optional] 
**room_name** | **str** | Room Name where guest is assigned | [optional] 
**room_type_name** | **str** | Room Type Name where guest is assigned | [optional] 
**room_type_is_virtual** | **bool** | If room is virtual (true) or physical (false) | [optional] 
**is_main_guest** | **bool** | If the guest is the main guest of the reservation or not | [optional] 
**custom_fields** | [**List[GetReservationResponseDataGuestListValueCustomFieldsInner]**](GetReservationResponseDataGuestListValueCustomFieldsInner.md) | List of custom fields | [optional] 
**rooms** | [**List[GetReservationResponseDataGuestListValueRoomsInner]**](GetReservationResponseDataGuestListValueRoomsInner.md) | List of all rooms that guest is assigned to | [optional] 
**unassigned_rooms** | [**List[GetReservationResponseDataGuestListValueUnassignedRoomsInner]**](GetReservationResponseDataGuestListValueUnassignedRoomsInner.md) | List of unassigned rooms | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_reservation_response_data_guest_list_value import GetReservationResponseDataGuestListValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationResponseDataGuestListValue from a JSON string
get_reservation_response_data_guest_list_value_instance = GetReservationResponseDataGuestListValue.from_json(json)
# print the JSON string representation of the object
print(GetReservationResponseDataGuestListValue.to_json())

# convert the object into a dict
get_reservation_response_data_guest_list_value_dict = get_reservation_response_data_guest_list_value_instance.to_dict()
# create an instance of GetReservationResponseDataGuestListValue from a dict
get_reservation_response_data_guest_list_value_from_dict = GetReservationResponseDataGuestListValue.from_dict(get_reservation_response_data_guest_list_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


