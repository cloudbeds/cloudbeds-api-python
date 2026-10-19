# CheckDiscountRequestSchema

A discount applied to the whole check. It posts as its own negative folio line. To discount a single line instead, nest the discount inside that item as `items[].discounts[]`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Discount amount as a positive value in the property currency. Cloudbeds posts it as a negative folio line. | 
**name** | **str** | Human-readable label displayed on the folio line. | 
**code** | **str** | Partner-supplied code identifying the discount (e.g., promotion or coupon code). | 
**note** | **str** | Optional free-text note attached to the discount line item. | [optional] 

## Example

```python
from cloudbeds_pms.models.check_discount_request_schema import CheckDiscountRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDiscountRequestSchema from a JSON string
check_discount_request_schema_instance = CheckDiscountRequestSchema.from_json(json)
# print the JSON string representation of the object
print(CheckDiscountRequestSchema.to_json())

# convert the object into a dict
check_discount_request_schema_dict = check_discount_request_schema_instance.to_dict()
# create an instance of CheckDiscountRequestSchema from a dict
check_discount_request_schema_from_dict = CheckDiscountRequestSchema.from_dict(check_discount_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


