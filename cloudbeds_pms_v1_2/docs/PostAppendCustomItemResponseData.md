# PostAppendCustomItemResponseData

Sold product details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sold_product_id** | **str** | Sold product identifier (Usable to void this product in future). | [optional] 
**transaction_id** | **str** | Transaction identifier | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_append_custom_item_response_data import PostAppendCustomItemResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostAppendCustomItemResponseData from a JSON string
post_append_custom_item_response_data_instance = PostAppendCustomItemResponseData.from_json(json)
# print the JSON string representation of the object
print(PostAppendCustomItemResponseData.to_json())

# convert the object into a dict
post_append_custom_item_response_data_dict = post_append_custom_item_response_data_instance.to_dict()
# create an instance of PostAppendCustomItemResponseData from a dict
post_append_custom_item_response_data_from_dict = PostAppendCustomItemResponseData.from_dict(post_append_custom_item_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


