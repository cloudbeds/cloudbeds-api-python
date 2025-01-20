# GetUsersResponseDataInnerUserRole

Details for the role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Role&#39;s name | [optional] 
**description** | **str** | Role&#39;s description | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_users_response_data_inner_user_role import GetUsersResponseDataInnerUserRole

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsersResponseDataInnerUserRole from a JSON string
get_users_response_data_inner_user_role_instance = GetUsersResponseDataInnerUserRole.from_json(json)
# print the JSON string representation of the object
print(GetUsersResponseDataInnerUserRole.to_json())

# convert the object into a dict
get_users_response_data_inner_user_role_dict = get_users_response_data_inner_user_role_instance.to_dict()
# create an instance of GetUsersResponseDataInnerUserRole from a dict
get_users_response_data_inner_user_role_from_dict = GetUsersResponseDataInnerUserRole.from_dict(get_users_response_data_inner_user_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


