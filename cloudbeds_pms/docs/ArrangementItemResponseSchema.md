# ArrangementItemResponseSchema

Bed arrangement in response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Arrangement ID | 
**is_default** | **bool** | Whether this is the default arrangement | 
**position** | **int** | Display position | 
**beds** | [**List[BedItemResponseSchema]**](BedItemResponseSchema.md) | Beds in this arrangement | 

## Example

```python
from cloudbeds_pms.models.arrangement_item_response_schema import ArrangementItemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ArrangementItemResponseSchema from a JSON string
arrangement_item_response_schema_instance = ArrangementItemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ArrangementItemResponseSchema.to_json())

# convert the object into a dict
arrangement_item_response_schema_dict = arrangement_item_response_schema_instance.to_dict()
# create an instance of ArrangementItemResponseSchema from a dict
arrangement_item_response_schema_from_dict = ArrangementItemResponseSchema.from_dict(arrangement_item_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


