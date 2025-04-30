# PostAccessTokenCheckResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **str** | True if the access_token is valid. False otherwise. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_access_token_check_response import PostAccessTokenCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccessTokenCheckResponse from a JSON string
post_access_token_check_response_instance = PostAccessTokenCheckResponse.from_json(json)
# print the JSON string representation of the object
print(PostAccessTokenCheckResponse.to_json())

# convert the object into a dict
post_access_token_check_response_dict = post_access_token_check_response_instance.to_dict()
# create an instance of PostAccessTokenCheckResponse from a dict
post_access_token_check_response_from_dict = PostAccessTokenCheckResponse.from_dict(post_access_token_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


