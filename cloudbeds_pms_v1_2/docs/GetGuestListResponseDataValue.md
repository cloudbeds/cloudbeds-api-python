# GetGuestListResponseDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** | Reservation&#39;s unique identifier | [optional] 
**guest_name** | **str** | Guest Name | [optional] 
**guest_email** | **str** | Guest Email | [optional] 
**guest_id** | **str** | Guest ID | [optional] 
**date_created** | **datetime** | Reservation creation date | [optional] 
**date_modified** | **datetime** | Reservation modification date | [optional] 
**is_main_guest** | **bool** | If the guest is the main guest of its reservation | [optional] 
**is_anonymized** | **bool** | Flag indicating the guest data was removed upon request | [optional] 
**guest_first_name** | **str** | Guest First Name | [optional] 
**guest_last_name** | **str** | Guest Last Name | [optional] 
**guest_gender** | **str** | Guest Gender | [optional] 
**guest_phone** | **str** | Guest Phone | [optional] 
**guest_cell_phone** | **str** | Guest Cell Phone | [optional] 
**guest_address1** | **str** | Guest Address (line 1) | [optional] 
**guest_address2** | **str** | Guest Address (line 2) | [optional] 
**guest_city** | **str** | Guest City | [optional] 
**guest_state** | **str** | Guest State | [optional] 
**guest_country** | **str** | Guest Country | [optional] 
**guest_zip** | **str** | Guest Zip code | [optional] 
**guest_birth_date** | **date** | Guest Birth Date | [optional] 
**guest_document_type** | **str** | Guest Document Type | [optional] 
**guest_document_number** | **str** | Guest Document Number | [optional] 
**guest_document_issue_date** | **date** | Guest Document Issue Date | [optional] 
**guest_document_issuing_country** | **str** | Guest Document Issuing Country | [optional] 
**guest_document_expiration_date** | **date** | Guest Document Expiration Date | [optional] 
**tax_id** | **str** | Tax ID | [optional] 
**company_tax_id** | **str** | Company tax ID | [optional] 
**company_name** | **str** | Company name | [optional] 
**guest_opt_in** | **bool** | If guest has opted-in to marketing communication or not | [optional] 
**guest_notes** | [**List[GetGuestListResponseDataValueGuestNotesInner]**](GetGuestListResponseDataValueGuestNotesInner.md) | Guest Notes | [optional] 
**status** | **str** | Reservation status&lt;br /&gt; in_progress - Reservation is pending confirmation&lt;br /&gt; confirmed - Reservation is confirmed&lt;br /&gt; not_confirmed - Reservation not passed confirmation&lt;br /&gt; canceled - Reservation is canceled&lt;br /&gt; checked_in - Guest is in hotel&lt;br /&gt; checked_out - Guest already left hotel&lt;br /&gt; no_show - Guest didn&#39;t showed up on check-in date | [optional] 
**is_merged** | **bool** | Flag indicating that guest was merged | [optional] 
**new_guest_id** | **str** | Merged guest ID | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_guest_list_response_data_value import GetGuestListResponseDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetGuestListResponseDataValue from a JSON string
get_guest_list_response_data_value_instance = GetGuestListResponseDataValue.from_json(json)
# print the JSON string representation of the object
print(GetGuestListResponseDataValue.to_json())

# convert the object into a dict
get_guest_list_response_data_value_dict = get_guest_list_response_data_value_instance.to_dict()
# create an instance of GetGuestListResponseDataValue from a dict
get_guest_list_response_data_value_from_dict = GetGuestListResponseDataValue.from_dict(get_guest_list_response_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


