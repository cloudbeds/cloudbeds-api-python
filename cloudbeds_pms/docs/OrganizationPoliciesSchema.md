# OrganizationPoliciesSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkin_time** | **str** | Property-local check-in time-of-day (HH:MM); read with the property timeZone. Not an instant. | [optional] 
**checkout_time** | **str** | Property-local check-out time-of-day (HH:MM); read with the property timeZone. Not an instant. | [optional] 
**late_checkout** | [**OrganizationLateCheckoutSchema**](OrganizationLateCheckoutSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.organization_policies_schema import OrganizationPoliciesSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationPoliciesSchema from a JSON string
organization_policies_schema_instance = OrganizationPoliciesSchema.from_json(json)
# print the JSON string representation of the object
print(OrganizationPoliciesSchema.to_json())

# convert the object into a dict
organization_policies_schema_dict = organization_policies_schema_instance.to_dict()
# create an instance of OrganizationPoliciesSchema from a dict
organization_policies_schema_from_dict = OrganizationPoliciesSchema.from_dict(organization_policies_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


