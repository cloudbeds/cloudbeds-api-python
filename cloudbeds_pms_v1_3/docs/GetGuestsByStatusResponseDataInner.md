# GetGuestsByStatusResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_id** | **str** | Guest ID | [optional] 
**reservation_id** | **str** | Reservation&#39;s unique identifier | [optional] 
**sub_reservation_id** | **str** |  | [optional] 
**reservation_created_date_time** | **datetime** | Reservation creation datetime | [optional] 
**room_type_id** | **str** | Room Type ID that the guest is assigned | [optional] 
**room_id** | **str** | Room ID that the guest is assigned | [optional] 
**room_name** | **str** | Name of the room where guest is assigned | [optional] 
**guest_first_name** | **str** | First Name | [optional] 
**guest_last_name** | **str** | Last Name | [optional] 
**guest_gender** | **str** | Gender | [optional] 
**guest_email** | **str** | Email Address | [optional] 
**guest_phone** | **str** | Phone Number | [optional] 
**guest_cell_phone** | **str** | Cell Phone Number | [optional] 
**guest_address1** | **str** | Address | [optional] 
**guest_address2** | **str** | Address line 2 | [optional] 
**guest_city** | **str** | Address city | [optional] 
**guest_state** | **str** | Address state | [optional] 
**guest_country** | **str** | Address country | [optional] 
**guest_zip** | **str** | Address zip code | [optional] 
**guest_birth_date** | **date** | Guests Date of Birth | [optional] 
**guest_document_type** | **str** | Document Type | [optional] 
**guest_document_number** | **str** | Document Number | [optional] 
**guest_document_issue_date** | **date** | Document Issue Date | [optional] 
**guest_document_issuing_country** | **str** | Document Issuing Country | [optional] 
**guest_document_expiration_date** | **date** | Document Expiration Date | [optional] 
**start_date** | **datetime** | Check-in date | [optional] 
**end_date** | **datetime** | Check-out date | [optional] 
**custom_fields** | [**List[GetGuestsModifiedResponseDataInnerCustomFieldsInner]**](GetGuestsModifiedResponseDataInnerCustomFieldsInner.md) | List of custom fields | [optional] 
**date_modified** | **datetime** | Guest modification date | [optional] 
**current_status** | **str** | Current Status of the guest. Does not need to be equal to the status looked for (it may have had a status change outside of the filtered date range). | [optional] 
**status_date** | **datetime** | DateTime when the last status modification occurred. | [optional] 
**tax_id** | **str** | Tax ID | [optional] 
**company_tax_id** | **str** | Company tax ID | [optional] 
**company_name** | **str** | Company name | [optional] 
**is_anonymized** | **bool** | Flag indicating the guest data was removed upon request | [optional] 
**is_deleted** | **bool** | Flag indicating the guest&#39;s reservation was removed | [optional] 
**guest_opt_in** | **bool** | If guest has opted-in to marketing communication or not | [optional] 
**is_merged** | **bool** | Flag indicating that guest was merged | [optional] 
**new_guest_id** | **str** | Merged guest ID | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_guests_by_status_response_data_inner import GetGuestsByStatusResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGuestsByStatusResponseDataInner from a JSON string
get_guests_by_status_response_data_inner_instance = GetGuestsByStatusResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetGuestsByStatusResponseDataInner.to_json())

# convert the object into a dict
get_guests_by_status_response_data_inner_dict = get_guests_by_status_response_data_inner_instance.to_dict()
# create an instance of GetGuestsByStatusResponseDataInner from a dict
get_guests_by_status_response_data_inner_from_dict = GetGuestsByStatusResponseDataInner.from_dict(get_guests_by_status_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


