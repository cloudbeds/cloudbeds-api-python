# AllotmentBlockReleaseBulkCreateItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** |  | 
**start_date** | **str** |  | 
**end_date** | **str** |  | 
**released_quantity** | **int** |  | 
**released_units** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.allotment_block_release_bulk_create_item_schema import AllotmentBlockReleaseBulkCreateItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AllotmentBlockReleaseBulkCreateItemSchema from a JSON string
allotment_block_release_bulk_create_item_schema_instance = AllotmentBlockReleaseBulkCreateItemSchema.from_json(json)
# print the JSON string representation of the object
print(AllotmentBlockReleaseBulkCreateItemSchema.to_json())

# convert the object into a dict
allotment_block_release_bulk_create_item_schema_dict = allotment_block_release_bulk_create_item_schema_instance.to_dict()
# create an instance of AllotmentBlockReleaseBulkCreateItemSchema from a dict
allotment_block_release_bulk_create_item_schema_from_dict = AllotmentBlockReleaseBulkCreateItemSchema.from_dict(allotment_block_release_bulk_create_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


