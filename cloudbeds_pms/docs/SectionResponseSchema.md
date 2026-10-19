# SectionResponseSchema

One entry of the ordered section index. Carries no units — every unit names its section by `sectionId`, so a unit appears exactly once no matter how the sections are arranged.  `id` is opaque and must never be parsed. What a section *is* comes from `kind` plus its companion field: `entity` for an entity-backed section, `systemLabel` for a computed one. A new sectioning dimension (floor, building) adds an `entity.type` value rather than a new section shape.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Opaque section id. Never parsed by the client. | 
**kind** | **str** | &#x60;entity&#x60;: backed by a domain record, see &#x60;entity&#x60;. &#x60;custom&#x60;: named by an admin. &#x60;system&#x60;: computed by the server, see &#x60;systemLabel&#x60;. | 
**label** | **str** | Display label, resolved server-side and rendered verbatim. Not localized: property-authored labels come back as authored, and the two server-generated labels ship English here plus a &#x60;systemLabel&#x60; token for the client to translate. Rendered verbatim. | 
**system_label** | **str** | Which computed section this is, for clients that need to treat one specially — the uncategorized tail is default-collapsed, for instance. | [optional] 
**entity** | [**SectionEntityResponseSchema**](SectionEntityResponseSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.section_response_schema import SectionResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SectionResponseSchema from a JSON string
section_response_schema_instance = SectionResponseSchema.from_json(json)
# print the JSON string representation of the object
print(SectionResponseSchema.to_json())

# convert the object into a dict
section_response_schema_dict = section_response_schema_instance.to_dict()
# create an instance of SectionResponseSchema from a dict
section_response_schema_from_dict = SectionResponseSchema.from_dict(section_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


