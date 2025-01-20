# DynamicFilterSchemaAndInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The field to apply the filter on | [optional] 
**operator** | [**FilterOperatorEnumSchema**](FilterOperatorEnumSchema.md) |  | [optional] 
**value** | [**DynamicFilterFieldSchemaValue**](DynamicFilterFieldSchemaValue.md) |  | [optional] 
**var_and** | [**List[DynamicFilterSchemaAndInner]**](DynamicFilterSchemaAndInner.md) | Logical operator grouping filters or nested logical groups | [optional] 
**var_or** | [**List[DynamicFilterSchemaAndInner]**](DynamicFilterSchemaAndInner.md) | Logical operator grouping filters or nested logical groups | [optional] 

## Example

```python
from cloudbeds_pms.models.dynamic_filter_schema_and_inner import DynamicFilterSchemaAndInner

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicFilterSchemaAndInner from a JSON string
dynamic_filter_schema_and_inner_instance = DynamicFilterSchemaAndInner.from_json(json)
# print the JSON string representation of the object
print(DynamicFilterSchemaAndInner.to_json())

# convert the object into a dict
dynamic_filter_schema_and_inner_dict = dynamic_filter_schema_and_inner_instance.to_dict()
# create an instance of DynamicFilterSchemaAndInner from a dict
dynamic_filter_schema_and_inner_from_dict = DynamicFilterSchemaAndInner.from_dict(dynamic_filter_schema_and_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


