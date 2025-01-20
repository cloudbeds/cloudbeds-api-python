# GetReservationInvoiceInformationResponseDataInnerReservationAddOnProductsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sold_product_id** | **str** | ID of the sold product | [optional] 
**product_name** | **str** | Name | [optional] 
**product_price** | **float** | Price | [optional] 
**product_quantity** | **int** | Quantity sold | [optional] 
**product_sub_total** | **float** | Gross amount | [optional] 
**product_fees** | **float** | Fees charged for this addon | [optional] 
**product_taxes** | **float** | Taxes charged for this addon | [optional] 
**product_total** | **float** | Net amount | [optional] 
**transaction_date_time** | **datetime** | Date and time of the sale | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_reservation_invoice_information_response_data_inner_reservation_add_on_products_inner import GetReservationInvoiceInformationResponseDataInnerReservationAddOnProductsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationInvoiceInformationResponseDataInnerReservationAddOnProductsInner from a JSON string
get_reservation_invoice_information_response_data_inner_reservation_add_on_products_inner_instance = GetReservationInvoiceInformationResponseDataInnerReservationAddOnProductsInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationInvoiceInformationResponseDataInnerReservationAddOnProductsInner.to_json())

# convert the object into a dict
get_reservation_invoice_information_response_data_inner_reservation_add_on_products_inner_dict = get_reservation_invoice_information_response_data_inner_reservation_add_on_products_inner_instance.to_dict()
# create an instance of GetReservationInvoiceInformationResponseDataInnerReservationAddOnProductsInner from a dict
get_reservation_invoice_information_response_data_inner_reservation_add_on_products_inner_from_dict = GetReservationInvoiceInformationResponseDataInnerReservationAddOnProductsInner.from_dict(get_reservation_invoice_information_response_data_inner_reservation_add_on_products_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


