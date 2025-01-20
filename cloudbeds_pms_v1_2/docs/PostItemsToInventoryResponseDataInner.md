# PostItemsToInventoryResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Item identifier | [optional] 
**item_sku** | **str** |  Item SKU | [optional] 
**item_name** | **str** | Item name | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_items_to_inventory_response_data_inner import PostItemsToInventoryResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostItemsToInventoryResponseDataInner from a JSON string
post_items_to_inventory_response_data_inner_instance = PostItemsToInventoryResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(PostItemsToInventoryResponseDataInner.to_json())

# convert the object into a dict
post_items_to_inventory_response_data_inner_dict = post_items_to_inventory_response_data_inner_instance.to_dict()
# create an instance of PostItemsToInventoryResponseDataInner from a dict
post_items_to_inventory_response_data_inner_from_dict = PostItemsToInventoryResponseDataInner.from_dict(post_items_to_inventory_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


