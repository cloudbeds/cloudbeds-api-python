# GetUserinfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ID of user | [optional] 
**first_name** | **str** | Authorized users&#39; first name. | [optional] 
**last_name** | **str** | Authorized users&#39; last name. | [optional] 
**email** | **str** | Authorized users&#39; email. | [optional] 
**acl** | **List[str]** | Authorized users&#39; access control list. | [optional] 
**roles** | [**List[GetUserinfoResponseRolesInner]**](GetUserinfoResponseRolesInner.md) | Authorized users&#39; role information. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_userinfo_response import GetUserinfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserinfoResponse from a JSON string
get_userinfo_response_instance = GetUserinfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserinfoResponse.to_json())

# convert the object into a dict
get_userinfo_response_dict = get_userinfo_response_instance.to_dict()
# create an instance of GetUserinfoResponse from a dict
get_userinfo_response_from_dict = GetUserinfoResponse.from_dict(get_userinfo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


