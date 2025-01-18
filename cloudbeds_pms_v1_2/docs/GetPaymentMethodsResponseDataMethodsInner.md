# GetPaymentMethodsResponseDataMethodsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Payment Type | [optional] 
**name** | **str** | Payment Name (in given lang) | [optional] 
**card_types** | [**List[GetPaymentMethodsResponseDataMethodsInnerCardTypesInner]**](GetPaymentMethodsResponseDataMethodsInnerCardTypesInner.md) | IF type &#x3D; &#39;credit&#39; the enabled card types. Having the array&#39;s keys as its type and the value as its name. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_payment_methods_response_data_methods_inner import GetPaymentMethodsResponseDataMethodsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentMethodsResponseDataMethodsInner from a JSON string
get_payment_methods_response_data_methods_inner_instance = GetPaymentMethodsResponseDataMethodsInner.from_json(json)
# print the JSON string representation of the object
print(GetPaymentMethodsResponseDataMethodsInner.to_json())

# convert the object into a dict
get_payment_methods_response_data_methods_inner_dict = get_payment_methods_response_data_methods_inner_instance.to_dict()
# create an instance of GetPaymentMethodsResponseDataMethodsInner from a dict
get_payment_methods_response_data_methods_inner_from_dict = GetPaymentMethodsResponseDataMethodsInner.from_dict(get_payment_methods_response_data_methods_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


