# GetGuestResponseData

Details for the guest queried

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First Name | [optional] 
**last_name** | **str** | Last Name | [optional] 
**gender** | **str** | Gender | [optional] 
**email** | **str** | Email | [optional] 
**phone** | **str** | Phone number | [optional] 
**cell_phone** | **str** | Cell phone number | [optional] 
**country** | **str** | Country (2 digit code) | [optional] 
**address** | **str** | Address | [optional] 
**address2** | **str** | Address 2 | [optional] 
**city** | **str** | City | [optional] 
**zip** | **str** | Zip | [optional] 
**state** | **str** | State | [optional] 
**birth_date** | [**GetGuestResponseDataBirthDate**](GetGuestResponseDataBirthDate.md) |  | [optional] 
**document_type** | **str** | Document Type | [optional] 
**document_number** | **str** | Document number | [optional] 
**document_issue_date** | [**GetGuestResponseDataDocumentIssueDate**](GetGuestResponseDataDocumentIssueDate.md) |  | [optional] 
**document_issuing_country** | **str** | Document Issuing Country (2-digits code) | [optional] 
**document_expiration_date** | [**GetGuestResponseDataDocumentExpirationDate**](GetGuestResponseDataDocumentExpirationDate.md) |  | [optional] 
**custom_fields** | [**List[GetGuestResponseDataCustomFieldsInner]**](GetGuestResponseDataCustomFieldsInner.md) |  | [optional] 
**special_requests** | **str** | Special requests made by the guest at the time of the booking | [optional] 
**tax_id** | **str** | Tax ID | [optional] 
**company_tax_id** | **str** | Company tax ID | [optional] 
**company_name** | **str** | Company name | [optional] 
**is_anonymized** | **bool** | Flag indicating the guest data was removed upon request | [optional] 
**guest_opt_in** | **bool** | If guest has opted-in to marketing communication or not | [optional] 
**is_merged** | **bool** | Flag indicating that guest was merged | [optional] 
**new_guest_id** | **str** | Merged guest ID | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_guest_response_data import GetGuestResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetGuestResponseData from a JSON string
get_guest_response_data_instance = GetGuestResponseData.from_json(json)
# print the JSON string representation of the object
print(GetGuestResponseData.to_json())

# convert the object into a dict
get_guest_response_data_dict = get_guest_response_data_instance.to_dict()
# create an instance of GetGuestResponseData from a dict
get_guest_response_data_from_dict = GetGuestResponseData.from_dict(get_guest_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


