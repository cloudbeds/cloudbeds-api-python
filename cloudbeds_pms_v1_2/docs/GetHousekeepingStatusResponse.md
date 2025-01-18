# GetHousekeepingStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetHousekeepingStatusResponseDataInner]**](GetHousekeepingStatusResponseDataInner.md) |  | [optional] 
**count** | **int** | Results in current request | [optional] 
**total** | **int** | Total number of results for supplied parameters | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_housekeeping_status_response import GetHousekeepingStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHousekeepingStatusResponse from a JSON string
get_housekeeping_status_response_instance = GetHousekeepingStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetHousekeepingStatusResponse.to_json())

# convert the object into a dict
get_housekeeping_status_response_dict = get_housekeeping_status_response_instance.to_dict()
# create an instance of GetHousekeepingStatusResponse from a dict
get_housekeeping_status_response_from_dict = GetHousekeepingStatusResponse.from_dict(get_housekeeping_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


