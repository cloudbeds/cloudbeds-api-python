# GetReservationsResponseDataInnerGuestListValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_id** | **str** | ID of the guest | [optional] 
**guest_name** | **str** |  | [optional] 
**guest_first_name** | **str** |  | [optional] 
**guest_last_name** | **str** |  | [optional] 
**guest_gender** | **str** |  | [optional] 
**guest_email** | **str** |  | [optional] 
**guest_phone** | **str** |  | [optional] 
**guest_cell_phone** | **str** |  | [optional] 
**guest_address** | **str** |  | [optional] 
**guest_address2** | **str** |  | [optional] 
**guest_city** | **str** |  | [optional] 
**guest_state** | **str** |  | [optional] 
**guest_country** | **str** |  | [optional] 
**guest_zip** | **str** |  | [optional] 
**guest_birthdate** | **date** |  | [optional] 
**guest_document_type** | **str** |  | [optional] 
**guest_document_number** | **str** |  | [optional] 
**guest_document_issue_date** | **date** |  | [optional] 
**guest_document_issuing_country** | **str** |  | [optional] 
**guest_document_expiration_date** | **date** |  | [optional] 
**tax_id** | **str** | Guest&#39;s tax ID | [optional] 
**company_tax_id** | **str** | Guest&#39;s company tax ID | [optional] 
**company_name** | **str** | Guest&#39;s company name | [optional] 
**sub_reservation_id** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**assigned_room** | **str** | Returns true if guest has roomed assigned, false if not | [optional] 
**room_id** | **str** | Room ID where guest is assigned | [optional] 
**room_name** | **str** | Room Name where guest is assigned | [optional] 
**room_type_name** | **str** | Room Name where guest is assigned | [optional] 
**room_type_is_virtual** | **bool** | If room is virtual (true) or physical (false) | [optional] 
**rooms** | [**List[GetReservationsResponseDataInnerGuestListValueRoomsInner]**](GetReservationsResponseDataInnerGuestListValueRoomsInner.md) | List of all rooms that guest is assigned to | [optional] 
**unassigned_rooms** | [**List[GetReservationsResponseDataInnerGuestListValueUnassignedRoomsInner]**](GetReservationsResponseDataInnerGuestListValueUnassignedRoomsInner.md) | List of all unassigned rooms | [optional] 
**guest_requirements** | **object** | Guest requirements data. Only included if &#x60;includeGuestsDetails&#x3D;true&#x60; and &#x60;includeGuestRequirements&#x3D;true&#x60;. | [optional] 
**custom_fields** | [**List[GetGuestsModifiedResponseDataInnerCustomFieldsInner]**](GetGuestsModifiedResponseDataInnerCustomFieldsInner.md) | List of guest custom fields | [optional] 
**is_anonymized** | **bool** | Flag indicating the guest data was removed upon request | [optional] 
**is_main_guest** | **bool** | Flag indicating the guest is the main guest on the reservation | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservations_response_data_inner_guest_list_value import GetReservationsResponseDataInnerGuestListValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationsResponseDataInnerGuestListValue from a JSON string
get_reservations_response_data_inner_guest_list_value_instance = GetReservationsResponseDataInnerGuestListValue.from_json(json)
# print the JSON string representation of the object
print(GetReservationsResponseDataInnerGuestListValue.to_json())

# convert the object into a dict
get_reservations_response_data_inner_guest_list_value_dict = get_reservations_response_data_inner_guest_list_value_instance.to_dict()
# create an instance of GetReservationsResponseDataInnerGuestListValue from a dict
get_reservations_response_data_inner_guest_list_value_from_dict = GetReservationsResponseDataInnerGuestListValue.from_dict(get_reservations_response_data_inner_guest_list_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


