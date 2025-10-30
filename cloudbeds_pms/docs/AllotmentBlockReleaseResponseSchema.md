# AllotmentBlockReleaseResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**property_id** | **str** |  | 
**allotment_block_id** | **str** |  | 
**room_type_id** | **str** |  | 
**start_date** | **str** |  | 
**end_date** | **str** |  | 
**released_quantity** | **int** |  | 
**released_units** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.allotment_block_release_response_schema import AllotmentBlockReleaseResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AllotmentBlockReleaseResponseSchema from a JSON string
allotment_block_release_response_schema_instance = AllotmentBlockReleaseResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AllotmentBlockReleaseResponseSchema.to_json())

# convert the object into a dict
allotment_block_release_response_schema_dict = allotment_block_release_response_schema_instance.to_dict()
# create an instance of AllotmentBlockReleaseResponseSchema from a dict
allotment_block_release_response_schema_from_dict = AllotmentBlockReleaseResponseSchema.from_dict(allotment_block_release_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


