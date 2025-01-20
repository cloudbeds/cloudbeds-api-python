# DynamicFilterSchema

Represents a logical group of filters with keys like 'and' or 'or'

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[DynamicFilterSchemaAndInner]**](DynamicFilterSchemaAndInner.md) | Logical operator grouping filters or nested logical groups | [optional] 
**var_or** | [**List[DynamicFilterSchemaAndInner]**](DynamicFilterSchemaAndInner.md) | Logical operator grouping filters or nested logical groups | [optional] 

## Example

```python
from cloudbeds_pms.models.dynamic_filter_schema import DynamicFilterSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicFilterSchema from a JSON string
dynamic_filter_schema_instance = DynamicFilterSchema.from_json(json)
# print the JSON string representation of the object
print(DynamicFilterSchema.to_json())

# convert the object into a dict
dynamic_filter_schema_dict = dynamic_filter_schema_instance.to_dict()
# create an instance of DynamicFilterSchema from a dict
dynamic_filter_schema_from_dict = DynamicFilterSchema.from_dict(dynamic_filter_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


