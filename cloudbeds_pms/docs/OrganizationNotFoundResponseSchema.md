# OrganizationNotFoundResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**success** | **bool** |  | 

## Example

```python
from cloudbeds_pms.models.organization_not_found_response_schema import OrganizationNotFoundResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationNotFoundResponseSchema from a JSON string
organization_not_found_response_schema_instance = OrganizationNotFoundResponseSchema.from_json(json)
# print the JSON string representation of the object
print(OrganizationNotFoundResponseSchema.to_json())

# convert the object into a dict
organization_not_found_response_schema_dict = organization_not_found_response_schema_instance.to_dict()
# create an instance of OrganizationNotFoundResponseSchema from a dict
organization_not_found_response_schema_from_dict = OrganizationNotFoundResponseSchema.from_dict(organization_not_found_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


