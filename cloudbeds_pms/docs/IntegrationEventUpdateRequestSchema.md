# IntegrationEventUpdateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the integration event. | 
**result** | **str** | Result of the integration event. When provided, description and details are replaced with the values sent (omitted ones are cleared). | [optional] 
**description** | **str** | Description of the integration event. Required when result is failure. | [optional] 
**details** | **str** | Details of the integration event, that usually contain instructions. | [optional] 

## Example

```python
from cloudbeds_pms.models.integration_event_update_request_schema import IntegrationEventUpdateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationEventUpdateRequestSchema from a JSON string
integration_event_update_request_schema_instance = IntegrationEventUpdateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(IntegrationEventUpdateRequestSchema.to_json())

# convert the object into a dict
integration_event_update_request_schema_dict = integration_event_update_request_schema_instance.to_dict()
# create an instance of IntegrationEventUpdateRequestSchema from a dict
integration_event_update_request_schema_from_dict = IntegrationEventUpdateRequestSchema.from_dict(integration_event_update_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


