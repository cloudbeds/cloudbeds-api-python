# AllotmentBlockAutoReleaseScheduleBulkUpdateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allotment_block_id** | **str** |  | 
**items** | [**List[AllotmentBlockAutoReleaseScheduleBulkUpdateItemSchema]**](AllotmentBlockAutoReleaseScheduleBulkUpdateItemSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.allotment_block_auto_release_schedule_bulk_update_request_schema import AllotmentBlockAutoReleaseScheduleBulkUpdateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AllotmentBlockAutoReleaseScheduleBulkUpdateRequestSchema from a JSON string
allotment_block_auto_release_schedule_bulk_update_request_schema_instance = AllotmentBlockAutoReleaseScheduleBulkUpdateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AllotmentBlockAutoReleaseScheduleBulkUpdateRequestSchema.to_json())

# convert the object into a dict
allotment_block_auto_release_schedule_bulk_update_request_schema_dict = allotment_block_auto_release_schedule_bulk_update_request_schema_instance.to_dict()
# create an instance of AllotmentBlockAutoReleaseScheduleBulkUpdateRequestSchema from a dict
allotment_block_auto_release_schedule_bulk_update_request_schema_from_dict = AllotmentBlockAutoReleaseScheduleBulkUpdateRequestSchema.from_dict(allotment_block_auto_release_schedule_bulk_update_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


