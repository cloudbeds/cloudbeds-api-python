# GetHotelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetHotelsResponseDataInner]**](GetHotelsResponseDataInner.md) | Information about the hotels | [optional] 
**count** | **int** | Number of results in this page | [optional] 
**total** | **int** | Total number of results | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_hotels_response import GetHotelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHotelsResponse from a JSON string
get_hotels_response_instance = GetHotelsResponse.from_json(json)
# print the JSON string representation of the object
print(GetHotelsResponse.to_json())

# convert the object into a dict
get_hotels_response_dict = get_hotels_response_instance.to_dict()
# create an instance of GetHotelsResponse from a dict
get_hotels_response_from_dict = GetHotelsResponse.from_dict(get_hotels_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


