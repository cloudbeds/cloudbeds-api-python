# AiAvailabilityErrorResponseSchema

An error, in the same schema.org vocabulary as a successful response, carrying the standard `code` and per-field `errors` alongside.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | JSON-LD vocabulary the document is expressed in. | 
**type** | **str** |  | 
**name** | **str** | Stable token an agent can branch on. | 
**description** | **str** | Human-readable detail. | 
**status_code** | **int** |  | 
**code** | **str** | Upper-case machine code, as on every Public API error. | 
**errors** | [**List[AiAvailabilityErrorResponseSchemaErrorsInner]**](AiAvailabilityErrorResponseSchemaErrorsInner.md) | The offending fields, one entry per violation. Empty when the error is not about a field. | 

## Example

```python
from cloudbeds_pms.models.ai_availability_error_response_schema import AiAvailabilityErrorResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AiAvailabilityErrorResponseSchema from a JSON string
ai_availability_error_response_schema_instance = AiAvailabilityErrorResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AiAvailabilityErrorResponseSchema.to_json())

# convert the object into a dict
ai_availability_error_response_schema_dict = ai_availability_error_response_schema_instance.to_dict()
# create an instance of AiAvailabilityErrorResponseSchema from a dict
ai_availability_error_response_schema_from_dict = AiAvailabilityErrorResponseSchema.from_dict(ai_availability_error_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


