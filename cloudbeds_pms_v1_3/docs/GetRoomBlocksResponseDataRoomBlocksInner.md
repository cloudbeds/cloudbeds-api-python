# GetRoomBlocksResponseDataRoomBlocksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_block_id** | **str** | Room block ID | [optional] 
**room_block_type** | **str** | Room block type. ‘blocked’ - Room block. ‘out_of_service’ - Out of service block. &#39;courtesy_hold&#39; - Courtesy hold block. | [optional] 
**room_block_reason** | **str** | Room block reason | [optional] 
**start_date** | **date** | Room block start date | [optional] 
**end_date** | **date** | Room block end date | [optional] 
**rooms** | [**List[GetRoomBlocksResponseDataRoomBlocksInnerRoomsInner]**](GetRoomBlocksResponseDataRoomBlocksInnerRoomsInner.md) | All rooms for Block ID. For properties using split inventory, this includes both source rooms (explicitly requested) and linked rooms (automatically added based on shared inventory configuration). | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_room_blocks_response_data_room_blocks_inner import GetRoomBlocksResponseDataRoomBlocksInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomBlocksResponseDataRoomBlocksInner from a JSON string
get_room_blocks_response_data_room_blocks_inner_instance = GetRoomBlocksResponseDataRoomBlocksInner.from_json(json)
# print the JSON string representation of the object
print(GetRoomBlocksResponseDataRoomBlocksInner.to_json())

# convert the object into a dict
get_room_blocks_response_data_room_blocks_inner_dict = get_room_blocks_response_data_room_blocks_inner_instance.to_dict()
# create an instance of GetRoomBlocksResponseDataRoomBlocksInner from a dict
get_room_blocks_response_data_room_blocks_inner_from_dict = GetRoomBlocksResponseDataRoomBlocksInner.from_dict(get_room_blocks_response_data_room_blocks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


