# CreateViewRequestSchema

Creating a stored view. The server mints the key — a client cannot choose one, and passing a reserved built-in id is a 400 rather than a way to pre-empt a built-in.  `status` defaults to `draft` so the normal flow is build-then-publish; pass `published` to save-and-publish in one step.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for the view. | 
**sections** | [**List[DefinitionSectionRequestSchema]**](DefinitionSectionRequestSchema.md) | Sections in order. The uncategorized tail is computed at render time and must not be submitted. | 
**status** | **str** | Initial status of revision 1. | [optional] [default to 'draft']

## Example

```python
from cloudbeds_pms.models.create_view_request_schema import CreateViewRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CreateViewRequestSchema from a JSON string
create_view_request_schema_instance = CreateViewRequestSchema.from_json(json)
# print the JSON string representation of the object
print(CreateViewRequestSchema.to_json())

# convert the object into a dict
create_view_request_schema_dict = create_view_request_schema_instance.to_dict()
# create an instance of CreateViewRequestSchema from a dict
create_view_request_schema_from_dict = CreateViewRequestSchema.from_dict(create_view_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


