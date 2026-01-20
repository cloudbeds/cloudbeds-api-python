# PaymentRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type** | **str** | Payment method type. Use getPaymentMethods API to retrieve available payment methods for the property. | 
**amount** | **str** | Payment amount in the smallest currency unit (e.g., cents for USD). For example, $10.50 should be sent as &#39;1050&#39;. | 
**notes** | **str** | Optional payment notes | [optional] 

## Example

```python
from cloudbeds_pms.models.payment_request_schema import PaymentRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRequestSchema from a JSON string
payment_request_schema_instance = PaymentRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PaymentRequestSchema.to_json())

# convert the object into a dict
payment_request_schema_dict = payment_request_schema_instance.to_dict()
# create an instance of PaymentRequestSchema from a dict
payment_request_schema_from_dict = PaymentRequestSchema.from_dict(payment_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


