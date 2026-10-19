# TaxExternalIdResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_tax_id** | **str** | Tax id as sent in the request. | 
**tax_id** | **str** | Current version of the tax the External ID was written to. Differs from requestedTaxId when the requested tax has since been edited. | 
**external_id** | **str** | External ID now assigned; null when cleared. | 

## Example

```python
from cloudbeds_pms.models.tax_external_id_response_schema import TaxExternalIdResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaxExternalIdResponseSchema from a JSON string
tax_external_id_response_schema_instance = TaxExternalIdResponseSchema.from_json(json)
# print the JSON string representation of the object
print(TaxExternalIdResponseSchema.to_json())

# convert the object into a dict
tax_external_id_response_schema_dict = tax_external_id_response_schema_instance.to_dict()
# create an instance of TaxExternalIdResponseSchema from a dict
tax_external_id_response_schema_from_dict = TaxExternalIdResponseSchema.from_dict(tax_external_id_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


