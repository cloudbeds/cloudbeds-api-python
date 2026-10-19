# PatchUnitRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connecting_unit_ids** | **List[str]** | List of connecting unit IDs. Send empty array to clear all connections. Omit to leave unchanged. | [optional] 
**name** | **str** | Unit name. Must be non-empty when provided. | [optional] 
**description** | **str** | Unit description (empty string to clear). | [optional] 
**images** | **List[object]** | Unit images. Send empty array to clear. FE is responsible for uploading the assets and passing back the resulting image objects. | [optional] 
**name_langs** | **Dict[str, str]** | Per-language map of the unit name (keys are IETF language codes, e.g. \&quot;en\&quot;, \&quot;pt-br\&quot;, \&quot;es-es\&quot;). Send the full map the property supports — missing keys will be persisted as empty strings on read. | [optional] 
**description_langs** | **Dict[str, str]** | Per-language map of the unit description (keys are IETF language codes). Same shape as &#x60;nameLangs&#x60;. | [optional] 
**doorlock_id** | **str** | Door lock integration identifier (null to clear). | [optional] 

## Example

```python
from cloudbeds_pms.models.patch_unit_request_schema import PatchUnitRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PatchUnitRequestSchema from a JSON string
patch_unit_request_schema_instance = PatchUnitRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PatchUnitRequestSchema.to_json())

# convert the object into a dict
patch_unit_request_schema_dict = patch_unit_request_schema_instance.to_dict()
# create an instance of PatchUnitRequestSchema from a dict
patch_unit_request_schema_from_dict = PatchUnitRequestSchema.from_dict(patch_unit_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


