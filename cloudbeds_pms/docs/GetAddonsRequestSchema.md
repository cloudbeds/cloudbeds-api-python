# GetAddonsRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit for the number of items to return (max 500) | [optional] [default to 100]
**offset** | **int** | The offset for the current page of results | [optional] [default to 0]
**filters** | [**QueryParameterDynamicFilterSchemaFilters**](QueryParameterDynamicFilterSchemaFilters.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.get_addons_request_schema import GetAddonsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetAddonsRequestSchema from a JSON string
get_addons_request_schema_instance = GetAddonsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GetAddonsRequestSchema.to_json())

# convert the object into a dict
get_addons_request_schema_dict = get_addons_request_schema_instance.to_dict()
# create an instance of GetAddonsRequestSchema from a dict
get_addons_request_schema_from_dict = GetAddonsRequestSchema.from_dict(get_addons_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


