# PostCRMCacheRemoveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_crm_cache_remove_response import PostCRMCacheRemoveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostCRMCacheRemoveResponse from a JSON string
post_crm_cache_remove_response_instance = PostCRMCacheRemoveResponse.from_json(json)
# print the JSON string representation of the object
print(PostCRMCacheRemoveResponse.to_json())

# convert the object into a dict
post_crm_cache_remove_response_dict = post_crm_cache_remove_response_instance.to_dict()
# create an instance of PostCRMCacheRemoveResponse from a dict
post_crm_cache_remove_response_from_dict = PostCRMCacheRemoveResponse.from_dict(post_crm_cache_remove_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


