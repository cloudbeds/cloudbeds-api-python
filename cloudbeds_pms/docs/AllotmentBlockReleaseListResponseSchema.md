# AllotmentBlockReleaseListResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AllotmentBlockReleaseResponseSchema]**](AllotmentBlockReleaseResponseSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.allotment_block_release_list_response_schema import AllotmentBlockReleaseListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AllotmentBlockReleaseListResponseSchema from a JSON string
allotment_block_release_list_response_schema_instance = AllotmentBlockReleaseListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AllotmentBlockReleaseListResponseSchema.to_json())

# convert the object into a dict
allotment_block_release_list_response_schema_dict = allotment_block_release_list_response_schema_instance.to_dict()
# create an instance of AllotmentBlockReleaseListResponseSchema from a dict
allotment_block_release_list_response_schema_from_dict = AllotmentBlockReleaseListResponseSchema.from_dict(allotment_block_release_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


