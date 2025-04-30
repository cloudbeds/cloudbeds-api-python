# PostAccessTokenResponseResourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A type of associated resource | [optional] 
**id** | **str** | Unique ID of associated resource | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_access_token_response_resources_inner import PostAccessTokenResponseResourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccessTokenResponseResourcesInner from a JSON string
post_access_token_response_resources_inner_instance = PostAccessTokenResponseResourcesInner.from_json(json)
# print the JSON string representation of the object
print(PostAccessTokenResponseResourcesInner.to_json())

# convert the object into a dict
post_access_token_response_resources_inner_dict = post_access_token_response_resources_inner_instance.to_dict()
# create an instance of PostAccessTokenResponseResourcesInner from a dict
post_access_token_response_resources_inner_from_dict = PostAccessTokenResponseResourcesInner.from_dict(post_access_token_response_resources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


