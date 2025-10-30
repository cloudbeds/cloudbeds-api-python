# ApplicationListResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApplicationResponseSchema]**](ApplicationResponseSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.application_list_response_schema import ApplicationListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationListResponseSchema from a JSON string
application_list_response_schema_instance = ApplicationListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ApplicationListResponseSchema.to_json())

# convert the object into a dict
application_list_response_schema_dict = application_list_response_schema_instance.to_dict()
# create an instance of ApplicationListResponseSchema from a dict
application_list_response_schema_from_dict = ApplicationListResponseSchema.from_dict(application_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


