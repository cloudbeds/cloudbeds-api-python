# PostItemRequestPaymentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type** | **str** | Payment method. Use the call [getPaymentMethods](#api-Payment-getPaymentMethods) to get the properties enabled payment methods. | [optional] 
**amount** | **float** | payment amount | [optional] 
**notes** | **str** | payment note | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_item_request_payments_inner import PostItemRequestPaymentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostItemRequestPaymentsInner from a JSON string
post_item_request_payments_inner_instance = PostItemRequestPaymentsInner.from_json(json)
# print the JSON string representation of the object
print(PostItemRequestPaymentsInner.to_json())

# convert the object into a dict
post_item_request_payments_inner_dict = post_item_request_payments_inner_instance.to_dict()
# create an instance of PostItemRequestPaymentsInner from a dict
post_item_request_payments_inner_from_dict = PostItemRequestPaymentsInner.from_dict(post_item_request_payments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


