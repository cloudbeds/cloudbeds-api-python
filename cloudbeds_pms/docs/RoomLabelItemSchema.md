# RoomLabelItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Unique label code | 
**title** | **str** | Translated label title | 
**accommodation_privacy_code** | **str** | Accommodation privacy code | 

## Example

```python
from cloudbeds_pms.models.room_label_item_schema import RoomLabelItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RoomLabelItemSchema from a JSON string
room_label_item_schema_instance = RoomLabelItemSchema.from_json(json)
# print the JSON string representation of the object
print(RoomLabelItemSchema.to_json())

# convert the object into a dict
room_label_item_schema_dict = room_label_item_schema_instance.to_dict()
# create an instance of RoomLabelItemSchema from a dict
room_label_item_schema_from_dict = RoomLabelItemSchema.from_dict(room_label_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


