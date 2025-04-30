# GetInvoiceResponseDataItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**total_amount** | **str** |  | [optional] 
**net_amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**taxes** | [**List[GetInvoiceResponseDataItemsInnerTaxesInner]**](GetInvoiceResponseDataItemsInnerTaxesInner.md) |  | [optional] 
**fees** | [**List[GetInvoiceResponseDataItemsInnerFeesInner]**](GetInvoiceResponseDataItemsInnerFeesInner.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_invoice_response_data_items_inner import GetInvoiceResponseDataItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceResponseDataItemsInner from a JSON string
get_invoice_response_data_items_inner_instance = GetInvoiceResponseDataItemsInner.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceResponseDataItemsInner.to_json())

# convert the object into a dict
get_invoice_response_data_items_inner_dict = get_invoice_response_data_items_inner_instance.to_dict()
# create an instance of GetInvoiceResponseDataItemsInner from a dict
get_invoice_response_data_items_inner_from_dict = GetInvoiceResponseDataItemsInner.from_dict(get_invoice_response_data_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


