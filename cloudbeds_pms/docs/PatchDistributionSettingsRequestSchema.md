# PatchDistributionSettingsRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**List[PatchDistributionSettingsRequestSchemaSettingsInner]**](PatchDistributionSettingsRequestSchemaSettingsInner.md) | List of distribution settings to update. | 

## Example

```python
from cloudbeds_pms.models.patch_distribution_settings_request_schema import PatchDistributionSettingsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PatchDistributionSettingsRequestSchema from a JSON string
patch_distribution_settings_request_schema_instance = PatchDistributionSettingsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PatchDistributionSettingsRequestSchema.to_json())

# convert the object into a dict
patch_distribution_settings_request_schema_dict = patch_distribution_settings_request_schema_instance.to_dict()
# create an instance of PatchDistributionSettingsRequestSchema from a dict
patch_distribution_settings_request_schema_from_dict = PatchDistributionSettingsRequestSchema.from_dict(patch_distribution_settings_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


