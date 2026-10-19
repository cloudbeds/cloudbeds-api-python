# OrganizationAvailabilityPropertySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Property identifier, used to join this entry with the organization detail response. | 
**has_availability** | **bool** | Whether the property can be booked for the requested dates. | 
**min_nightly_rate** | [**MoneySchema**](MoneySchema.md) |  | 
**min_total_price** | [**MoneySchema**](MoneySchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.organization_availability_property_schema import OrganizationAvailabilityPropertySchema

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAvailabilityPropertySchema from a JSON string
organization_availability_property_schema_instance = OrganizationAvailabilityPropertySchema.from_json(json)
# print the JSON string representation of the object
print(OrganizationAvailabilityPropertySchema.to_json())

# convert the object into a dict
organization_availability_property_schema_dict = organization_availability_property_schema_instance.to_dict()
# create an instance of OrganizationAvailabilityPropertySchema from a dict
organization_availability_property_schema_from_dict = OrganizationAvailabilityPropertySchema.from_dict(organization_availability_property_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


