# GetRoomTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetRoomTypesResponseDataInner]**](GetRoomTypesResponseDataInner.md) | Room Types details | [optional] 
**count** | **int** | Number of results in this page | [optional] 
**total** | **int** | Total number of results | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_room_types_response import GetRoomTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomTypesResponse from a JSON string
get_room_types_response_instance = GetRoomTypesResponse.from_json(json)
# print the JSON string representation of the object
print(GetRoomTypesResponse.to_json())

# convert the object into a dict
get_room_types_response_dict = get_room_types_response_instance.to_dict()
# create an instance of GetRoomTypesResponse from a dict
get_room_types_response_from_dict = GetRoomTypesResponse.from_dict(get_room_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


