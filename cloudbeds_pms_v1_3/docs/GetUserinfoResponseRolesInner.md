# GetUserinfoResponseRolesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the role. | [optional] 
**name** | **str** | Name of the role. | [optional] 
**description** | **str** | Description of the role. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_userinfo_response_roles_inner import GetUserinfoResponseRolesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserinfoResponseRolesInner from a JSON string
get_userinfo_response_roles_inner_instance = GetUserinfoResponseRolesInner.from_json(json)
# print the JSON string representation of the object
print(GetUserinfoResponseRolesInner.to_json())

# convert the object into a dict
get_userinfo_response_roles_inner_dict = get_userinfo_response_roles_inner_instance.to_dict()
# create an instance of GetUserinfoResponseRolesInner from a dict
get_userinfo_response_roles_inner_from_dict = GetUserinfoResponseRolesInner.from_dict(get_userinfo_response_roles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


