# TaxSchemaOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | 
**tax_id** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.tax_schema_one_of import TaxSchemaOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of TaxSchemaOneOf from a JSON string
tax_schema_one_of_instance = TaxSchemaOneOf.from_json(json)
# print the JSON string representation of the object
print(TaxSchemaOneOf.to_json())

# convert the object into a dict
tax_schema_one_of_dict = tax_schema_one_of_instance.to_dict()
# create an instance of TaxSchemaOneOf from a dict
tax_schema_one_of_from_dict = TaxSchemaOneOf.from_dict(tax_schema_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


