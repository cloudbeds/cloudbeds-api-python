# OrganizationLateCheckoutSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour** | **str** | Property-local latest late-checkout time-of-day (HH:MM); read with the property timeZone. Not an instant. | 
**fee_type** | **str** |  | 
**fee** | [**OrganizationLateCheckoutSchemaFee**](OrganizationLateCheckoutSchemaFee.md) |  | 

## Example

```python
from cloudbeds_pms.models.organization_late_checkout_schema import OrganizationLateCheckoutSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationLateCheckoutSchema from a JSON string
organization_late_checkout_schema_instance = OrganizationLateCheckoutSchema.from_json(json)
# print the JSON string representation of the object
print(OrganizationLateCheckoutSchema.to_json())

# convert the object into a dict
organization_late_checkout_schema_dict = organization_late_checkout_schema_instance.to_dict()
# create an instance of OrganizationLateCheckoutSchema from a dict
organization_late_checkout_schema_from_dict = OrganizationLateCheckoutSchema.from_dict(organization_late_checkout_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


