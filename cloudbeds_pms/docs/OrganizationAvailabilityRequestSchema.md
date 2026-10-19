# OrganizationAvailabilityRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Organization ID | [optional] 
**check_in** | **date** | Check-in date in YYYY-MM-DD format. | [optional] 
**check_out** | **date** | Check-out date in YYYY-MM-DD format. Exclusive: the departure day is not charged. | [optional] 
**currency** | **str** | ISO 4217 currency code every property is priced in. Required: the response is a comparison list, and prices only compare if they share a currency. | [optional] 

## Example

```python
from cloudbeds_pms.models.organization_availability_request_schema import OrganizationAvailabilityRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAvailabilityRequestSchema from a JSON string
organization_availability_request_schema_instance = OrganizationAvailabilityRequestSchema.from_json(json)
# print the JSON string representation of the object
print(OrganizationAvailabilityRequestSchema.to_json())

# convert the object into a dict
organization_availability_request_schema_dict = organization_availability_request_schema_instance.to_dict()
# create an instance of OrganizationAvailabilityRequestSchema from a dict
organization_availability_request_schema_from_dict = OrganizationAvailabilityRequestSchema.from_dict(organization_availability_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


