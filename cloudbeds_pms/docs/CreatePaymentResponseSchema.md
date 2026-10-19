# CreatePaymentResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_status** | [**PaymentStatus**](PaymentStatus.md) |  | [optional] 
**payment_id** | **str** | The ID of the created payment | [optional] 
**payment_method_details** | [**PaymentMethodDetailsResponseSchema**](PaymentMethodDetailsResponseSchema.md) |  | [optional] 
**next_action** | [**NextActionResponseSchema**](NextActionResponseSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.create_payment_response_schema import CreatePaymentResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentResponseSchema from a JSON string
create_payment_response_schema_instance = CreatePaymentResponseSchema.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentResponseSchema.to_json())

# convert the object into a dict
create_payment_response_schema_dict = create_payment_response_schema_instance.to_dict()
# create an instance of CreatePaymentResponseSchema from a dict
create_payment_response_schema_from_dict = CreatePaymentResponseSchema.from_dict(create_payment_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


