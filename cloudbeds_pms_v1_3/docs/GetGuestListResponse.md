# GetGuestListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**Dict[str, GetGuestListResponseDataValue]**](GetGuestListResponseDataValue.md) | Details for the guest linked to the property (key is the Guest ID) | [optional] 
**count** | **int** | Number of results returned | [optional] 
**total** | **int** | Total number of results | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_guest_list_response import GetGuestListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGuestListResponse from a JSON string
get_guest_list_response_instance = GetGuestListResponse.from_json(json)
# print the JSON string representation of the object
print(GetGuestListResponse.to_json())

# convert the object into a dict
get_guest_list_response_dict = get_guest_list_response_instance.to_dict()
# create an instance of GetGuestListResponse from a dict
get_guest_list_response_from_dict = GetGuestListResponse.from_dict(get_guest_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


