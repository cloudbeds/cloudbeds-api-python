# GetPaymentMethodsResponseDataGateway

Payment Gateway used by property

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gateway name | [optional] 
**currency** | **str** | 3 letters iso code | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_payment_methods_response_data_gateway import GetPaymentMethodsResponseDataGateway

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentMethodsResponseDataGateway from a JSON string
get_payment_methods_response_data_gateway_instance = GetPaymentMethodsResponseDataGateway.from_json(json)
# print the JSON string representation of the object
print(GetPaymentMethodsResponseDataGateway.to_json())

# convert the object into a dict
get_payment_methods_response_data_gateway_dict = get_payment_methods_response_data_gateway_instance.to_dict()
# create an instance of GetPaymentMethodsResponseDataGateway from a dict
get_payment_methods_response_data_gateway_from_dict = GetPaymentMethodsResponseDataGateway.from_dict(get_payment_methods_response_data_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


