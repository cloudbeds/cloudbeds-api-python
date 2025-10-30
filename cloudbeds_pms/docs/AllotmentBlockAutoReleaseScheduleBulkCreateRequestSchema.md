# AllotmentBlockAutoReleaseScheduleBulkCreateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allotment_block_id** | **str** |  | 
**items** | [**List[AllotmentBlockAutoReleaseScheduleBulkCreateItemSchema]**](AllotmentBlockAutoReleaseScheduleBulkCreateItemSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.allotment_block_auto_release_schedule_bulk_create_request_schema import AllotmentBlockAutoReleaseScheduleBulkCreateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AllotmentBlockAutoReleaseScheduleBulkCreateRequestSchema from a JSON string
allotment_block_auto_release_schedule_bulk_create_request_schema_instance = AllotmentBlockAutoReleaseScheduleBulkCreateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AllotmentBlockAutoReleaseScheduleBulkCreateRequestSchema.to_json())

# convert the object into a dict
allotment_block_auto_release_schedule_bulk_create_request_schema_dict = allotment_block_auto_release_schedule_bulk_create_request_schema_instance.to_dict()
# create an instance of AllotmentBlockAutoReleaseScheduleBulkCreateRequestSchema from a dict
allotment_block_auto_release_schedule_bulk_create_request_schema_from_dict = AllotmentBlockAutoReleaseScheduleBulkCreateRequestSchema.from_dict(allotment_block_auto_release_schedule_bulk_create_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


