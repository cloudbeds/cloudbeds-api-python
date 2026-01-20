# PostedItemResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sold_product_id** | **str** | Sold product identifier (can be used to void this product in the future) | 
**external_relation_id** | **str** | External relation ID (same as sold product ID). Together with external relation kind (ITEM) it can be used to get transaction from Accounting API | 
**transaction_status** | **str** | Transaction status. Returns &#39;pending&#39; when sale date is in the future, &#39;completed&#39; otherwise. | [optional] 
**remaining_item_quantity** | **int** | Remaining number of items in stock (only returned if item has stock inventory tracking enabled) | [optional] 
**reorder_needed** | **bool** | Whether item is at or below the reorder threshold (only returned if item has stock inventory tracking enabled) | [optional] 
**stop_sell_met** | **bool** | Whether item is at or below the stop-sell threshold (only returned if item has stock inventory tracking enabled) | [optional] 

## Example

```python
from cloudbeds_pms.models.posted_item_response_schema import PostedItemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PostedItemResponseSchema from a JSON string
posted_item_response_schema_instance = PostedItemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PostedItemResponseSchema.to_json())

# convert the object into a dict
posted_item_response_schema_dict = posted_item_response_schema_instance.to_dict()
# create an instance of PostedItemResponseSchema from a dict
posted_item_response_schema_from_dict = PostedItemResponseSchema.from_dict(posted_item_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


