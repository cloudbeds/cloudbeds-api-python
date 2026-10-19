# OrganizationAddressSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | 
**state** | **str** |  | 
**country** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.organization_address_schema import OrganizationAddressSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAddressSchema from a JSON string
organization_address_schema_instance = OrganizationAddressSchema.from_json(json)
# print the JSON string representation of the object
print(OrganizationAddressSchema.to_json())

# convert the object into a dict
organization_address_schema_dict = organization_address_schema_instance.to_dict()
# create an instance of OrganizationAddressSchema from a dict
organization_address_schema_from_dict = OrganizationAddressSchema.from_dict(organization_address_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


