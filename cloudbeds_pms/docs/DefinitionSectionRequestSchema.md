# DefinitionSectionRequestSchema

One section of a submitted definition — the same `{id, label, unitIds}` a read returns, because the read and the write of a definition are the same document.  Reserved ids (the `sec_rt_` prefix, `sec_alpha`, `sec_uncat`) are rejected: those belong to server-computed sections, and letting a client claim one would collide at render time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The section&#39;s id, stable across saves. **Omit it for a new section** — the server assigns one. Round-trip the id from a definition read to keep an existing section&#39;s identity, and with it whatever the client hangs off that id. Must not be a server-reserved id such as &#x60;sec_uncat&#x60;. | [optional] 
**label** | **str** | Section label as the admin typed it. | 
**unit_ids** | **List[str]** | Units placed in this section, in order. A unit may appear in only one section, and a bed must sit in the same section as its dorm — placing the dorm alone brings its beds along, which is the normal case. At most 20,000 unit ids across the whole definition; the ceiling is on the definition, not on one section, so it cannot be expressed as &#x60;maxItems&#x60; here. | 

## Example

```python
from cloudbeds_pms.models.definition_section_request_schema import DefinitionSectionRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DefinitionSectionRequestSchema from a JSON string
definition_section_request_schema_instance = DefinitionSectionRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DefinitionSectionRequestSchema.to_json())

# convert the object into a dict
definition_section_request_schema_dict = definition_section_request_schema_instance.to_dict()
# create an instance of DefinitionSectionRequestSchema from a dict
definition_section_request_schema_from_dict = DefinitionSectionRequestSchema.from_dict(definition_section_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


