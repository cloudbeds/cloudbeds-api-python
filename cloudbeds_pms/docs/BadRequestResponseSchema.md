# BadRequestResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**errors** | [**BadRequestResponseSchemaErrors**](BadRequestResponseSchemaErrors.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.bad_request_response_schema import BadRequestResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestResponseSchema from a JSON string
bad_request_response_schema_instance = BadRequestResponseSchema.from_json(json)
# print the JSON string representation of the object
print(BadRequestResponseSchema.to_json())

# convert the object into a dict
bad_request_response_schema_dict = bad_request_response_schema_instance.to_dict()
# create an instance of BadRequestResponseSchema from a dict
bad_request_response_schema_from_dict = BadRequestResponseSchema.from_dict(bad_request_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


