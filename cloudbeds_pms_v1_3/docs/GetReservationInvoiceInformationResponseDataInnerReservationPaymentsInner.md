# GetReservationInvoiceInformationResponseDataInnerReservationPaymentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type** | **str** | Type | [optional] 
**payment_description** | **str** | Description | [optional] 
**payment_date_time** | **datetime** | Date and time of the payment | [optional] 
**payment_date_time_utc** | **datetime** | Date and time of the payment (UTC) | [optional] 
**payment_amount** | **float** | Amount | [optional] 
**reservation_payments_total** | **float** | Total sum of payments | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_invoice_information_response_data_inner_reservation_payments_inner import GetReservationInvoiceInformationResponseDataInnerReservationPaymentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationInvoiceInformationResponseDataInnerReservationPaymentsInner from a JSON string
get_reservation_invoice_information_response_data_inner_reservation_payments_inner_instance = GetReservationInvoiceInformationResponseDataInnerReservationPaymentsInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationInvoiceInformationResponseDataInnerReservationPaymentsInner.to_json())

# convert the object into a dict
get_reservation_invoice_information_response_data_inner_reservation_payments_inner_dict = get_reservation_invoice_information_response_data_inner_reservation_payments_inner_instance.to_dict()
# create an instance of GetReservationInvoiceInformationResponseDataInnerReservationPaymentsInner from a dict
get_reservation_invoice_information_response_data_inner_reservation_payments_inner_from_dict = GetReservationInvoiceInformationResponseDataInnerReservationPaymentsInner.from_dict(get_reservation_invoice_information_response_data_inner_reservation_payments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


