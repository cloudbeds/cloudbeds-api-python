# CustomItemResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the custom item | 
**name** | **str** | Item name | 
**property_id** | **str** | Property ID | 
**source_id** | **str** | Source ID (POS app ID) | 
**source_name** | **str** | Source name (POS app name) | 
**app_item_id** | **str** | App item ID | 
**sku** | **str** | SKU | [optional] 
**category_name** | **str** | Category name | [optional] 
**description** | **str** | Item description | [optional] 

## Example

```python
from cloudbeds_pms.models.custom_item_response_schema import CustomItemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CustomItemResponseSchema from a JSON string
custom_item_response_schema_instance = CustomItemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(CustomItemResponseSchema.to_json())

# convert the object into a dict
custom_item_response_schema_dict = custom_item_response_schema_instance.to_dict()
# create an instance of CustomItemResponseSchema from a dict
custom_item_response_schema_from_dict = CustomItemResponseSchema.from_dict(custom_item_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


