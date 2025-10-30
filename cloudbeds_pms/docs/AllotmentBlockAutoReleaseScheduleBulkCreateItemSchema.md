# AllotmentBlockAutoReleaseScheduleBulkCreateItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_date** | **str** |  | 
**room_type_id** | **str** |  | 
**start_date** | **str** |  | 
**end_date** | **str** |  | 
**release_value_type** | **str** |  | 
**release_value** | **int** |  | 
**release_units** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.allotment_block_auto_release_schedule_bulk_create_item_schema import AllotmentBlockAutoReleaseScheduleBulkCreateItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AllotmentBlockAutoReleaseScheduleBulkCreateItemSchema from a JSON string
allotment_block_auto_release_schedule_bulk_create_item_schema_instance = AllotmentBlockAutoReleaseScheduleBulkCreateItemSchema.from_json(json)
# print the JSON string representation of the object
print(AllotmentBlockAutoReleaseScheduleBulkCreateItemSchema.to_json())

# convert the object into a dict
allotment_block_auto_release_schedule_bulk_create_item_schema_dict = allotment_block_auto_release_schedule_bulk_create_item_schema_instance.to_dict()
# create an instance of AllotmentBlockAutoReleaseScheduleBulkCreateItemSchema from a dict
allotment_block_auto_release_schedule_bulk_create_item_schema_from_dict = AllotmentBlockAutoReleaseScheduleBulkCreateItemSchema.from_dict(allotment_block_auto_release_schedule_bulk_create_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


