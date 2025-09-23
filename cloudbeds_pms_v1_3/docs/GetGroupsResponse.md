# GetGroupsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success | [optional] 
**data** | [**List[GetGroupsResponseDataInner]**](GetGroupsResponseDataInner.md) | Data | [optional] 
**cell_phone** | **str** | \&quot;fax\&quot;} data.contacts.phones.type Phone type | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_groups_response import GetGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsResponse from a JSON string
get_groups_response_instance = GetGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(GetGroupsResponse.to_json())

# convert the object into a dict
get_groups_response_dict = get_groups_response_instance.to_dict()
# create an instance of GetGroupsResponse from a dict
get_groups_response_from_dict = GetGroupsResponse.from_dict(get_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


