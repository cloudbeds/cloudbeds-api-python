# OrganizationDetailResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**data** | [**OrganizationDetailDataSchema**](OrganizationDetailDataSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.organization_detail_response_schema import OrganizationDetailResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationDetailResponseSchema from a JSON string
organization_detail_response_schema_instance = OrganizationDetailResponseSchema.from_json(json)
# print the JSON string representation of the object
print(OrganizationDetailResponseSchema.to_json())

# convert the object into a dict
organization_detail_response_schema_dict = organization_detail_response_schema_instance.to_dict()
# create an instance of OrganizationDetailResponseSchema from a dict
organization_detail_response_schema_from_dict = OrganizationDetailResponseSchema.from_dict(organization_detail_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


