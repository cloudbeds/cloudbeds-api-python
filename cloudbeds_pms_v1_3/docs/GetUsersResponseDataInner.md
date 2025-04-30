# GetUsersResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User ID | [optional] 
**first_name** | **str** | First Name | [optional] 
**last_name** | **str** | Last Name | [optional] 
**email** | **str** | Email | [optional] 
**language** | **str** | User Language|Property Default Language. See the full list of available language parameters &lt;a target&#x3D;\&quot;_blank\&quot; href&#x3D;\&quot;https://integrations.cloudbeds.com/hc/en-us/articles/360007144993-FAQ#methods-and-parameters\&quot;&gt;here&lt;/a&gt; | [optional] 
**user_role** | [**GetUsersResponseDataInnerUserRole**](GetUsersResponseDataInnerUserRole.md) |  | [optional] 
**active** | **str** |  | [optional] 
**last_login** | **date** | Date and time of the last login event | [optional] 
**property_id** | **str** | Property numeric identifier | [optional] 
**organization_id** | **str** | Organization ID | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_users_response_data_inner import GetUsersResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsersResponseDataInner from a JSON string
get_users_response_data_inner_instance = GetUsersResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetUsersResponseDataInner.to_json())

# convert the object into a dict
get_users_response_data_inner_dict = get_users_response_data_inner_instance.to_dict()
# create an instance of GetUsersResponseDataInner from a dict
get_users_response_data_inner_from_dict = GetUsersResponseDataInner.from_dict(get_users_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


