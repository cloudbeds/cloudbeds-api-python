# AreaItemResponseSchema

Room type area in response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Area ID | 
**type_code** | **str** | Area type code | 
**position** | **int** | Display position | 
**arrangements** | [**List[ArrangementItemResponseSchema]**](ArrangementItemResponseSchema.md) | Bed arrangements in this area | 

## Example

```python
from cloudbeds_pms.models.area_item_response_schema import AreaItemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AreaItemResponseSchema from a JSON string
area_item_response_schema_instance = AreaItemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AreaItemResponseSchema.to_json())

# convert the object into a dict
area_item_response_schema_dict = area_item_response_schema_instance.to_dict()
# create an instance of AreaItemResponseSchema from a dict
area_item_response_schema_from_dict = AreaItemResponseSchema.from_dict(area_item_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


