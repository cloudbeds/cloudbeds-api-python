# AssignableRoomsRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | Scope rates and rooms to this room type. Absent returns the reservation&#39;s current type. | [optional] 

## Example

```python
from cloudbeds_pms.models.assignable_rooms_request_schema import AssignableRoomsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AssignableRoomsRequestSchema from a JSON string
assignable_rooms_request_schema_instance = AssignableRoomsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AssignableRoomsRequestSchema.to_json())

# convert the object into a dict
assignable_rooms_request_schema_dict = assignable_rooms_request_schema_instance.to_dict()
# create an instance of AssignableRoomsRequestSchema from a dict
assignable_rooms_request_schema_from_dict = AssignableRoomsRequestSchema.from_dict(assignable_rooms_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


