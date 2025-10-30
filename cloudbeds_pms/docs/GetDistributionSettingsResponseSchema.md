# GetDistributionSettingsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**List[GetDistributionSettingsResponseSchemaSettingsInner]**](GetDistributionSettingsResponseSchemaSettingsInner.md) | List of distribution settings with their values and permissions. | 

## Example

```python
from cloudbeds_pms.models.get_distribution_settings_response_schema import GetDistributionSettingsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetDistributionSettingsResponseSchema from a JSON string
get_distribution_settings_response_schema_instance = GetDistributionSettingsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GetDistributionSettingsResponseSchema.to_json())

# convert the object into a dict
get_distribution_settings_response_schema_dict = get_distribution_settings_response_schema_instance.to_dict()
# create an instance of GetDistributionSettingsResponseSchema from a dict
get_distribution_settings_response_schema_from_dict = GetDistributionSettingsResponseSchema.from_dict(get_distribution_settings_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


