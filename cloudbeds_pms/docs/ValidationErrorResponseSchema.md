# ValidationErrorResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**code** | **str** | Machine-readable error code. | 
**errors** | [**List[ValidationErrorFieldSchema]**](ValidationErrorFieldSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.validation_error_response_schema import ValidationErrorResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorResponseSchema from a JSON string
validation_error_response_schema_instance = ValidationErrorResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorResponseSchema.to_json())

# convert the object into a dict
validation_error_response_schema_dict = validation_error_response_schema_instance.to_dict()
# create an instance of ValidationErrorResponseSchema from a dict
validation_error_response_schema_from_dict = ValidationErrorResponseSchema.from_dict(validation_error_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


