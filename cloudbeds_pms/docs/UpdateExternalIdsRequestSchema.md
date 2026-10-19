# UpdateExternalIdsRequestSchema

Taxes and fees whose External ID to set or clear. At least one entry overall, at most 100 across both lists. Taxes and fees not listed keep their External ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxes** | [**List[TaxExternalIdSchema]**](TaxExternalIdSchema.md) | Taxes to update. Each tax may appear once. | [optional] 
**fees** | [**List[FeeExternalIdSchema]**](FeeExternalIdSchema.md) | Fees to update. Each fee may appear once. | [optional] 

## Example

```python
from cloudbeds_pms.models.update_external_ids_request_schema import UpdateExternalIdsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExternalIdsRequestSchema from a JSON string
update_external_ids_request_schema_instance = UpdateExternalIdsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(UpdateExternalIdsRequestSchema.to_json())

# convert the object into a dict
update_external_ids_request_schema_dict = update_external_ids_request_schema_instance.to_dict()
# create an instance of UpdateExternalIdsRequestSchema from a dict
update_external_ids_request_schema_from_dict = UpdateExternalIdsRequestSchema.from_dict(update_external_ids_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


