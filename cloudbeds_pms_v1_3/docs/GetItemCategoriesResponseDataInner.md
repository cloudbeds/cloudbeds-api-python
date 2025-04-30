# GetItemCategoriesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | Category unique identifier | [optional] 
**category_name** | **str** | Category name | [optional] 
**category_code** | **str** | Category code | [optional] 
**category_color** | **str** | Category color (like #3b7be7) | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_item_categories_response_data_inner import GetItemCategoriesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetItemCategoriesResponseDataInner from a JSON string
get_item_categories_response_data_inner_instance = GetItemCategoriesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetItemCategoriesResponseDataInner.to_json())

# convert the object into a dict
get_item_categories_response_data_inner_dict = get_item_categories_response_data_inner_instance.to_dict()
# create an instance of GetItemCategoriesResponseDataInner from a dict
get_item_categories_response_data_inner_from_dict = GetItemCategoriesResponseDataInner.from_dict(get_item_categories_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


