# GetPaymentMethodsResponseDataGatewayInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gateway name | [optional] 
**currency** | **str** | 3 letters iso code | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_payment_methods_response_data_gateway_inner import GetPaymentMethodsResponseDataGatewayInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentMethodsResponseDataGatewayInner from a JSON string
get_payment_methods_response_data_gateway_inner_instance = GetPaymentMethodsResponseDataGatewayInner.from_json(json)
# print the JSON string representation of the object
print(GetPaymentMethodsResponseDataGatewayInner.to_json())

# convert the object into a dict
get_payment_methods_response_data_gateway_inner_dict = get_payment_methods_response_data_gateway_inner_instance.to_dict()
# create an instance of GetPaymentMethodsResponseDataGatewayInner from a dict
get_payment_methods_response_data_gateway_inner_from_dict = GetPaymentMethodsResponseDataGatewayInner.from_dict(get_payment_methods_response_data_gateway_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


