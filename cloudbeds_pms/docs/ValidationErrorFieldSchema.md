# ValidationErrorFieldSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.validation_error_field_schema import ValidationErrorFieldSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorFieldSchema from a JSON string
validation_error_field_schema_instance = ValidationErrorFieldSchema.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorFieldSchema.to_json())

# convert the object into a dict
validation_error_field_schema_dict = validation_error_field_schema_instance.to_dict()
# create an instance of ValidationErrorFieldSchema from a dict
validation_error_field_schema_from_dict = ValidationErrorFieldSchema.from_dict(validation_error_field_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


