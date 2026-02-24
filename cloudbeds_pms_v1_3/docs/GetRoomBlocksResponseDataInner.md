# GetRoomBlocksResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_block_id** | **str** | Room block ID | [optional] 
**room_block_reason** | **str** | Room block reason | [optional] 
**start_date** | **date** | Room block start date | [optional] 
**end_date** | **date** | Room block end date | [optional] 
**rooms** | [**List[GetRoomBlocksResponseDataInnerRoomsInner]**](GetRoomBlocksResponseDataInnerRoomsInner.md) | All rooms for Block ID | [optional] 
**count** | **int** | Number of results (properties) returned. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_room_blocks_response_data_inner import GetRoomBlocksResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomBlocksResponseDataInner from a JSON string
get_room_blocks_response_data_inner_instance = GetRoomBlocksResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetRoomBlocksResponseDataInner.to_json())

# convert the object into a dict
get_room_blocks_response_data_inner_dict = get_room_blocks_response_data_inner_instance.to_dict()
# create an instance of GetRoomBlocksResponseDataInner from a dict
get_room_blocks_response_data_inner_from_dict = GetRoomBlocksResponseDataInner.from_dict(get_room_blocks_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


