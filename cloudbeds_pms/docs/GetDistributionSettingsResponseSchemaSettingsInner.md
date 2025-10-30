# GetDistributionSettingsResponseSchemaSettingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **object** | Parsed setting value. Can be string, number, boolean, or structured data, depending on the setting. | [optional] 
**permission** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.get_distribution_settings_response_schema_settings_inner import GetDistributionSettingsResponseSchemaSettingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDistributionSettingsResponseSchemaSettingsInner from a JSON string
get_distribution_settings_response_schema_settings_inner_instance = GetDistributionSettingsResponseSchemaSettingsInner.from_json(json)
# print the JSON string representation of the object
print(GetDistributionSettingsResponseSchemaSettingsInner.to_json())

# convert the object into a dict
get_distribution_settings_response_schema_settings_inner_dict = get_distribution_settings_response_schema_settings_inner_instance.to_dict()
# create an instance of GetDistributionSettingsResponseSchemaSettingsInner from a dict
get_distribution_settings_response_schema_settings_inner_from_dict = GetDistributionSettingsResponseSchemaSettingsInner.from_dict(get_distribution_settings_response_schema_settings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


