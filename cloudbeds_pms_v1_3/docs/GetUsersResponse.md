# GetUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetUsersResponseDataInner]**](GetUsersResponseDataInner.md) | Details for the users | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_users_response import GetUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsersResponse from a JSON string
get_users_response_instance = GetUsersResponse.from_json(json)
# print the JSON string representation of the object
print(GetUsersResponse.to_json())

# convert the object into a dict
get_users_response_dict = get_users_response_instance.to_dict()
# create an instance of GetUsersResponse from a dict
get_users_response_from_dict = GetUsersResponse.from_dict(get_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


