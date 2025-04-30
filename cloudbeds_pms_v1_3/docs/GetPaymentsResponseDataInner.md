# GetPaymentsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Transaction identifier | [optional] 
**payment_id** | **str** | Payment ID | [optional] 
**property_id** | **str** | Property ID | [optional] 
**transaction_date_time** | **datetime** | Transaction DateTime | [optional] 
**transaction_date_time_utc** | **datetime** | Transaction DateTime on UTC timezone | [optional] 
**user_id** | **str** | User ID that generated payment | [optional] 
**user_name** | **str** | User name that generated payment | [optional] 
**room_id** | **str** | ID of room. Only available when reservationID is sent. | [optional] 
**room_name** | **str** | Name/Number of room. Only available when reservationID is sent. | [optional] 
**guest_id** | **str** | Guest ID. Only available when reservationID or guestID is sent. | [optional] 
**guest_name** | **str** | Guest Name. Only available when reservationID or guestID is sent. | [optional] 
**guest_check_in** | **date** | Guest Check-In date. Only available when reservationID is sent. | [optional] 
**guest_check_out** | **date** | Guest Check-Out date. Only available when reservationID is sent. | [optional] 
**reservation_id** | **str** | Reservation ID. Only available when reservationID is sent. | [optional] 
**sub_reservation_id** | **str** | Sub reservation ID. Only available when reservationID is sent. | [optional] 
**reservation_status** | **str** | Current reservation status. Only available when reservationID is sent. | [optional] 
**house_account_id** | **str** | House Account ID, Only available when houseAccountID is sent. | [optional] 
**house_account_name** | **str** | House Account Name, Only available when houseAccountID is sent. | [optional] 
**description** | **str** | Description of the transaction | [optional] 
**payment_method** | **str** | Payment Method of the transaction | [optional] 
**quantity** | **int** |  | [optional] 
**amount** | **float** | Consolidated amount on the transaction (Credit - Debit) | [optional] 
**currency** | **str** | Currency of the transaction | [optional] 
**is_posted** | **bool** |  | [optional] 
**is_voided** | **bool** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**state** | **str** |  | [optional] 
**is_allocated** | **bool** | only if includePaymentAllocation&#x3D;true | [optional] 
**total_allocated** | **float** | ² Amount of allocated payment | [optional] 
**total_unallocated** | **float** | ² Amount of unallocated payment | [optional] 
**payment_allocation** | [**List[GetPaymentsResponseDataInnerPaymentAllocationInner]**](GetPaymentsResponseDataInnerPaymentAllocationInner.md) | ² | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_payments_response_data_inner import GetPaymentsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentsResponseDataInner from a JSON string
get_payments_response_data_inner_instance = GetPaymentsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetPaymentsResponseDataInner.to_json())

# convert the object into a dict
get_payments_response_data_inner_dict = get_payments_response_data_inner_instance.to_dict()
# create an instance of GetPaymentsResponseDataInner from a dict
get_payments_response_data_inner_from_dict = GetPaymentsResponseDataInner.from_dict(get_payments_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


