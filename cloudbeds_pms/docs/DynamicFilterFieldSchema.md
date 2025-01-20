# DynamicFilterFieldSchema

Represents a single filter condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The field to apply the filter on | [optional] 
**operator** | [**FilterOperatorEnumSchema**](FilterOperatorEnumSchema.md) |  | [optional] 
**value** | [**DynamicFilterFieldSchemaValue**](DynamicFilterFieldSchemaValue.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.dynamic_filter_field_schema import DynamicFilterFieldSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicFilterFieldSchema from a JSON string
dynamic_filter_field_schema_instance = DynamicFilterFieldSchema.from_json(json)
# print the JSON string representation of the object
print(DynamicFilterFieldSchema.to_json())

# convert the object into a dict
dynamic_filter_field_schema_dict = dynamic_filter_field_schema_instance.to_dict()
# create an instance of DynamicFilterFieldSchema from a dict
dynamic_filter_field_schema_from_dict = DynamicFilterFieldSchema.from_dict(dynamic_filter_field_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


