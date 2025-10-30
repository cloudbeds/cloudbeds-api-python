# AllotmentBlockReleaseUpdateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**allotment_block_id** | **str** |  | [optional] 
**room_type_id** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**released_quantity** | **int** |  | [optional] 
**released_units** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.allotment_block_release_update_request_schema import AllotmentBlockReleaseUpdateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AllotmentBlockReleaseUpdateRequestSchema from a JSON string
allotment_block_release_update_request_schema_instance = AllotmentBlockReleaseUpdateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AllotmentBlockReleaseUpdateRequestSchema.to_json())

# convert the object into a dict
allotment_block_release_update_request_schema_dict = allotment_block_release_update_request_schema_instance.to_dict()
# create an instance of AllotmentBlockReleaseUpdateRequestSchema from a dict
allotment_block_release_update_request_schema_from_dict = AllotmentBlockReleaseUpdateRequestSchema.from_dict(allotment_block_release_update_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


