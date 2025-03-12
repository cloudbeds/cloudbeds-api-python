# ImportTaskCreateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Import task type. | 
**priority** | **str** | Import task priority. | [optional] 

## Example

```python
from cloudbeds_pms.models.import_task_create_request_schema import ImportTaskCreateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTaskCreateRequestSchema from a JSON string
import_task_create_request_schema_instance = ImportTaskCreateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ImportTaskCreateRequestSchema.to_json())

# convert the object into a dict
import_task_create_request_schema_dict = import_task_create_request_schema_instance.to_dict()
# create an instance of ImportTaskCreateRequestSchema from a dict
import_task_create_request_schema_from_dict = ImportTaskCreateRequestSchema.from_dict(import_task_create_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


