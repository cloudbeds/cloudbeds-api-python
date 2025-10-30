# PatchDistributionSettingsRequestSchemaSettingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of the setting to update. Must be one of the valid distribution setting keys. | 
**value** | **object** | Parsed setting value. Can be string, number, boolean, or structured data, depending on the setting you are updating. | 

## Example

```python
from cloudbeds_pms.models.patch_distribution_settings_request_schema_settings_inner import PatchDistributionSettingsRequestSchemaSettingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PatchDistributionSettingsRequestSchemaSettingsInner from a JSON string
patch_distribution_settings_request_schema_settings_inner_instance = PatchDistributionSettingsRequestSchemaSettingsInner.from_json(json)
# print the JSON string representation of the object
print(PatchDistributionSettingsRequestSchemaSettingsInner.to_json())

# convert the object into a dict
patch_distribution_settings_request_schema_settings_inner_dict = patch_distribution_settings_request_schema_settings_inner_instance.to_dict()
# create an instance of PatchDistributionSettingsRequestSchemaSettingsInner from a dict
patch_distribution_settings_request_schema_settings_inner_from_dict = PatchDistributionSettingsRequestSchemaSettingsInner.from_dict(patch_distribution_settings_request_schema_settings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


