# PostCustomItemRequestPaymentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type** | **str** | Payment method. Use the call [getPaymentMethods](#api-Payment-getPaymentMethods) to get the properties enabled payment methods. | [optional] 
**card_type** | **str** | When paymentType is cards or credit, the cardType could be specified (visa, master etc.). The list of types can be found with [getPaymentMethods](#api-Payment-getPaymentMethods) (cardCode inside cardTypes). If omitted, payment is treated as Credit Card Without Details. | [optional] 
**amount** | **float** | payment amount | [optional] 
**notes** | **str** | payment note | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_custom_item_request_payments_inner import PostCustomItemRequestPaymentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostCustomItemRequestPaymentsInner from a JSON string
post_custom_item_request_payments_inner_instance = PostCustomItemRequestPaymentsInner.from_json(json)
# print the JSON string representation of the object
print(PostCustomItemRequestPaymentsInner.to_json())

# convert the object into a dict
post_custom_item_request_payments_inner_dict = post_custom_item_request_payments_inner_instance.to_dict()
# create an instance of PostCustomItemRequestPaymentsInner from a dict
post_custom_item_request_payments_inner_from_dict = PostCustomItemRequestPaymentsInner.from_dict(post_custom_item_request_payments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


