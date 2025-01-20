# BodyDynamicFilterSchemaFilters

The filters for the query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[DynamicFilterSchemaAndInner]**](DynamicFilterSchemaAndInner.md) | Logical operator grouping filters or nested logical groups | [optional] 
**var_or** | [**List[DynamicFilterSchemaAndInner]**](DynamicFilterSchemaAndInner.md) | Logical operator grouping filters or nested logical groups | [optional] 

## Example

```python
from cloudbeds_pms.models.body_dynamic_filter_schema_filters import BodyDynamicFilterSchemaFilters

# TODO update the JSON string below
json = "{}"
# create an instance of BodyDynamicFilterSchemaFilters from a JSON string
body_dynamic_filter_schema_filters_instance = BodyDynamicFilterSchemaFilters.from_json(json)
# print the JSON string representation of the object
print(BodyDynamicFilterSchemaFilters.to_json())

# convert the object into a dict
body_dynamic_filter_schema_filters_dict = body_dynamic_filter_schema_filters_instance.to_dict()
# create an instance of BodyDynamicFilterSchemaFilters from a dict
body_dynamic_filter_schema_filters_from_dict = BodyDynamicFilterSchemaFilters.from_dict(body_dynamic_filter_schema_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


