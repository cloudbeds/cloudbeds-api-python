# QueryParameterDynamicFilterSchemaFilters

This parameter should be formatted as a list of strings separated by ;

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[DynamicFilterSchemaAndInner]**](DynamicFilterSchemaAndInner.md) | Logical operator grouping filters or nested logical groups | [optional] 
**var_or** | [**List[DynamicFilterSchemaAndInner]**](DynamicFilterSchemaAndInner.md) | Logical operator grouping filters or nested logical groups | [optional] 

## Example

```python
from cloudbeds_pms.models.query_parameter_dynamic_filter_schema_filters import QueryParameterDynamicFilterSchemaFilters

# TODO update the JSON string below
json = "{}"
# create an instance of QueryParameterDynamicFilterSchemaFilters from a JSON string
query_parameter_dynamic_filter_schema_filters_instance = QueryParameterDynamicFilterSchemaFilters.from_json(json)
# print the JSON string representation of the object
print(QueryParameterDynamicFilterSchemaFilters.to_json())

# convert the object into a dict
query_parameter_dynamic_filter_schema_filters_dict = query_parameter_dynamic_filter_schema_filters_instance.to_dict()
# create an instance of QueryParameterDynamicFilterSchemaFilters from a dict
query_parameter_dynamic_filter_schema_filters_from_dict = QueryParameterDynamicFilterSchemaFilters.from_dict(query_parameter_dynamic_filter_schema_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


