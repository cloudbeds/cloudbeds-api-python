# DeletedUnitItem

A unit (room) that has been deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unit ID | 
**property_id** | **int** | Property ID | 
**room_type_id** | **int** | Room type (accommodation) ID | 
**name** | **str** | Unit name at the time it was deleted | 
**archived_at** | **datetime** | When the unit was archived. | 

## Example

```python
from cloudbeds_pms.models.deleted_unit_item import DeletedUnitItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedUnitItem from a JSON string
deleted_unit_item_instance = DeletedUnitItem.from_json(json)
# print the JSON string representation of the object
print(DeletedUnitItem.to_json())

# convert the object into a dict
deleted_unit_item_dict = deleted_unit_item_instance.to_dict()
# create an instance of DeletedUnitItem from a dict
deleted_unit_item_from_dict = DeletedUnitItem.from_dict(deleted_unit_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


