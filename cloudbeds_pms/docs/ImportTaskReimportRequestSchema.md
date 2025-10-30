# ImportTaskReimportRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **str** | Import task priority. | [optional] 
**reprocess_failed_records** | **bool** | Re-process failed records of parent task. | [optional] 

## Example

```python
from cloudbeds_pms.models.import_task_reimport_request_schema import ImportTaskReimportRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTaskReimportRequestSchema from a JSON string
import_task_reimport_request_schema_instance = ImportTaskReimportRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ImportTaskReimportRequestSchema.to_json())

# convert the object into a dict
import_task_reimport_request_schema_dict = import_task_reimport_request_schema_instance.to_dict()
# create an instance of ImportTaskReimportRequestSchema from a dict
import_task_reimport_request_schema_from_dict = ImportTaskReimportRequestSchema.from_dict(import_task_reimport_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


