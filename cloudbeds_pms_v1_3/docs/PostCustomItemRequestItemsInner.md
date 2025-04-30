# PostCustomItemRequestItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_item_id** | **str** | Identifier of item. Future calls using the same ID will use previously sent item name and description. Item name/description sent in new request will be ignored. | [optional] 
**item_sku** | **str** | Item SKU identifier | [optional] 
**item_quantity** | **int** | Items quantity | [optional] 
**item_price** | **float** | Item price | [optional] 
**item_name** | **str** | Item name | [optional] 
**item_category_name** | **str** | Item category name | [optional] 
**item_note** | **str** | Item note | [optional] 
**item_taxes** | [**List[PostCustomItemRequestItemsInnerItemTaxesInner]**](PostCustomItemRequestItemsInnerItemTaxesInner.md) | list of taxes applied to item | [optional] 
**item_fees** | [**List[PostCustomItemRequestItemsInnerItemFeesInner]**](PostCustomItemRequestItemsInnerItemFeesInner.md) | list of fees applied to item | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_custom_item_request_items_inner import PostCustomItemRequestItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostCustomItemRequestItemsInner from a JSON string
post_custom_item_request_items_inner_instance = PostCustomItemRequestItemsInner.from_json(json)
# print the JSON string representation of the object
print(PostCustomItemRequestItemsInner.to_json())

# convert the object into a dict
post_custom_item_request_items_inner_dict = post_custom_item_request_items_inner_instance.to_dict()
# create an instance of PostCustomItemRequestItemsInner from a dict
post_custom_item_request_items_inner_from_dict = PostCustomItemRequestItemsInner.from_dict(post_custom_item_request_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


