# PaymentMethodDetailsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PaymentMethodType**](PaymentMethodType.md) |  | 
**card** | [**CardDetailsResponseSchema**](CardDetailsResponseSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.payment_method_details_response_schema import PaymentMethodDetailsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodDetailsResponseSchema from a JSON string
payment_method_details_response_schema_instance = PaymentMethodDetailsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodDetailsResponseSchema.to_json())

# convert the object into a dict
payment_method_details_response_schema_dict = payment_method_details_response_schema_instance.to_dict()
# create an instance of PaymentMethodDetailsResponseSchema from a dict
payment_method_details_response_schema_from_dict = PaymentMethodDetailsResponseSchema.from_dict(payment_method_details_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


