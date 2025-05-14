# IntegrationEventResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the integration event. | 
**property_id** | **str** | Unique identifier for the property. | 
**object_id** | **str** | Unique identifier for the object associated with the integration event. | [optional] 
**object_type** | **str** | Type of object associated with the integration event. | 
**system** | **str** | Type of system associated with the integration event. | 
**status** | **str** | Status of the integration event. | 
**result** | **str** | Result of the integration event. | 
**description** | **str** | Short description of the integration event. | [optional] 
**details** | **str** | Detailed information about the integration event. | [optional] 
**action_text** | **str** | Text to be displayed for the action associated with the integration event. | [optional] 
**created_at** | **str** |  | 
**updated_at** | **str** |  | [optional] 
**retried_at** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.integration_event_response_schema import IntegrationEventResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationEventResponseSchema from a JSON string
integration_event_response_schema_instance = IntegrationEventResponseSchema.from_json(json)
# print the JSON string representation of the object
print(IntegrationEventResponseSchema.to_json())

# convert the object into a dict
integration_event_response_schema_dict = integration_event_response_schema_instance.to_dict()
# create an instance of IntegrationEventResponseSchema from a dict
integration_event_response_schema_from_dict = IntegrationEventResponseSchema.from_dict(integration_event_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


