# PostDeleteAllotmentBlockResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_delete_allotment_block_response import PostDeleteAllotmentBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteAllotmentBlockResponse from a JSON string
post_delete_allotment_block_response_instance = PostDeleteAllotmentBlockResponse.from_json(json)
# print the JSON string representation of the object
print(PostDeleteAllotmentBlockResponse.to_json())

# convert the object into a dict
post_delete_allotment_block_response_dict = post_delete_allotment_block_response_instance.to_dict()
# create an instance of PostDeleteAllotmentBlockResponse from a dict
post_delete_allotment_block_response_from_dict = PostDeleteAllotmentBlockResponse.from_dict(post_delete_allotment_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


