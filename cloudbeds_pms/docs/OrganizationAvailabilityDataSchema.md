# OrganizationAvailabilityDataSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_in** | **date** | The requested check-in date, echoed back so a client can match a response to the date range currently on screen. | 
**check_out** | **date** | The requested check-out date. Exclusive: the departure day is not a charged night. | 
**properties** | [**List[OrganizationAvailabilityPropertySchema]**](OrganizationAvailabilityPropertySchema.md) | One entry per member property, including those with no vacancy. A property is omitted when it has no base currency configured, so a missing property id means no data for that property rather than no vacancy. | 

## Example

```python
from cloudbeds_pms.models.organization_availability_data_schema import OrganizationAvailabilityDataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAvailabilityDataSchema from a JSON string
organization_availability_data_schema_instance = OrganizationAvailabilityDataSchema.from_json(json)
# print the JSON string representation of the object
print(OrganizationAvailabilityDataSchema.to_json())

# convert the object into a dict
organization_availability_data_schema_dict = organization_availability_data_schema_instance.to_dict()
# create an instance of OrganizationAvailabilityDataSchema from a dict
organization_availability_data_schema_from_dict = OrganizationAvailabilityDataSchema.from_dict(organization_availability_data_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


