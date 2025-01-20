# GetInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**GetInvoiceResponseData**](GetInvoiceResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_invoice_response import GetInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceResponse from a JSON string
get_invoice_response_instance = GetInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceResponse.to_json())

# convert the object into a dict
get_invoice_response_dict = get_invoice_response_instance.to_dict()
# create an instance of GetInvoiceResponse from a dict
get_invoice_response_from_dict = GetInvoiceResponse.from_dict(get_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


