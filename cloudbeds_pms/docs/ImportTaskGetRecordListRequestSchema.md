# ImportTaskGetRecordListRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit for the number of items to return (max 500) | [optional] [default to 100]
**offset** | **int** | The offset for the current page of results | [optional] [default to 0]
**errors_only** | **bool** | Get erroneous records if set to true. | [optional] [default to False]

## Example

```python
from cloudbeds_pms.models.import_task_get_record_list_request_schema import ImportTaskGetRecordListRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTaskGetRecordListRequestSchema from a JSON string
import_task_get_record_list_request_schema_instance = ImportTaskGetRecordListRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ImportTaskGetRecordListRequestSchema.to_json())

# convert the object into a dict
import_task_get_record_list_request_schema_dict = import_task_get_record_list_request_schema_instance.to_dict()
# create an instance of ImportTaskGetRecordListRequestSchema from a dict
import_task_get_record_list_request_schema_from_dict = ImportTaskGetRecordListRequestSchema.from_dict(import_task_get_record_list_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


