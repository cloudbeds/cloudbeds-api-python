# PostAccessTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Authenticated access token. | [optional] 
**token_type** | **str** | The type of the access token authenticated. | [optional] 
**expires_in** | **int** | The expiration time of the access token in seconds. | [optional] 
**refresh_token** | **str** | A token to refresh your access token without performing the full auth flow. | [optional] 
**resources** | [**List[PostAccessTokenResponseResourcesInner]**](PostAccessTokenResponseResourcesInner.md) | List of resources associated with the token during consent | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_access_token_response import PostAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccessTokenResponse from a JSON string
post_access_token_response_instance = PostAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print(PostAccessTokenResponse.to_json())

# convert the object into a dict
post_access_token_response_dict = post_access_token_response_instance.to_dict()
# create an instance of PostAccessTokenResponse from a dict
post_access_token_response_from_dict = PostAccessTokenResponse.from_dict(post_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


