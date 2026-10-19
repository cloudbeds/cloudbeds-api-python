# OrganizationBadRequestSchema

Returned when the request cannot be served as sent: a malformed or reversed date range, or an unsupported currency. The error string identifies which.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**success** | **bool** |  | 

## Example

```python
from cloudbeds_pms.models.organization_bad_request_schema import OrganizationBadRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationBadRequestSchema from a JSON string
organization_bad_request_schema_instance = OrganizationBadRequestSchema.from_json(json)
# print the JSON string representation of the object
print(OrganizationBadRequestSchema.to_json())

# convert the object into a dict
organization_bad_request_schema_dict = organization_bad_request_schema_instance.to_dict()
# create an instance of OrganizationBadRequestSchema from a dict
organization_bad_request_schema_from_dict = OrganizationBadRequestSchema.from_dict(organization_bad_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


