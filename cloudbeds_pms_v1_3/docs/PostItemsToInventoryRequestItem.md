# PostItemsToInventoryRequestItem

Items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Property ID | [optional] 
**item_name** | **str** | Item name | [optional] 
**category_id** | **str** | Item category identifier | [optional] 
**item_type** | **str** | Item type | [optional] 
**item_sku** | **str** | Item SKU. Will be generated if not set | [optional] 
**item_code** | **str** | Item code | [optional] 
**item_description** | **str** | Item description | [optional] 
**item_price** | **float** | Item price&lt;br /&gt;When ItemPrice is blank the item will be created as Free / Complimentaty item without price | [optional] 
**stock_inventory** | **bool** | Track stock inventory for this item | [optional] [default to False]
**item_quantity** | **int** | ¹ Current amount of item available | [optional] 
**reorder_threshold** | **int** | ¹ Quantity at which to reorder item | [optional] 
**stop_sell_met** | **bool** | ¹ true - Whether item is at or below value set for stop-sell threshold. | [optional] [default to False]
**stop_sell** | **int** | ¹ Quantity at which to stop selling product. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_items_to_inventory_request_item import PostItemsToInventoryRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of PostItemsToInventoryRequestItem from a JSON string
post_items_to_inventory_request_item_instance = PostItemsToInventoryRequestItem.from_json(json)
# print the JSON string representation of the object
print(PostItemsToInventoryRequestItem.to_json())

# convert the object into a dict
post_items_to_inventory_request_item_dict = post_items_to_inventory_request_item_instance.to_dict()
# create an instance of PostItemsToInventoryRequestItem from a dict
post_items_to_inventory_request_item_from_dict = PostItemsToInventoryRequestItem.from_dict(post_items_to_inventory_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


