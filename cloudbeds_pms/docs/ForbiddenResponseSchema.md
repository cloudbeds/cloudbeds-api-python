# ForbiddenResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.forbidden_response_schema import ForbiddenResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ForbiddenResponseSchema from a JSON string
forbidden_response_schema_instance = ForbiddenResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ForbiddenResponseSchema.to_json())

# convert the object into a dict
forbidden_response_schema_dict = forbidden_response_schema_instance.to_dict()
# create an instance of ForbiddenResponseSchema from a dict
forbidden_response_schema_from_dict = ForbiddenResponseSchema.from_dict(forbidden_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


