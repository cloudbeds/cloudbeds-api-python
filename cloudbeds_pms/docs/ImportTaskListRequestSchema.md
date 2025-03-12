# ImportTaskListRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit for the number of items to return (max 500) | [optional] [default to 100]
**offset** | **int** | The offset for the current page of results | [optional] [default to 0]

## Example

```python
from cloudbeds_pms.models.import_task_list_request_schema import ImportTaskListRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTaskListRequestSchema from a JSON string
import_task_list_request_schema_instance = ImportTaskListRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ImportTaskListRequestSchema.to_json())

# convert the object into a dict
import_task_list_request_schema_dict = import_task_list_request_schema_instance.to_dict()
# create an instance of ImportTaskListRequestSchema from a dict
import_task_list_request_schema_from_dict = ImportTaskListRequestSchema.from_dict(import_task_list_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


