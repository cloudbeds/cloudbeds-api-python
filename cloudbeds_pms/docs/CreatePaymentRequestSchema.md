# CreatePaymentRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_mode** | [**CaptureModeSchema**](CaptureModeSchema.md) |  | 
**total** | [**MoneySchema**](MoneySchema.md) |  | 
**redirect_url** | **str** | URL to redirect the user to after 3D Secure authentication or other payment actions | 
**inventory_object** | [**InventoryObjectSchema**](InventoryObjectSchema.md) |  | 
**payment_method** | [**PaymentMethodSchema**](PaymentMethodSchema.md) |  | 
**description** | **str** | Optional payment description that appears in the folio. | [optional] 

## Example

```python
from cloudbeds_pms.models.create_payment_request_schema import CreatePaymentRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentRequestSchema from a JSON string
create_payment_request_schema_instance = CreatePaymentRequestSchema.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentRequestSchema.to_json())

# convert the object into a dict
create_payment_request_schema_dict = create_payment_request_schema_instance.to_dict()
# create an instance of CreatePaymentRequestSchema from a dict
create_payment_request_schema_from_dict = CreatePaymentRequestSchema.from_dict(create_payment_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


