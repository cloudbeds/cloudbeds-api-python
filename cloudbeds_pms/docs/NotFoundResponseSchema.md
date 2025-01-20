# NotFoundResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.not_found_response_schema import NotFoundResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of NotFoundResponseSchema from a JSON string
not_found_response_schema_instance = NotFoundResponseSchema.from_json(json)
# print the JSON string representation of the object
print(NotFoundResponseSchema.to_json())

# convert the object into a dict
not_found_response_schema_dict = not_found_response_schema_instance.to_dict()
# create an instance of NotFoundResponseSchema from a dict
not_found_response_schema_from_dict = NotFoundResponseSchema.from_dict(not_found_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


