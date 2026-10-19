# AllotmentBlockAutoReleaseScheduleBulkSyncItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**release_date** | **str** | Release date and time in Y-m-d H:i:s format | 
**room_type_id** | **str** |  | 
**start_date** | **str** |  | 
**end_date** | **str** |  | 
**release_value_type** | **str** |  | 
**release_value** | **int** |  | 
**release_units** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.allotment_block_auto_release_schedule_bulk_sync_item_schema import AllotmentBlockAutoReleaseScheduleBulkSyncItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AllotmentBlockAutoReleaseScheduleBulkSyncItemSchema from a JSON string
allotment_block_auto_release_schedule_bulk_sync_item_schema_instance = AllotmentBlockAutoReleaseScheduleBulkSyncItemSchema.from_json(json)
# print the JSON string representation of the object
print(AllotmentBlockAutoReleaseScheduleBulkSyncItemSchema.to_json())

# convert the object into a dict
allotment_block_auto_release_schedule_bulk_sync_item_schema_dict = allotment_block_auto_release_schedule_bulk_sync_item_schema_instance.to_dict()
# create an instance of AllotmentBlockAutoReleaseScheduleBulkSyncItemSchema from a dict
allotment_block_auto_release_schedule_bulk_sync_item_schema_from_dict = AllotmentBlockAutoReleaseScheduleBulkSyncItemSchema.from_dict(allotment_block_auto_release_schedule_bulk_sync_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


