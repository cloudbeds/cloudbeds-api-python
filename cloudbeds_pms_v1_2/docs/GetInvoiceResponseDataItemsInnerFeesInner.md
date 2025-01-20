# GetInvoiceResponseDataItemsInnerFeesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**fee_id** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_invoice_response_data_items_inner_fees_inner import GetInvoiceResponseDataItemsInnerFeesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceResponseDataItemsInnerFeesInner from a JSON string
get_invoice_response_data_items_inner_fees_inner_instance = GetInvoiceResponseDataItemsInnerFeesInner.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceResponseDataItemsInnerFeesInner.to_json())

# convert the object into a dict
get_invoice_response_data_items_inner_fees_inner_dict = get_invoice_response_data_items_inner_fees_inner_instance.to_dict()
# create an instance of GetInvoiceResponseDataItemsInnerFeesInner from a dict
get_invoice_response_data_items_inner_fees_inner_from_dict = GetInvoiceResponseDataItemsInnerFeesInner.from_dict(get_invoice_response_data_items_inner_fees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


