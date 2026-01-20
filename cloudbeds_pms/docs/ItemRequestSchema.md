# ItemRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Item identifier | 
**item_quantity** | **int** | Item quantity (must be greater than 0) | 
**item_price** | **str** | Custom item price in the smallest currency unit (e.g., cents for USD). If not provided, the item&#39;s registered price will be used. For example, $10.50 should be sent as &#39;1050&#39;. | [optional] 
**item_note** | **str** | Optional item note | [optional] 
**sub_reservation_id** | **str** | Sub-reservation identifier (optional) | [optional] 
**payments** | [**List[PaymentRequestSchema]**](PaymentRequestSchema.md) | Optional list of payments for this item. If provided, itemPaid is ignored. | [optional] 
**item_paid** | **bool** | If true, a cash payment will be automatically registered for the total value of the item including taxes and fees. Ignored if payments array is provided. | [optional] 

## Example

```python
from cloudbeds_pms.models.item_request_schema import ItemRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRequestSchema from a JSON string
item_request_schema_instance = ItemRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ItemRequestSchema.to_json())

# convert the object into a dict
item_request_schema_dict = item_request_schema_instance.to_dict()
# create an instance of ItemRequestSchema from a dict
item_request_schema_from_dict = ItemRequestSchema.from_dict(item_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


