# BodyDynamicFilterSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**BodyDynamicFilterSchemaFilters**](BodyDynamicFilterSchemaFilters.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.body_dynamic_filter_schema import BodyDynamicFilterSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BodyDynamicFilterSchema from a JSON string
body_dynamic_filter_schema_instance = BodyDynamicFilterSchema.from_json(json)
# print the JSON string representation of the object
print(BodyDynamicFilterSchema.to_json())

# convert the object into a dict
body_dynamic_filter_schema_dict = body_dynamic_filter_schema_instance.to_dict()
# create an instance of BodyDynamicFilterSchema from a dict
body_dynamic_filter_schema_from_dict = BodyDynamicFilterSchema.from_dict(body_dynamic_filter_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


