# GetDistributionSettingsResponseSchemaSettingsInnerOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value to send back when saving this setting. | 
**label** | **str** | Display text for this choice. A raw value is returned if its label cannot be resolved. | 

## Example

```python
from cloudbeds_pms.models.get_distribution_settings_response_schema_settings_inner_options_inner import GetDistributionSettingsResponseSchemaSettingsInnerOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDistributionSettingsResponseSchemaSettingsInnerOptionsInner from a JSON string
get_distribution_settings_response_schema_settings_inner_options_inner_instance = GetDistributionSettingsResponseSchemaSettingsInnerOptionsInner.from_json(json)
# print the JSON string representation of the object
print(GetDistributionSettingsResponseSchemaSettingsInnerOptionsInner.to_json())

# convert the object into a dict
get_distribution_settings_response_schema_settings_inner_options_inner_dict = get_distribution_settings_response_schema_settings_inner_options_inner_instance.to_dict()
# create an instance of GetDistributionSettingsResponseSchemaSettingsInnerOptionsInner from a dict
get_distribution_settings_response_schema_settings_inner_options_inner_from_dict = GetDistributionSettingsResponseSchemaSettingsInnerOptionsInner.from_dict(get_distribution_settings_response_schema_settings_inner_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


