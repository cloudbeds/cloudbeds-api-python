# CheckPaymentRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type** | **str** | Payment method type. Use the getPaymentMethods API to retrieve available payment methods for the property. | 
**amount** | **str** | Payment amount in the property currency. | 
**card_type** | **str** | Card type, when paymentType is a card. Optional. | [optional] 
**note** | **str** | Optional payment note | [optional] 

## Example

```python
from cloudbeds_pms.models.check_payment_request_schema import CheckPaymentRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CheckPaymentRequestSchema from a JSON string
check_payment_request_schema_instance = CheckPaymentRequestSchema.from_json(json)
# print the JSON string representation of the object
print(CheckPaymentRequestSchema.to_json())

# convert the object into a dict
check_payment_request_schema_dict = check_payment_request_schema_instance.to_dict()
# create an instance of CheckPaymentRequestSchema from a dict
check_payment_request_schema_from_dict = CheckPaymentRequestSchema.from_dict(check_payment_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


