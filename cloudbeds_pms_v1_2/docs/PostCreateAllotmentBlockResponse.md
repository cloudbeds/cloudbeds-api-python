# PostCreateAllotmentBlockResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Date on or after which each returned allotmentBlock applies | [optional] 
**end_date** | **date** | Date on or before which each returned allotmentBlock applies | [optional] 
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[PostCreateAllotmentBlockResponseDataInner]**](PostCreateAllotmentBlockResponseDataInner.md) | Allotment Blocks | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_create_allotment_block_response import PostCreateAllotmentBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateAllotmentBlockResponse from a JSON string
post_create_allotment_block_response_instance = PostCreateAllotmentBlockResponse.from_json(json)
# print the JSON string representation of the object
print(PostCreateAllotmentBlockResponse.to_json())

# convert the object into a dict
post_create_allotment_block_response_dict = post_create_allotment_block_response_instance.to_dict()
# create an instance of PostCreateAllotmentBlockResponse from a dict
post_create_allotment_block_response_from_dict = PostCreateAllotmentBlockResponse.from_dict(post_create_allotment_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


