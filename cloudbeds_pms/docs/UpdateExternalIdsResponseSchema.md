# UpdateExternalIdsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdatedExternalIdsResponseSchema**](UpdatedExternalIdsResponseSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.update_external_ids_response_schema import UpdateExternalIdsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExternalIdsResponseSchema from a JSON string
update_external_ids_response_schema_instance = UpdateExternalIdsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(UpdateExternalIdsResponseSchema.to_json())

# convert the object into a dict
update_external_ids_response_schema_dict = update_external_ids_response_schema_instance.to_dict()
# create an instance of UpdateExternalIdsResponseSchema from a dict
update_external_ids_response_schema_from_dict = UpdateExternalIdsResponseSchema.from_dict(update_external_ids_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


