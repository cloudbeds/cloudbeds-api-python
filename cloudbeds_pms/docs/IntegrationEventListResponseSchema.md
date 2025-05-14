# IntegrationEventListResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[IntegrationEventResponseSchema]**](IntegrationEventResponseSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.integration_event_list_response_schema import IntegrationEventListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationEventListResponseSchema from a JSON string
integration_event_list_response_schema_instance = IntegrationEventListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(IntegrationEventListResponseSchema.to_json())

# convert the object into a dict
integration_event_list_response_schema_dict = integration_event_list_response_schema_instance.to_dict()
# create an instance of IntegrationEventListResponseSchema from a dict
integration_event_list_response_schema_from_dict = IntegrationEventListResponseSchema.from_dict(integration_event_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


