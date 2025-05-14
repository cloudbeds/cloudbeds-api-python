# IntegrationEventListRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit for the number of items to return (max 500) | [optional] [default to 100]
**offset** | **int** | The offset for the current page of results | [optional] [default to 0]
**filters** | [**QueryParameterDynamicFilterSchemaFilters**](QueryParameterDynamicFilterSchemaFilters.md) |  | [optional] 
**sort** | [**SortSchema**](SortSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.integration_event_list_request_schema import IntegrationEventListRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationEventListRequestSchema from a JSON string
integration_event_list_request_schema_instance = IntegrationEventListRequestSchema.from_json(json)
# print the JSON string representation of the object
print(IntegrationEventListRequestSchema.to_json())

# convert the object into a dict
integration_event_list_request_schema_dict = integration_event_list_request_schema_instance.to_dict()
# create an instance of IntegrationEventListRequestSchema from a dict
integration_event_list_request_schema_from_dict = IntegrationEventListRequestSchema.from_dict(integration_event_list_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


