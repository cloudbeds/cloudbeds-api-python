# CheckItemDiscountRequestSchema

A discount applied to the line it is nested under. Cloudbeds reduces that line's `amount` by this value and appends the discount to the line's `note`, so it stays visible on the folio; an item-level discount does not post a separate negative line. Several may be applied to one line, in which case their values are summed. A discount that applies to the whole check goes in the check-level `discounts[]` instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Discount amount as a positive value in the property currency. It is subtracted from the line&#39;s amount. The combined discounts on a line may not exceed that line&#39;s amount. | 
**name** | **str** | Human-readable label. Appended to the line&#39;s note so the reduction is explained on the folio. | 
**code** | **str** | Partner-supplied code identifying the discount (e.g. promotion or coupon code). | 
**note** | **str** | Optional free-text note. | [optional] 

## Example

```python
from cloudbeds_pms.models.check_item_discount_request_schema import CheckItemDiscountRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CheckItemDiscountRequestSchema from a JSON string
check_item_discount_request_schema_instance = CheckItemDiscountRequestSchema.from_json(json)
# print the JSON string representation of the object
print(CheckItemDiscountRequestSchema.to_json())

# convert the object into a dict
check_item_discount_request_schema_dict = check_item_discount_request_schema_instance.to_dict()
# create an instance of CheckItemDiscountRequestSchema from a dict
check_item_discount_request_schema_from_dict = CheckItemDiscountRequestSchema.from_dict(check_item_discount_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


