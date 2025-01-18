# GetInvoiceResponseDataItemsInnerTaxesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_invoice_response_data_items_inner_taxes_inner import GetInvoiceResponseDataItemsInnerTaxesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceResponseDataItemsInnerTaxesInner from a JSON string
get_invoice_response_data_items_inner_taxes_inner_instance = GetInvoiceResponseDataItemsInnerTaxesInner.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceResponseDataItemsInnerTaxesInner.to_json())

# convert the object into a dict
get_invoice_response_data_items_inner_taxes_inner_dict = get_invoice_response_data_items_inner_taxes_inner_instance.to_dict()
# create an instance of GetInvoiceResponseDataItemsInnerTaxesInner from a dict
get_invoice_response_data_items_inner_taxes_inner_from_dict = GetInvoiceResponseDataItemsInnerTaxesInner.from_dict(get_invoice_response_data_items_inner_taxes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


