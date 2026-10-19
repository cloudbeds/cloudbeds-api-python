# OrganizationPropertySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**code** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**currency_code** | **str** |  | 
**time_zone** | **str** | Property IANA timezone; read together with policy times (which are property-local). | [optional] 
**hotel_address** | [**OrganizationAddressSchema**](OrganizationAddressSchema.md) |  | 
**lat** | **float** |  | 
**lng** | **float** |  | 
**booking_url** | **str** |  | 
**website** | **str** |  | [optional] 
**images** | **List[str]** |  | 
**logo** | **str** |  | [optional] 
**amenities** | [**List[AmenityItemSchema]**](AmenityItemSchema.md) |  | 
**policies** | [**OrganizationPoliciesSchema**](OrganizationPoliciesSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.organization_property_schema import OrganizationPropertySchema

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationPropertySchema from a JSON string
organization_property_schema_instance = OrganizationPropertySchema.from_json(json)
# print the JSON string representation of the object
print(OrganizationPropertySchema.to_json())

# convert the object into a dict
organization_property_schema_dict = organization_property_schema_instance.to_dict()
# create an instance of OrganizationPropertySchema from a dict
organization_property_schema_from_dict = OrganizationPropertySchema.from_dict(organization_property_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


