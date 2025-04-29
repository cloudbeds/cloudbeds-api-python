# GetInvoiceResponseDataBilledTo

Information about who being billed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of who being billed Additional information about who being billed could be retrieved via corresponding API e.g.: for a guest it could be [getGuest](#tag/Guest/paths/~1getGuest/get) | [optional] 
**type** | **str** | Type of who being billed | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_invoice_response_data_billed_to import GetInvoiceResponseDataBilledTo

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceResponseDataBilledTo from a JSON string
get_invoice_response_data_billed_to_instance = GetInvoiceResponseDataBilledTo.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceResponseDataBilledTo.to_json())

# convert the object into a dict
get_invoice_response_data_billed_to_dict = get_invoice_response_data_billed_to_instance.to_dict()
# create an instance of GetInvoiceResponseDataBilledTo from a dict
get_invoice_response_data_billed_to_from_dict = GetInvoiceResponseDataBilledTo.from_dict(get_invoice_response_data_billed_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


