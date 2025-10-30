# AllotmentBlockReleaseListRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_ids** | **str** | Filter by room type IDs. Comma-separated list of room type IDs. Values passed as strings to avoid precision loss | [optional] 
**release_date** | **str** | Filter by release date. Use single date (2025-01-01) or range (2025-01-01..2025-01-31) | [optional] 
**start_date** | **str** | Filter by schedule start date. Use single date (2025-01-01) or range (2025-01-01..2025-01-31) | [optional] 
**end_date** | **str** | Filter by schedule end date. Use single date (2025-01-01) or range (2025-01-01..2025-01-31) | [optional] 

## Example

```python
from cloudbeds_pms.models.allotment_block_release_list_request_schema import AllotmentBlockReleaseListRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AllotmentBlockReleaseListRequestSchema from a JSON string
allotment_block_release_list_request_schema_instance = AllotmentBlockReleaseListRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AllotmentBlockReleaseListRequestSchema.to_json())

# convert the object into a dict
allotment_block_release_list_request_schema_dict = allotment_block_release_list_request_schema_instance.to_dict()
# create an instance of AllotmentBlockReleaseListRequestSchema from a dict
allotment_block_release_list_request_schema_from_dict = AllotmentBlockReleaseListRequestSchema.from_dict(allotment_block_release_list_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


