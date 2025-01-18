# GetAllotmentBlocksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**count** | **int** | Number of allotment blocks returned | [optional] 
**total** | **int** | Total number of allotment blocks | [optional] 
**data** | [**List[GetAllotmentBlocksResponseDataInner]**](GetAllotmentBlocksResponseDataInner.md) | Allotment Blocks | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_allotment_blocks_response import GetAllotmentBlocksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllotmentBlocksResponse from a JSON string
get_allotment_blocks_response_instance = GetAllotmentBlocksResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllotmentBlocksResponse.to_json())

# convert the object into a dict
get_allotment_blocks_response_dict = get_allotment_blocks_response_instance.to_dict()
# create an instance of GetAllotmentBlocksResponse from a dict
get_allotment_blocks_response_from_dict = GetAllotmentBlocksResponse.from_dict(get_allotment_blocks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


