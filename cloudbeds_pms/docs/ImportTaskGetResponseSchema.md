# ImportTaskGetResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**source** | **str** |  | 
**parsed_records_count** | **str** |  | 
**imported_records_count** | **str** |  | 
**type** | **str** | Import task type. | 
**priority** | **str** | Import task priority. | 
**file_status** | **str** |  | 
**import_status** | **str** | Import task status. | 
**created_at** | **str** |  | [optional] 
**errors** | **str** |  | [optional] 
**user_id** | **str** | ID of the user who created the import task. | [optional] 
**updated_at** | **str** | When the task last changed, RFC3339. | [optional] 
**parent_id** | **str** | Parent task ID when this task re-imports failed records of another task. | [optional] 

## Example

```python
from cloudbeds_pms.models.import_task_get_response_schema import ImportTaskGetResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTaskGetResponseSchema from a JSON string
import_task_get_response_schema_instance = ImportTaskGetResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ImportTaskGetResponseSchema.to_json())

# convert the object into a dict
import_task_get_response_schema_dict = import_task_get_response_schema_instance.to_dict()
# create an instance of ImportTaskGetResponseSchema from a dict
import_task_get_response_schema_from_dict = ImportTaskGetResponseSchema.from_dict(import_task_get_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


