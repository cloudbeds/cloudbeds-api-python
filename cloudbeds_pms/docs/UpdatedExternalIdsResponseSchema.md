# UpdatedExternalIdsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxes** | [**List[TaxExternalIdResponseSchema]**](TaxExternalIdResponseSchema.md) | Resulting External ID of each requested tax, in request order. | 
**fees** | [**List[FeeExternalIdResponseSchema]**](FeeExternalIdResponseSchema.md) | Resulting External ID of each requested fee, in request order. | 

## Example

```python
from cloudbeds_pms.models.updated_external_ids_response_schema import UpdatedExternalIdsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatedExternalIdsResponseSchema from a JSON string
updated_external_ids_response_schema_instance = UpdatedExternalIdsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(UpdatedExternalIdsResponseSchema.to_json())

# convert the object into a dict
updated_external_ids_response_schema_dict = updated_external_ids_response_schema_instance.to_dict()
# create an instance of UpdatedExternalIdsResponseSchema from a dict
updated_external_ids_response_schema_from_dict = UpdatedExternalIdsResponseSchema.from_dict(updated_external_ids_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


