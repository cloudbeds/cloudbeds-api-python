# GetPaymentMethodsResponseData



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Property ID | [optional] 
**methods** | [**List[GetPaymentMethodsResponseDataMethodsInner]**](GetPaymentMethodsResponseDataMethodsInner.md) | List of active methods enabled | [optional] 
**gateway** | [**GetPaymentMethodsResponseDataGateway**](GetPaymentMethodsResponseDataGateway.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_payment_methods_response_data import GetPaymentMethodsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentMethodsResponseData from a JSON string
get_payment_methods_response_data_instance = GetPaymentMethodsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetPaymentMethodsResponseData.to_json())

# convert the object into a dict
get_payment_methods_response_data_dict = get_payment_methods_response_data_instance.to_dict()
# create an instance of GetPaymentMethodsResponseData from a dict
get_payment_methods_response_data_from_dict = GetPaymentMethodsResponseData.from_dict(get_payment_methods_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


