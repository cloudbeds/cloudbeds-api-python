# OrganizationDetailRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Organization ID | [optional] 
**lang** | **str** | Cloudbeds language code (e.g. en, pt-br, es-es). Defaults to en. | [optional] 
**currency** | **str** | ISO 4217 currency code. Optional: when omitted, each property keeps its own currency, and every monetary value carries the currency it is expressed in. | [optional] 

## Example

```python
from cloudbeds_pms.models.organization_detail_request_schema import OrganizationDetailRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationDetailRequestSchema from a JSON string
organization_detail_request_schema_instance = OrganizationDetailRequestSchema.from_json(json)
# print the JSON string representation of the object
print(OrganizationDetailRequestSchema.to_json())

# convert the object into a dict
organization_detail_request_schema_dict = organization_detail_request_schema_instance.to_dict()
# create an instance of OrganizationDetailRequestSchema from a dict
organization_detail_request_schema_from_dict = OrganizationDetailRequestSchema.from_dict(organization_detail_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


