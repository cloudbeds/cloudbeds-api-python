# SectionEntityResponseSchema

A generic record reference, so adding a sectioning dimension is a new `type` value rather than a schema change.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Record kind. | 
**id** | **str** | Record id. | 

## Example

```python
from cloudbeds_pms.models.section_entity_response_schema import SectionEntityResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SectionEntityResponseSchema from a JSON string
section_entity_response_schema_instance = SectionEntityResponseSchema.from_json(json)
# print the JSON string representation of the object
print(SectionEntityResponseSchema.to_json())

# convert the object into a dict
section_entity_response_schema_dict = section_entity_response_schema_instance.to_dict()
# create an instance of SectionEntityResponseSchema from a dict
section_entity_response_schema_from_dict = SectionEntityResponseSchema.from_dict(section_entity_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


