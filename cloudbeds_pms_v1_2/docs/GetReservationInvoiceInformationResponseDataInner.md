# GetReservationInvoiceInformationResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Reservation status&lt;br /&gt; &#39;not_confirmed&#39; - Reservation is pending confirmation&lt;br /&gt; &#39;confirmed&#39; - Reservation is confirmed&lt;br /&gt; &#39;canceled&#39; - Reservation is canceled&lt;br /&gt; &#39;checked_in&#39; - Guest is in hotel&lt;br /&gt; &#39;checked_out&#39; - Guest already left hotel&lt;br /&gt; &#39;no_show&#39; - Guest didn&#39;t showed up on check-in date | [optional] 
**custom_fields** | [**List[GetReservationResponseDataGuestListValueCustomFieldsInner]**](GetReservationResponseDataGuestListValueCustomFieldsInner.md) | Custom Fields related to the reservation | [optional] 
**main_guest_details** | [**List[GetReservationInvoiceInformationResponseDataInnerMainGuestDetailsInner]**](GetReservationInvoiceInformationResponseDataInnerMainGuestDetailsInner.md) | Details for the main guest of the reservation | [optional] 
**reservation_rooms** | [**List[GetReservationInvoiceInformationResponseDataInnerReservationRoomsInner]**](GetReservationInvoiceInformationResponseDataInnerReservationRoomsInner.md) | Booked rooms information | [optional] 
**reservation_rooms_total** | **float** | Total rates for all rooms | [optional] 
**reservation_adjustments** | [**List[GetReservationInvoiceInformationResponseDataInnerReservationAdjustmentsInner]**](GetReservationInvoiceInformationResponseDataInnerReservationAdjustmentsInner.md) | Adjustments applied to the reservation | [optional] 
**reservation_adjustments_total** | **float** | Total sum of adjustments | [optional] 
**reservation_payments** | [**List[GetReservationInvoiceInformationResponseDataInnerReservationPaymentsInner]**](GetReservationInvoiceInformationResponseDataInnerReservationPaymentsInner.md) | Payments made for this reservation | [optional] 
**reservation_additional_products** | [**List[GetReservationInvoiceInformationResponseDataInnerReservationAdditionalProductsInner]**](GetReservationInvoiceInformationResponseDataInnerReservationAdditionalProductsInner.md) | Additional items (products or services) | [optional] 
**reservation_additional_products_total** | **float** | Total sum for additional items | [optional] 
**reservation_add_on_products** | [**List[GetReservationInvoiceInformationResponseDataInnerReservationAddOnProductsInner]**](GetReservationInvoiceInformationResponseDataInnerReservationAddOnProductsInner.md) | Addons | [optional] 
**reservation_add_on_products_total** | **float** | Total sum for addons | [optional] 
**reservation_taxes** | [**List[GetReservationInvoiceInformationResponseDataInnerReservationTaxesInner]**](GetReservationInvoiceInformationResponseDataInnerReservationTaxesInner.md) | Taxes | [optional] 
**reservation_taxes_total** | **float** | Total sum for taxes | [optional] 
**reservation_fees** | [**List[GetReservationInvoiceInformationResponseDataInnerReservationTaxesInner]**](GetReservationInvoiceInformationResponseDataInnerReservationTaxesInner.md) | Fees | [optional] 
**reservation_fees_total** | **float** | Total sum for fees | [optional] 
**balance** | **float** | Balance currently owed | [optional] 
**balance_detailed** | [**List[GetReservationInvoiceInformationResponseDataInnerBalanceDetailedInner]**](GetReservationInvoiceInformationResponseDataInnerBalanceDetailedInner.md) | Reservation balance detailed with the information available on PC app, describing the financial items calculated | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_reservation_invoice_information_response_data_inner import GetReservationInvoiceInformationResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationInvoiceInformationResponseDataInner from a JSON string
get_reservation_invoice_information_response_data_inner_instance = GetReservationInvoiceInformationResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationInvoiceInformationResponseDataInner.to_json())

# convert the object into a dict
get_reservation_invoice_information_response_data_inner_dict = get_reservation_invoice_information_response_data_inner_instance.to_dict()
# create an instance of GetReservationInvoiceInformationResponseDataInner from a dict
get_reservation_invoice_information_response_data_inner_from_dict = GetReservationInvoiceInformationResponseDataInner.from_dict(get_reservation_invoice_information_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


