# CustomItemListResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomItemResponseSchema]**](CustomItemResponseSchema.md) |  | 
**total** | **int** | Total number of items | 

## Example

```python
from cloudbeds_pms.models.custom_item_list_response_schema import CustomItemListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CustomItemListResponseSchema from a JSON string
custom_item_list_response_schema_instance = CustomItemListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(CustomItemListResponseSchema.to_json())

# convert the object into a dict
custom_item_list_response_schema_dict = custom_item_list_response_schema_instance.to_dict()
# create an instance of CustomItemListResponseSchema from a dict
custom_item_list_response_schema_from_dict = CustomItemListResponseSchema.from_dict(custom_item_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


