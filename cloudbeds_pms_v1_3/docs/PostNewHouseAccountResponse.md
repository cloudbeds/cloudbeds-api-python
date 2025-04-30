# PostNewHouseAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**PostNewHouseAccountResponseData**](PostNewHouseAccountResponseData.md) |  | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_new_house_account_response import PostNewHouseAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostNewHouseAccountResponse from a JSON string
post_new_house_account_response_instance = PostNewHouseAccountResponse.from_json(json)
# print the JSON string representation of the object
print(PostNewHouseAccountResponse.to_json())

# convert the object into a dict
post_new_house_account_response_dict = post_new_house_account_response_instance.to_dict()
# create an instance of PostNewHouseAccountResponse from a dict
post_new_house_account_response_from_dict = PostNewHouseAccountResponse.from_dict(post_new_house_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


