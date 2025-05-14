# IntegrationEventCreateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | Type of object related to the integration event. | 
**system** | **str** | System where the integration event occurred. | 
**status** | **str** | Status of the integration event. | 
**result** | **str** | Result of the integration event. | 
**object_id** | **str** | ID of object related to the integration event. | [optional] 
**description** | **str** | Description of the integration event. Required when result is failure. | [optional] 
**details** | **str** | Details of the integration event, that usually contain instructions. | [optional] 
**action_text** | **str** | Text to be displayed on the UI for the action. | [optional] 
**retry_url** | **str** | URL that is used to retry the action. | [optional] 

## Example

```python
from cloudbeds_pms.models.integration_event_create_request_schema import IntegrationEventCreateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationEventCreateRequestSchema from a JSON string
integration_event_create_request_schema_instance = IntegrationEventCreateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(IntegrationEventCreateRequestSchema.to_json())

# convert the object into a dict
integration_event_create_request_schema_dict = integration_event_create_request_schema_instance.to_dict()
# create an instance of IntegrationEventCreateRequestSchema from a dict
integration_event_create_request_schema_from_dict = IntegrationEventCreateRequestSchema.from_dict(integration_event_create_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


