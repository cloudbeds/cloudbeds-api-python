# InternalServerErrorResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.internal_server_error_response_schema import InternalServerErrorResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of InternalServerErrorResponseSchema from a JSON string
internal_server_error_response_schema_instance = InternalServerErrorResponseSchema.from_json(json)
# print the JSON string representation of the object
print(InternalServerErrorResponseSchema.to_json())

# convert the object into a dict
internal_server_error_response_schema_dict = internal_server_error_response_schema_instance.to_dict()
# create an instance of InternalServerErrorResponseSchema from a dict
internal_server_error_response_schema_from_dict = InternalServerErrorResponseSchema.from_dict(internal_server_error_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


