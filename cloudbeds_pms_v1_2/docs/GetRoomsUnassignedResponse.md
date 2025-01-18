# GetRoomsUnassignedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetRoomsUnassignedResponseDataInner]**](GetRoomsUnassignedResponseDataInner.md) | Room Types details | [optional] 
**count** | **int** | Number of results (properties) returned | [optional] 
**total** | **int** | Total number of results, can be more than what was returned | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_rooms_unassigned_response import GetRoomsUnassignedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomsUnassignedResponse from a JSON string
get_rooms_unassigned_response_instance = GetRoomsUnassignedResponse.from_json(json)
# print the JSON string representation of the object
print(GetRoomsUnassignedResponse.to_json())

# convert the object into a dict
get_rooms_unassigned_response_dict = get_rooms_unassigned_response_instance.to_dict()
# create an instance of GetRoomsUnassignedResponse from a dict
get_rooms_unassigned_response_from_dict = GetRoomsUnassignedResponse.from_dict(get_rooms_unassigned_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


