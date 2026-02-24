# GetRoomLabelsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**List[RoomLabelItemSchema]**](RoomLabelItemSchema.md) | List of room labels in the catalog | 

## Example

```python
from cloudbeds_pms.models.get_room_labels_response_schema import GetRoomLabelsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomLabelsResponseSchema from a JSON string
get_room_labels_response_schema_instance = GetRoomLabelsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GetRoomLabelsResponseSchema.to_json())

# convert the object into a dict
get_room_labels_response_schema_dict = get_room_labels_response_schema_instance.to_dict()
# create an instance of GetRoomLabelsResponseSchema from a dict
get_room_labels_response_schema_from_dict = GetRoomLabelsResponseSchema.from_dict(get_room_labels_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


