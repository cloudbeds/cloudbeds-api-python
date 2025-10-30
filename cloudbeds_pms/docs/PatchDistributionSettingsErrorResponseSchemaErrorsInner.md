# PatchDistributionSettingsErrorResponseSchemaErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The setting key that caused the error. | 
**message** | **str** | The reason why the update failed. | 

## Example

```python
from cloudbeds_pms.models.patch_distribution_settings_error_response_schema_errors_inner import PatchDistributionSettingsErrorResponseSchemaErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PatchDistributionSettingsErrorResponseSchemaErrorsInner from a JSON string
patch_distribution_settings_error_response_schema_errors_inner_instance = PatchDistributionSettingsErrorResponseSchemaErrorsInner.from_json(json)
# print the JSON string representation of the object
print(PatchDistributionSettingsErrorResponseSchemaErrorsInner.to_json())

# convert the object into a dict
patch_distribution_settings_error_response_schema_errors_inner_dict = patch_distribution_settings_error_response_schema_errors_inner_instance.to_dict()
# create an instance of PatchDistributionSettingsErrorResponseSchemaErrorsInner from a dict
patch_distribution_settings_error_response_schema_errors_inner_from_dict = PatchDistributionSettingsErrorResponseSchemaErrorsInner.from_dict(patch_distribution_settings_error_response_schema_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


