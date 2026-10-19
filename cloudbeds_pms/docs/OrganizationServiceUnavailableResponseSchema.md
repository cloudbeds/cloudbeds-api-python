# OrganizationServiceUnavailableResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**success** | **bool** |  | 

## Example

```python
from cloudbeds_pms.models.organization_service_unavailable_response_schema import OrganizationServiceUnavailableResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationServiceUnavailableResponseSchema from a JSON string
organization_service_unavailable_response_schema_instance = OrganizationServiceUnavailableResponseSchema.from_json(json)
# print the JSON string representation of the object
print(OrganizationServiceUnavailableResponseSchema.to_json())

# convert the object into a dict
organization_service_unavailable_response_schema_dict = organization_service_unavailable_response_schema_instance.to_dict()
# create an instance of OrganizationServiceUnavailableResponseSchema from a dict
organization_service_unavailable_response_schema_from_dict = OrganizationServiceUnavailableResponseSchema.from_dict(organization_service_unavailable_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


