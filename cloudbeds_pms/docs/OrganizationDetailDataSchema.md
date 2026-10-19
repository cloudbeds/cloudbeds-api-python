# OrganizationDetailDataSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**properties** | [**List[OrganizationPropertySchema]**](OrganizationPropertySchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.organization_detail_data_schema import OrganizationDetailDataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationDetailDataSchema from a JSON string
organization_detail_data_schema_instance = OrganizationDetailDataSchema.from_json(json)
# print the JSON string representation of the object
print(OrganizationDetailDataSchema.to_json())

# convert the object into a dict
organization_detail_data_schema_dict = organization_detail_data_schema_instance.to_dict()
# create an instance of OrganizationDetailDataSchema from a dict
organization_detail_data_schema_from_dict = OrganizationDetailDataSchema.from_dict(organization_detail_data_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


