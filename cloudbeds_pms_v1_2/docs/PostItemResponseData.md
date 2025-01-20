# PostItemResponseData

Sold product details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sold_product_id** | **str** | Sold product identifier (Usable to void this product in future). | [optional] 
**transaction_id** | **str** | Transaction identifier | [optional] 
**transaction_status** | **str** | Transaction Status is returned \&quot;Pending\&quot; when sale date is in the future. | [optional] 
**remaining_item_quantity** | **int** | Remaining number of items in stock (if applicable) | [optional] 
**reorder_needed** | **bool** | true - Whether item is at or below value set for reorder threshold. | [optional] 
**stop_sell_met** | **bool** | true - Whether item is at or below value set for stop-sell threshold. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_item_response_data import PostItemResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostItemResponseData from a JSON string
post_item_response_data_instance = PostItemResponseData.from_json(json)
# print the JSON string representation of the object
print(PostItemResponseData.to_json())

# convert the object into a dict
post_item_response_data_dict = post_item_response_data_instance.to_dict()
# create an instance of PostItemResponseData from a dict
post_item_response_data_from_dict = PostItemResponseData.from_dict(post_item_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


