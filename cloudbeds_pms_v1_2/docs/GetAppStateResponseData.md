# GetAppStateResponseData

Integration state details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_state** | **str** | Integration state | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_app_state_response_data import GetAppStateResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppStateResponseData from a JSON string
get_app_state_response_data_instance = GetAppStateResponseData.from_json(json)
# print the JSON string representation of the object
print(GetAppStateResponseData.to_json())

# convert the object into a dict
get_app_state_response_data_dict = get_app_state_response_data_instance.to_dict()
# create an instance of GetAppStateResponseData from a dict
get_app_state_response_data_from_dict = GetAppStateResponseData.from_dict(get_app_state_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


