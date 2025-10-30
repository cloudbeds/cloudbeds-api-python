# PatchDistributionSettingsErrorResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Human-readable explanation of the error. | 
**errors** | [**List[PatchDistributionSettingsErrorResponseSchemaErrorsInner]**](PatchDistributionSettingsErrorResponseSchemaErrorsInner.md) | List of errors encountered during the update. | 

## Example

```python
from cloudbeds_pms.models.patch_distribution_settings_error_response_schema import PatchDistributionSettingsErrorResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PatchDistributionSettingsErrorResponseSchema from a JSON string
patch_distribution_settings_error_response_schema_instance = PatchDistributionSettingsErrorResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PatchDistributionSettingsErrorResponseSchema.to_json())

# convert the object into a dict
patch_distribution_settings_error_response_schema_dict = patch_distribution_settings_error_response_schema_instance.to_dict()
# create an instance of PatchDistributionSettingsErrorResponseSchema from a dict
patch_distribution_settings_error_response_schema_from_dict = PatchDistributionSettingsErrorResponseSchema.from_dict(patch_distribution_settings_error_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


