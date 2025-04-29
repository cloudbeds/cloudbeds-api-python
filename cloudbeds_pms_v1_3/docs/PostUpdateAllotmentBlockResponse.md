# PostUpdateAllotmentBlockResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[PostUpdateAllotmentBlockResponseDataInner]**](PostUpdateAllotmentBlockResponseDataInner.md) | Allotment Blocks | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_update_allotment_block_response import PostUpdateAllotmentBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostUpdateAllotmentBlockResponse from a JSON string
post_update_allotment_block_response_instance = PostUpdateAllotmentBlockResponse.from_json(json)
# print the JSON string representation of the object
print(PostUpdateAllotmentBlockResponse.to_json())

# convert the object into a dict
post_update_allotment_block_response_dict = post_update_allotment_block_response_instance.to_dict()
# create an instance of PostUpdateAllotmentBlockResponse from a dict
post_update_allotment_block_response_from_dict = PostUpdateAllotmentBlockResponse.from_dict(post_update_allotment_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


