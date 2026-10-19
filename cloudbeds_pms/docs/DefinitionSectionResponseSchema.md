# DefinitionSectionResponseSchema

A section as stored — exactly the shape a save accepts back, because the read and the write of a definition are the same document.  Not to be confused with a section in a rendered layout: a definition holds the unit ids, while a layout puts the id on each unit and leaves the section carrying only its label and kind.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Client-assigned section id, stable across saves. | 
**label** | **str** | Admin-authored label. | 
**unit_ids** | **List[str]** | Units placed in this section, in order. Ids the catalog cannot resolve are kept here verbatim and reported in &#x60;unresolvedUnitIds&#x60;. | 

## Example

```python
from cloudbeds_pms.models.definition_section_response_schema import DefinitionSectionResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DefinitionSectionResponseSchema from a JSON string
definition_section_response_schema_instance = DefinitionSectionResponseSchema.from_json(json)
# print the JSON string representation of the object
print(DefinitionSectionResponseSchema.to_json())

# convert the object into a dict
definition_section_response_schema_dict = definition_section_response_schema_instance.to_dict()
# create an instance of DefinitionSectionResponseSchema from a dict
definition_section_response_schema_from_dict = DefinitionSectionResponseSchema.from_dict(definition_section_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


