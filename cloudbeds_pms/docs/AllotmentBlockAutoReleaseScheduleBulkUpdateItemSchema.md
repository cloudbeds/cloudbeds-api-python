# AllotmentBlockAutoReleaseScheduleBulkUpdateItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**release_date** | **str** |  | [optional] 
**allotment_block_id** | **str** |  | [optional] 
**room_type_id** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**release_value_type** | **str** |  | [optional] 
**release_value** | **int** |  | [optional] 
**release_units** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.allotment_block_auto_release_schedule_bulk_update_item_schema import AllotmentBlockAutoReleaseScheduleBulkUpdateItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AllotmentBlockAutoReleaseScheduleBulkUpdateItemSchema from a JSON string
allotment_block_auto_release_schedule_bulk_update_item_schema_instance = AllotmentBlockAutoReleaseScheduleBulkUpdateItemSchema.from_json(json)
# print the JSON string representation of the object
print(AllotmentBlockAutoReleaseScheduleBulkUpdateItemSchema.to_json())

# convert the object into a dict
allotment_block_auto_release_schedule_bulk_update_item_schema_dict = allotment_block_auto_release_schedule_bulk_update_item_schema_instance.to_dict()
# create an instance of AllotmentBlockAutoReleaseScheduleBulkUpdateItemSchema from a dict
allotment_block_auto_release_schedule_bulk_update_item_schema_from_dict = AllotmentBlockAutoReleaseScheduleBulkUpdateItemSchema.from_dict(allotment_block_auto_release_schedule_bulk_update_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


