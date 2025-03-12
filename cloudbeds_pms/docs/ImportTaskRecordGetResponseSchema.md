# ImportTaskRecordGetResponseSchema

Import task record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**import_id** | **str** |  | 
**uuid** | **str** |  | 
**created_at** | **str** |  | 
**property_id** | **int** |  | 
**object_id** | **int** |  | 
**import_status** | **str** | Import task status. | 
**errors** | **str** |  | 
**import_attempted_at** | **str** |  | 
**data** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.import_task_record_get_response_schema import ImportTaskRecordGetResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTaskRecordGetResponseSchema from a JSON string
import_task_record_get_response_schema_instance = ImportTaskRecordGetResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ImportTaskRecordGetResponseSchema.to_json())

# convert the object into a dict
import_task_record_get_response_schema_dict = import_task_record_get_response_schema_instance.to_dict()
# create an instance of ImportTaskRecordGetResponseSchema from a dict
import_task_record_get_response_schema_from_dict = ImportTaskRecordGetResponseSchema.from_dict(import_task_record_get_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


