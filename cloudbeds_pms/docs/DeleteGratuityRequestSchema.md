# DeleteGratuityRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gratuity_id** | **str** | The public gratuityId of the gratuity to void (as returned at post time). Voids that single gratuity and its tax children. | 

## Example

```python
from cloudbeds_pms.models.delete_gratuity_request_schema import DeleteGratuityRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteGratuityRequestSchema from a JSON string
delete_gratuity_request_schema_instance = DeleteGratuityRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DeleteGratuityRequestSchema.to_json())

# convert the object into a dict
delete_gratuity_request_schema_dict = delete_gratuity_request_schema_instance.to_dict()
# create an instance of DeleteGratuityRequestSchema from a dict
delete_gratuity_request_schema_from_dict = DeleteGratuityRequestSchema.from_dict(delete_gratuity_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


