# PutRoomBlockResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**property_id** | **str** | Property ID | [optional] 
**room_block_id** | **str** | Room block ID | [optional] 
**room_block_type** | **str** | Room block type. &#39;blocked&#39; - Room block. &#39;out_of_service&#39; - Out of service block. &#39;courtesy_hold&#39; - Courtesy hold. | [optional] 
**room_block_reason** | **str** | Room block reason | [optional] 
**start_date** | **date** | Room block start date | [optional] 
**end_date** | **date** | Room block end date | [optional] 
**rooms** | [**List[PostRoomBlockResponseRoomsInner]**](PostRoomBlockResponseRoomsInner.md) | All rooms for room block. For properties using split inventory, this includes both source rooms (explicitly requested) and linked rooms (automatically added based on shared inventory configuration). | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false).  If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.put_room_block_response import PutRoomBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutRoomBlockResponse from a JSON string
put_room_block_response_instance = PutRoomBlockResponse.from_json(json)
# print the JSON string representation of the object
print(PutRoomBlockResponse.to_json())

# convert the object into a dict
put_room_block_response_dict = put_room_block_response_instance.to_dict()
# create an instance of PutRoomBlockResponse from a dict
put_room_block_response_from_dict = PutRoomBlockResponse.from_dict(put_room_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


