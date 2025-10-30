# SystemResponseSchema

System features response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**List[SystemFeatureResponseSchema]**](SystemFeatureResponseSchema.md) | Array of system feature versions for this property | 

## Example

```python
from cloudbeds_pms.models.system_response_schema import SystemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SystemResponseSchema from a JSON string
system_response_schema_instance = SystemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(SystemResponseSchema.to_json())

# convert the object into a dict
system_response_schema_dict = system_response_schema_instance.to_dict()
# create an instance of SystemResponseSchema from a dict
system_response_schema_from_dict = SystemResponseSchema.from_dict(system_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


