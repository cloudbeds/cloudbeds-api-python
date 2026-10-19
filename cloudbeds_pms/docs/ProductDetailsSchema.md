# ProductDetailsSchema

Product-only fields for a check item whose type is PRODUCT. sku is required — it is the catalog dedup key. Category and sub-reservation override remain optional.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | Partner-supplied SKU for the item. Required — used as the catalog dedup key and recorded on the folio line for cross-reference. | 
**category_name** | **str** | Category name as classified by the POS (e.g., &#39;Food&#39;, &#39;Beverage&#39;, &#39;Alcohol&#39;). Used for reporting and item classification. | [optional] 
**sub_reservation_id** | **str** | Sub-reservation identifier. If provided, this item is routed to the specified sub-reservation within the parent reservation (request-level reservationId). Has no effect when the request-level target is houseAccountId or eventCode. | [optional] 

## Example

```python
from cloudbeds_pms.models.product_details_schema import ProductDetailsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetailsSchema from a JSON string
product_details_schema_instance = ProductDetailsSchema.from_json(json)
# print the JSON string representation of the object
print(ProductDetailsSchema.to_json())

# convert the object into a dict
product_details_schema_dict = product_details_schema_instance.to_dict()
# create an instance of ProductDetailsSchema from a dict
product_details_schema_from_dict = ProductDetailsSchema.from_dict(product_details_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


