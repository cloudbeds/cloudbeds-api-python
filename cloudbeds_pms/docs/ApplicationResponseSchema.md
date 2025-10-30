# ApplicationResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Application ID | 
**name** | **str** | Application name | 
**oauth_scopes** | **List[str]** | OAuth scopes | 
**application_types** | **List[str]** | Application types | 

## Example

```python
from cloudbeds_pms.models.application_response_schema import ApplicationResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResponseSchema from a JSON string
application_response_schema_instance = ApplicationResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ApplicationResponseSchema.to_json())

# convert the object into a dict
application_response_schema_dict = application_response_schema_instance.to_dict()
# create an instance of ApplicationResponseSchema from a dict
application_response_schema_from_dict = ApplicationResponseSchema.from_dict(application_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


