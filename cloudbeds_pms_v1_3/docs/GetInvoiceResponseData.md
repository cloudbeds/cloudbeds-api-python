# GetInvoiceResponseData

Invoice details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Unique invoice ID | [optional] 
**reservation_id** | **str** | Reservation identifier | [optional] 
**prefix** | **str** | Invoice ID prefix | [optional] 
**number** | **int** | Invoice ID number | [optional] 
**suffix** | **str** | Invoice ID suffix | [optional] 
**document_issue_date** | **str** | Date and time when invoice was issued | [optional] 
**status** | **str** | Invoice status | [optional] 
**billed_to** | [**GetInvoiceResponseDataBilledTo**](GetInvoiceResponseDataBilledTo.md) |  | [optional] 
**items** | [**List[GetInvoiceResponseDataItemsInner]**](GetInvoiceResponseDataItemsInner.md) | Invoice items | [optional] 
**taxes** | [**List[GetInvoiceResponseDataItemsInnerTaxesInner]**](GetInvoiceResponseDataItemsInnerTaxesInner.md) |  | [optional] 
**fees** | [**List[GetInvoiceResponseDataItemsInnerFeesInner]**](GetInvoiceResponseDataItemsInnerFeesInner.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_invoice_response_data import GetInvoiceResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceResponseData from a JSON string
get_invoice_response_data_instance = GetInvoiceResponseData.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceResponseData.to_json())

# convert the object into a dict
get_invoice_response_data_dict = get_invoice_response_data_instance.to_dict()
# create an instance of GetInvoiceResponseData from a dict
get_invoice_response_data_from_dict = GetInvoiceResponseData.from_dict(get_invoice_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


