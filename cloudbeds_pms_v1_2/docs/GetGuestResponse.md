# GetGuestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**GetGuestResponseData**](GetGuestResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_guest_response import GetGuestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGuestResponse from a JSON string
get_guest_response_instance = GetGuestResponse.from_json(json)
# print the JSON string representation of the object
print(GetGuestResponse.to_json())

# convert the object into a dict
get_guest_response_dict = get_guest_response_instance.to_dict()
# create an instance of GetGuestResponse from a dict
get_guest_response_from_dict = GetGuestResponse.from_dict(get_guest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


