# ImportTaskResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**upload_url** | **str** | A temporary URL, valid for 10 minutes, used to upload the import file. | 

## Example

```python
from cloudbeds_pms.models.import_task_response_schema import ImportTaskResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTaskResponseSchema from a JSON string
import_task_response_schema_instance = ImportTaskResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ImportTaskResponseSchema.to_json())

# convert the object into a dict
import_task_response_schema_dict = import_task_response_schema_instance.to_dict()
# create an instance of ImportTaskResponseSchema from a dict
import_task_response_schema_from_dict = ImportTaskResponseSchema.from_dict(import_task_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


