# AllotmentBlockReleaseBulkCreateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allotment_block_id** | **str** |  | 
**items** | [**List[AllotmentBlockReleaseBulkCreateItemSchema]**](AllotmentBlockReleaseBulkCreateItemSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.allotment_block_release_bulk_create_request_schema import AllotmentBlockReleaseBulkCreateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AllotmentBlockReleaseBulkCreateRequestSchema from a JSON string
allotment_block_release_bulk_create_request_schema_instance = AllotmentBlockReleaseBulkCreateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AllotmentBlockReleaseBulkCreateRequestSchema.to_json())

# convert the object into a dict
allotment_block_release_bulk_create_request_schema_dict = allotment_block_release_bulk_create_request_schema_instance.to_dict()
# create an instance of AllotmentBlockReleaseBulkCreateRequestSchema from a dict
allotment_block_release_bulk_create_request_schema_from_dict = AllotmentBlockReleaseBulkCreateRequestSchema.from_dict(allotment_block_release_bulk_create_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


