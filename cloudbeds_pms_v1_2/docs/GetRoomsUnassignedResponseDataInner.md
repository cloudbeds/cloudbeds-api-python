# GetRoomsUnassignedResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Property ID | [optional] 
**rooms** | [**List[GetRoomsUnassignedResponseDataInnerRoomsInner]**](GetRoomsUnassignedResponseDataInnerRoomsInner.md) | All rooms for property ID | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_rooms_unassigned_response_data_inner import GetRoomsUnassignedResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomsUnassignedResponseDataInner from a JSON string
get_rooms_unassigned_response_data_inner_instance = GetRoomsUnassignedResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetRoomsUnassignedResponseDataInner.to_json())

# convert the object into a dict
get_rooms_unassigned_response_data_inner_dict = get_rooms_unassigned_response_data_inner_instance.to_dict()
# create an instance of GetRoomsUnassignedResponseDataInner from a dict
get_rooms_unassigned_response_data_inner_from_dict = GetRoomsUnassignedResponseDataInner.from_dict(get_rooms_unassigned_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


