# QueryParameterDynamicFilterSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**QueryParameterDynamicFilterSchemaFilters**](QueryParameterDynamicFilterSchemaFilters.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.query_parameter_dynamic_filter_schema import QueryParameterDynamicFilterSchema

# TODO update the JSON string below
json = "{}"
# create an instance of QueryParameterDynamicFilterSchema from a JSON string
query_parameter_dynamic_filter_schema_instance = QueryParameterDynamicFilterSchema.from_json(json)
# print the JSON string representation of the object
print(QueryParameterDynamicFilterSchema.to_json())

# convert the object into a dict
query_parameter_dynamic_filter_schema_dict = query_parameter_dynamic_filter_schema_instance.to_dict()
# create an instance of QueryParameterDynamicFilterSchema from a dict
query_parameter_dynamic_filter_schema_from_dict = QueryParameterDynamicFilterSchema.from_dict(query_parameter_dynamic_filter_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


