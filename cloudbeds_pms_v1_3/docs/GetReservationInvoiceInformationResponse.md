# GetReservationInvoiceInformationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetReservationInvoiceInformationResponseDataInner]**](GetReservationInvoiceInformationResponseDataInner.md) | Details for the rooms assigned on the selected date | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_invoice_information_response import GetReservationInvoiceInformationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationInvoiceInformationResponse from a JSON string
get_reservation_invoice_information_response_instance = GetReservationInvoiceInformationResponse.from_json(json)
# print the JSON string representation of the object
print(GetReservationInvoiceInformationResponse.to_json())

# convert the object into a dict
get_reservation_invoice_information_response_dict = get_reservation_invoice_information_response_instance.to_dict()
# create an instance of GetReservationInvoiceInformationResponse from a dict
get_reservation_invoice_information_response_from_dict = GetReservationInvoiceInformationResponse.from_dict(get_reservation_invoice_information_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


