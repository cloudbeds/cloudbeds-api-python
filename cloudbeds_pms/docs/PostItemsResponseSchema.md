# PostItemsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PostedItemResponseSchema]**](PostedItemResponseSchema.md) | Array of posted item results, one for each item in the request | 

## Example

```python
from cloudbeds_pms.models.post_items_response_schema import PostItemsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PostItemsResponseSchema from a JSON string
post_items_response_schema_instance = PostItemsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PostItemsResponseSchema.to_json())

# convert the object into a dict
post_items_response_schema_dict = post_items_response_schema_instance.to_dict()
# create an instance of PostItemsResponseSchema from a dict
post_items_response_schema_from_dict = PostItemsResponseSchema.from_dict(post_items_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


