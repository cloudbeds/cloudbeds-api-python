# SystemFeatureResponseSchema

System feature information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Feature name | 
**version** | **str** | Feature version | 

## Example

```python
from cloudbeds_pms.models.system_feature_response_schema import SystemFeatureResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SystemFeatureResponseSchema from a JSON string
system_feature_response_schema_instance = SystemFeatureResponseSchema.from_json(json)
# print the JSON string representation of the object
print(SystemFeatureResponseSchema.to_json())

# convert the object into a dict
system_feature_response_schema_dict = system_feature_response_schema_instance.to_dict()
# create an instance of SystemFeatureResponseSchema from a dict
system_feature_response_schema_from_dict = SystemFeatureResponseSchema.from_dict(system_feature_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


