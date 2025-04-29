# GetAppStateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**GetAppStateResponseData**](GetAppStateResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_app_state_response import GetAppStateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppStateResponse from a JSON string
get_app_state_response_instance = GetAppStateResponse.from_json(json)
# print the JSON string representation of the object
print(GetAppStateResponse.to_json())

# convert the object into a dict
get_app_state_response_dict = get_app_state_response_instance.to_dict()
# create an instance of GetAppStateResponse from a dict
get_app_state_response_from_dict = GetAppStateResponse.from_dict(get_app_state_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


