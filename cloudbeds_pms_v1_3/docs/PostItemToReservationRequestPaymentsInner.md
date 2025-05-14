# PostItemToReservationRequestPaymentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type** | **str** | Payment method. Use the call [getPaymentMethods](#api-Payment-getPaymentMethods) to get the properties enabled payment methods. | [optional] 
**amount** | **float** | payment amount | [optional] 
**notes** | **str** | payment note | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_item_to_reservation_request_payments_inner import PostItemToReservationRequestPaymentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostItemToReservationRequestPaymentsInner from a JSON string
post_item_to_reservation_request_payments_inner_instance = PostItemToReservationRequestPaymentsInner.from_json(json)
# print the JSON string representation of the object
print(PostItemToReservationRequestPaymentsInner.to_json())

# convert the object into a dict
post_item_to_reservation_request_payments_inner_dict = post_item_to_reservation_request_payments_inner_instance.to_dict()
# create an instance of PostItemToReservationRequestPaymentsInner from a dict
post_item_to_reservation_request_payments_inner_from_dict = PostItemToReservationRequestPaymentsInner.from_dict(post_item_to_reservation_request_payments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


