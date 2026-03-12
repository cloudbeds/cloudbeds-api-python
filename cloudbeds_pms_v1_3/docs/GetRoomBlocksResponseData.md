# GetRoomBlocksResponseData

Property room block details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Property ID | [optional] 
**room_blocks** | [**List[GetRoomBlocksResponseDataRoomBlocksInner]**](GetRoomBlocksResponseDataRoomBlocksInner.md) | Room blocks for the property | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_room_blocks_response_data import GetRoomBlocksResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomBlocksResponseData from a JSON string
get_room_blocks_response_data_instance = GetRoomBlocksResponseData.from_json(json)
# print the JSON string representation of the object
print(GetRoomBlocksResponseData.to_json())

# convert the object into a dict
get_room_blocks_response_data_dict = get_room_blocks_response_data_instance.to_dict()
# create an instance of GetRoomBlocksResponseData from a dict
get_room_blocks_response_data_from_dict = GetRoomBlocksResponseData.from_dict(get_room_blocks_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


