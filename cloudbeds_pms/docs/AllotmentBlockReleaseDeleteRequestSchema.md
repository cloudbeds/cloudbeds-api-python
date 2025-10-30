# AllotmentBlockReleaseDeleteRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**allotment_block_id** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.allotment_block_release_delete_request_schema import AllotmentBlockReleaseDeleteRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AllotmentBlockReleaseDeleteRequestSchema from a JSON string
allotment_block_release_delete_request_schema_instance = AllotmentBlockReleaseDeleteRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AllotmentBlockReleaseDeleteRequestSchema.to_json())

# convert the object into a dict
allotment_block_release_delete_request_schema_dict = allotment_block_release_delete_request_schema_instance.to_dict()
# create an instance of AllotmentBlockReleaseDeleteRequestSchema from a dict
allotment_block_release_delete_request_schema_from_dict = AllotmentBlockReleaseDeleteRequestSchema.from_dict(allotment_block_release_delete_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


