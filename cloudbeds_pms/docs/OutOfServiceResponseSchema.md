# OutOfServiceResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[OutOfServiceResponseItemSchema]**](OutOfServiceResponseItemSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.out_of_service_response_schema import OutOfServiceResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OutOfServiceResponseSchema from a JSON string
out_of_service_response_schema_instance = OutOfServiceResponseSchema.from_json(json)
# print the JSON string representation of the object
print(OutOfServiceResponseSchema.to_json())

# convert the object into a dict
out_of_service_response_schema_dict = out_of_service_response_schema_instance.to_dict()
# create an instance of OutOfServiceResponseSchema from a dict
out_of_service_response_schema_from_dict = OutOfServiceResponseSchema.from_dict(out_of_service_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


