# InventoryObjectSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InventoryObjectType**](InventoryObjectType.md) |  | 
**id** | **str** | The ID of the inventory object | 

## Example

```python
from cloudbeds_pms.models.inventory_object_schema import InventoryObjectSchema

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryObjectSchema from a JSON string
inventory_object_schema_instance = InventoryObjectSchema.from_json(json)
# print the JSON string representation of the object
print(InventoryObjectSchema.to_json())

# convert the object into a dict
inventory_object_schema_dict = inventory_object_schema_instance.to_dict()
# create an instance of InventoryObjectSchema from a dict
inventory_object_schema_from_dict = InventoryObjectSchema.from_dict(inventory_object_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


