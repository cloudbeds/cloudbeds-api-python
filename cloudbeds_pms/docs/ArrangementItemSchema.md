# ArrangementItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **bool** | Whether this is the default arrangement | 
**position** | **int** | Position/order of this arrangement | 
**beds** | [**List[BedItemSchema]**](BedItemSchema.md) | List of beds in this arrangement | 

## Example

```python
from cloudbeds_pms.models.arrangement_item_schema import ArrangementItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ArrangementItemSchema from a JSON string
arrangement_item_schema_instance = ArrangementItemSchema.from_json(json)
# print the JSON string representation of the object
print(ArrangementItemSchema.to_json())

# convert the object into a dict
arrangement_item_schema_dict = arrangement_item_schema_instance.to_dict()
# create an instance of ArrangementItemSchema from a dict
arrangement_item_schema_from_dict = ArrangementItemSchema.from_dict(arrangement_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


