# AllotmentBlockReleaseBulkUpdateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allotment_block_id** | **str** |  | 
**items** | [**List[AllotmentBlockReleaseBulkUpdateItemSchema]**](AllotmentBlockReleaseBulkUpdateItemSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.allotment_block_release_bulk_update_request_schema import AllotmentBlockReleaseBulkUpdateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AllotmentBlockReleaseBulkUpdateRequestSchema from a JSON string
allotment_block_release_bulk_update_request_schema_instance = AllotmentBlockReleaseBulkUpdateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AllotmentBlockReleaseBulkUpdateRequestSchema.to_json())

# convert the object into a dict
allotment_block_release_bulk_update_request_schema_dict = allotment_block_release_bulk_update_request_schema_instance.to_dict()
# create an instance of AllotmentBlockReleaseBulkUpdateRequestSchema from a dict
allotment_block_release_bulk_update_request_schema_from_dict = AllotmentBlockReleaseBulkUpdateRequestSchema.from_dict(allotment_block_release_bulk_update_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


