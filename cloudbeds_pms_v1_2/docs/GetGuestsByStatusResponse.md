# GetGuestsByStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetGuestsByStatusResponseDataInner]**](GetGuestsByStatusResponseDataInner.md) | Details for the guest | [optional] 
**count** | **int** | Number of results returned | [optional] 
**total** | **int** | Total number of results | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_guests_by_status_response import GetGuestsByStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGuestsByStatusResponse from a JSON string
get_guests_by_status_response_instance = GetGuestsByStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetGuestsByStatusResponse.to_json())

# convert the object into a dict
get_guests_by_status_response_dict = get_guests_by_status_response_instance.to_dict()
# create an instance of GetGuestsByStatusResponse from a dict
get_guests_by_status_response_from_dict = GetGuestsByStatusResponse.from_dict(get_guests_by_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


