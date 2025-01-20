# GetReservationInvoiceInformationResponseDataInnerReservationTaxesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_name** | **str** | Name | [optional] 
**tax_amount** | **float** | Amount | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_reservation_invoice_information_response_data_inner_reservation_taxes_inner import GetReservationInvoiceInformationResponseDataInnerReservationTaxesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationInvoiceInformationResponseDataInnerReservationTaxesInner from a JSON string
get_reservation_invoice_information_response_data_inner_reservation_taxes_inner_instance = GetReservationInvoiceInformationResponseDataInnerReservationTaxesInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationInvoiceInformationResponseDataInnerReservationTaxesInner.to_json())

# convert the object into a dict
get_reservation_invoice_information_response_data_inner_reservation_taxes_inner_dict = get_reservation_invoice_information_response_data_inner_reservation_taxes_inner_instance.to_dict()
# create an instance of GetReservationInvoiceInformationResponseDataInnerReservationTaxesInner from a dict
get_reservation_invoice_information_response_data_inner_reservation_taxes_inner_from_dict = GetReservationInvoiceInformationResponseDataInnerReservationTaxesInner.from_dict(get_reservation_invoice_information_response_data_inner_reservation_taxes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


