# GetReservationInvoiceInformationResponseDataInnerReservationAdjustmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment_description** | **str** | Description | [optional] 
**adjustment_room_name** | **str** | Room name | [optional] 
**adjustment_date_time** | **datetime** | Date and time of the adjustment | [optional] 
**adjustment_date_time_utc** | **datetime** | Date and time of the adjustment (UTC) | [optional] 
**adjustment_amount** | **float** | Amount | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_reservation_invoice_information_response_data_inner_reservation_adjustments_inner import GetReservationInvoiceInformationResponseDataInnerReservationAdjustmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationInvoiceInformationResponseDataInnerReservationAdjustmentsInner from a JSON string
get_reservation_invoice_information_response_data_inner_reservation_adjustments_inner_instance = GetReservationInvoiceInformationResponseDataInnerReservationAdjustmentsInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationInvoiceInformationResponseDataInnerReservationAdjustmentsInner.to_json())

# convert the object into a dict
get_reservation_invoice_information_response_data_inner_reservation_adjustments_inner_dict = get_reservation_invoice_information_response_data_inner_reservation_adjustments_inner_instance.to_dict()
# create an instance of GetReservationInvoiceInformationResponseDataInnerReservationAdjustmentsInner from a dict
get_reservation_invoice_information_response_data_inner_reservation_adjustments_inner_from_dict = GetReservationInvoiceInformationResponseDataInnerReservationAdjustmentsInner.from_dict(get_reservation_invoice_information_response_data_inner_reservation_adjustments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


