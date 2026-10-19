# DeleteCheckRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_id** | **str** | The check&#39;s public checkId (partner-supplied or Cloudbeds-generated) returned by createCheck. | 

## Example

```python
from cloudbeds_pms.models.delete_check_request_schema import DeleteCheckRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCheckRequestSchema from a JSON string
delete_check_request_schema_instance = DeleteCheckRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DeleteCheckRequestSchema.to_json())

# convert the object into a dict
delete_check_request_schema_dict = delete_check_request_schema_instance.to_dict()
# create an instance of DeleteCheckRequestSchema from a dict
delete_check_request_schema_from_dict = DeleteCheckRequestSchema.from_dict(delete_check_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


