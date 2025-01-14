# SortFieldSchema

Represents a logical group of filters with keys like 'and' or 'or'

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The field to apply the sort on | [optional] 
**direction** | [**DirectionEnumSchema**](DirectionEnumSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.sort_field_schema import SortFieldSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SortFieldSchema from a JSON string
sort_field_schema_instance = SortFieldSchema.from_json(json)
# print the JSON string representation of the object
print(SortFieldSchema.to_json())

# convert the object into a dict
sort_field_schema_dict = sort_field_schema_instance.to_dict()
# create an instance of SortFieldSchema from a dict
sort_field_schema_from_dict = SortFieldSchema.from_dict(sort_field_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


