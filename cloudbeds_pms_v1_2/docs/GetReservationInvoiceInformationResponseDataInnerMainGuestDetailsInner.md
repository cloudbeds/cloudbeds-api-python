# GetReservationInvoiceInformationResponseDataInnerMainGuestDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_first_name** | **str** | First Name | [optional] 
**guest_last_name** | **str** | Last Name | [optional] 
**guest_gender** | **str** | Gender | [optional] 
**guest_email** | **str** | Email Address | [optional] 
**guest_phone** | **str** | Phone Number | [optional] 
**guest_cell_phone** | **str** | Cell Phone Number | [optional] 
**guest_address** | **str** | Adress | [optional] 
**guest_address2** | **str** | Address Line 2 (Complement) | [optional] 
**guest_city** | **str** | City | [optional] 
**guest_country** | **str** | Country | [optional] 
**tax_id** | **str** | Guest Tax Identifier Number | [optional] 
**company_tax_id** | **str** | Company Tax Identifier Number | [optional] 
**company_name** | **str** | Company Name | [optional] 
**guest_state** | **str** | State | [optional] 
**guest_zip** | **str** | Zip code | [optional] 
**is_anonymyzed** | **bool** | Flag indicating the guest data was removed upon request | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_reservation_invoice_information_response_data_inner_main_guest_details_inner import GetReservationInvoiceInformationResponseDataInnerMainGuestDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationInvoiceInformationResponseDataInnerMainGuestDetailsInner from a JSON string
get_reservation_invoice_information_response_data_inner_main_guest_details_inner_instance = GetReservationInvoiceInformationResponseDataInnerMainGuestDetailsInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationInvoiceInformationResponseDataInnerMainGuestDetailsInner.to_json())

# convert the object into a dict
get_reservation_invoice_information_response_data_inner_main_guest_details_inner_dict = get_reservation_invoice_information_response_data_inner_main_guest_details_inner_instance.to_dict()
# create an instance of GetReservationInvoiceInformationResponseDataInnerMainGuestDetailsInner from a dict
get_reservation_invoice_information_response_data_inner_main_guest_details_inner_from_dict = GetReservationInvoiceInformationResponseDataInnerMainGuestDetailsInner.from_dict(get_reservation_invoice_information_response_data_inner_main_guest_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


