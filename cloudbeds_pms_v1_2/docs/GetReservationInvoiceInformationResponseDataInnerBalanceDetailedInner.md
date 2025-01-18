# GetReservationInvoiceInformationResponseDataInnerBalanceDetailedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggested_deposit** | **str** | Suggested deposit value, calculated according to the hotel policies. Does not mean that it was effectively paid | [optional] 
**sub_total** | **float** | Sum of the room prices on the reservation | [optional] 
**additional_items** | **float** | Sum of the additional items recorded on the reservation | [optional] 
**taxes_fees** | **float** | Sum of taxes and fees on the reservation | [optional] 
**grand_total** | **float** | Sum of sub.Total + additionalItems + taxesFees | [optional] 
**paid** | **float** | Amount paid (reservation deposit + any other extra payment) | [optional] 
**original_currency_code** | **str** | The currency the booking was originally made in. Included only if different from property currency | [optional] 
**original_currency_rate** | **float** | The currency conversion rate used at the time of booking. Included only if originalCurrencyCode is different from property currency. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_reservation_invoice_information_response_data_inner_balance_detailed_inner import GetReservationInvoiceInformationResponseDataInnerBalanceDetailedInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationInvoiceInformationResponseDataInnerBalanceDetailedInner from a JSON string
get_reservation_invoice_information_response_data_inner_balance_detailed_inner_instance = GetReservationInvoiceInformationResponseDataInnerBalanceDetailedInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationInvoiceInformationResponseDataInnerBalanceDetailedInner.to_json())

# convert the object into a dict
get_reservation_invoice_information_response_data_inner_balance_detailed_inner_dict = get_reservation_invoice_information_response_data_inner_balance_detailed_inner_instance.to_dict()
# create an instance of GetReservationInvoiceInformationResponseDataInnerBalanceDetailedInner from a dict
get_reservation_invoice_information_response_data_inner_balance_detailed_inner_from_dict = GetReservationInvoiceInformationResponseDataInnerBalanceDetailedInner.from_dict(get_reservation_invoice_information_response_data_inner_balance_detailed_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


