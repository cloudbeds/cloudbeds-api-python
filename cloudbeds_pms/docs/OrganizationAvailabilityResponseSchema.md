# OrganizationAvailabilityResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**data** | [**OrganizationAvailabilityDataSchema**](OrganizationAvailabilityDataSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.organization_availability_response_schema import OrganizationAvailabilityResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAvailabilityResponseSchema from a JSON string
organization_availability_response_schema_instance = OrganizationAvailabilityResponseSchema.from_json(json)
# print the JSON string representation of the object
print(OrganizationAvailabilityResponseSchema.to_json())

# convert the object into a dict
organization_availability_response_schema_dict = organization_availability_response_schema_instance.to_dict()
# create an instance of OrganizationAvailabilityResponseSchema from a dict
organization_availability_response_schema_from_dict = OrganizationAvailabilityResponseSchema.from_dict(organization_availability_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


