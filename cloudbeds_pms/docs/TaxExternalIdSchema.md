# TaxExternalIdSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** | Cloudbeds tax id, as returned in &#x60;taxID&#x60; by getTaxesAndFees: a positive integer without leading zeros, at most 9223372036854775807. An id replaced by a later edit of the tax is accepted and resolved to the tax&#39;s current version. | 
**external_id** | **str** | External ID to assign, at most 64 characters after leading and trailing whitespace is trimmed. Null, an empty value or an omitted field clears the mapping. | [optional] 

## Example

```python
from cloudbeds_pms.models.tax_external_id_schema import TaxExternalIdSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaxExternalIdSchema from a JSON string
tax_external_id_schema_instance = TaxExternalIdSchema.from_json(json)
# print the JSON string representation of the object
print(TaxExternalIdSchema.to_json())

# convert the object into a dict
tax_external_id_schema_dict = tax_external_id_schema_instance.to_dict()
# create an instance of TaxExternalIdSchema from a dict
tax_external_id_schema_from_dict = TaxExternalIdSchema.from_dict(tax_external_id_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


