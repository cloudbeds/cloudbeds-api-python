# ImportTaskListResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**limit** | **int** |  | 
**total** | **int** |  | 
**data** | [**List[ImportTaskGetResponseSchema]**](ImportTaskGetResponseSchema.md) | Logical operator grouping filters or nested logical groups | 

## Example

```python
from cloudbeds_pms.models.import_task_list_response_schema import ImportTaskListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTaskListResponseSchema from a JSON string
import_task_list_response_schema_instance = ImportTaskListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ImportTaskListResponseSchema.to_json())

# convert the object into a dict
import_task_list_response_schema_dict = import_task_list_response_schema_instance.to_dict()
# create an instance of ImportTaskListResponseSchema from a dict
import_task_list_response_schema_from_dict = ImportTaskListResponseSchema.from_dict(import_task_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


