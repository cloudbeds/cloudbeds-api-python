# ImportTaskRecordListResponseSchema

List of import task records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**limit** | **int** |  | 
**total** | **int** |  | 
**data** | [**List[ImportTaskRecordGetResponseSchema]**](ImportTaskRecordGetResponseSchema.md) | List of import task records. | 

## Example

```python
from cloudbeds_pms.models.import_task_record_list_response_schema import ImportTaskRecordListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTaskRecordListResponseSchema from a JSON string
import_task_record_list_response_schema_instance = ImportTaskRecordListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ImportTaskRecordListResponseSchema.to_json())

# convert the object into a dict
import_task_record_list_response_schema_dict = import_task_record_list_response_schema_instance.to_dict()
# create an instance of ImportTaskRecordListResponseSchema from a dict
import_task_record_list_response_schema_from_dict = ImportTaskRecordListResponseSchema.from_dict(import_task_record_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


