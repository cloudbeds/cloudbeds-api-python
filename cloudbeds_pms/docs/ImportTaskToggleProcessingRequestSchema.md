# ImportTaskToggleProcessingRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action to perform on the import task | [optional] 

## Example

```python
from cloudbeds_pms.models.import_task_toggle_processing_request_schema import ImportTaskToggleProcessingRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTaskToggleProcessingRequestSchema from a JSON string
import_task_toggle_processing_request_schema_instance = ImportTaskToggleProcessingRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ImportTaskToggleProcessingRequestSchema.to_json())

# convert the object into a dict
import_task_toggle_processing_request_schema_dict = import_task_toggle_processing_request_schema_instance.to_dict()
# create an instance of ImportTaskToggleProcessingRequestSchema from a dict
import_task_toggle_processing_request_schema_from_dict = ImportTaskToggleProcessingRequestSchema.from_dict(import_task_toggle_processing_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


