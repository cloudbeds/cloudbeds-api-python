# PostCustomItemResponseData

Sold product details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sold_product_id** | **str** | Sold product identifier (Usable to void this product in future). | [optional] 
**external_relation_id** | **str** | Same as sold product ID in case of this endpoint. Together with external relation kind ITEM_POS it can be used to get transaction from Accounting API | [optional] 
**notice** | **str** | In case that a referenceID was sent, for second time, this field will alert that nothing was created or updated. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_custom_item_response_data import PostCustomItemResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostCustomItemResponseData from a JSON string
post_custom_item_response_data_instance = PostCustomItemResponseData.from_json(json)
# print the JSON string representation of the object
print(PostCustomItemResponseData.to_json())

# convert the object into a dict
post_custom_item_response_data_dict = post_custom_item_response_data_instance.to_dict()
# create an instance of PostCustomItemResponseData from a dict
post_custom_item_response_data_from_dict = PostCustomItemResponseData.from_dict(post_custom_item_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


